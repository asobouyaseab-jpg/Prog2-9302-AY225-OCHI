import os
# Silence TensorFlow & MediaPipe C++ log spam in terminal
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['GLOG_minloglevel'] = '2'

import urllib.request
import tkinter as tk
from tkinter import ttk, messagebox
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from PIL import Image, ImageTk

# --- 1. MODEL DOWNLOAD & INITIALIZATION ---
MODEL_PATH = "hand_landmarker.task"
if not os.path.exists(MODEL_PATH):
    print("Downloading hand_landmarker.task model (one-time setup)...")
    url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
    urllib.request.urlretrieve(url, MODEL_PATH)

base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    min_hand_presence_confidence=0.6,
    running_mode=vision.RunningMode.IMAGE
)
detector = vision.HandLandmarker.create_from_options(options)

# Skeletal connections and landmark indices
HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),        # Thumb
    (0, 5), (5, 6), (6, 7), (7, 8),        # Index
    (5, 9), (9, 10), (10, 11), (11, 12),   # Middle
    (9, 13), (13, 14), (14, 15), (15, 16), # Ring
    (13, 17), (17, 18), (18, 19), (19, 20),# Pinky
    (0, 17)                                # Palm base
]
TIP_IDS = [4, 8, 12, 16, 20]
PIP_IDS = [2, 6, 10, 14, 18]

def get_finger_states(landmarks, handedness="Right"):
    fingers = []
    # Thumb: check X-axis displacement based on handedness
    if handedness == "Right":
        fingers.append(1 if landmarks[TIP_IDS[0]].x < landmarks[PIP_IDS[0]].x else 0)
    else:
        fingers.append(1 if landmarks[TIP_IDS[0]].x > landmarks[PIP_IDS[0]].x else 0)

    # 4 Fingers: check Y-axis (tip higher than PIP joint)
    for i in range(1, 5):
        fingers.append(1 if landmarks[TIP_IDS[i]].y < landmarks[PIP_IDS[i]].y else 0)
    return fingers

def classify_gesture(fingers):
    if fingers == [1, 1, 1, 1, 1]:
        return "HELLO"
    elif fingers == [0, 0, 0, 0, 0]:
        return "YES (A)"
    elif fingers == [1, 1, 0, 0, 0]:
        return "L (NO)"
    elif fingers == [0, 1, 1, 0, 0]:
        return "PEACE (V)"
    elif fingers == [1, 1, 0, 0, 1]:
        return "I LOVE YOU"
    elif fingers == [1, 0, 0, 0, 0]:
        return "GOOD / OK"
    elif fingers == [0, 1, 0, 0, 0]:
        return "ONE"
    return None

# --- 2. MAXITCARE TELEPROMPTER GUI ---
class MaxITCareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MaxITCare 窶� Sign Language Teleprompter")
        self.root.geometry("1180x720")
        self.root.configure(bg="#121214")

        # Camera setup
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Recognition state
        self.current_gesture = "Detecting..."
        self.last_stable_gesture = None
        self.consecutive_frames = 0
        self.DEBOUNCE_THRESHOLD = 18
        self.teleprompter_text = ""
        self.is_running = True

        self.build_ui()

        # Keyboard shortcuts and graceful exit hooks
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.bind("<Escape>", lambda e: self.on_closing())
        self.root.bind("<q>", lambda e: self.on_closing())
        self.root.bind("<Q>", lambda e: self.on_closing())
        self.root.bind("<c>", lambda e: self.clear_teleprompter())
        self.root.bind("<C>", lambda e: self.clear_teleprompter())

        # Start frame loop
        self.update_frame()

    def build_ui(self):
        # Top Header
        header = tk.Frame(self.root, bg="#1a1a1e", height=50)
        header.pack(fill=tk.X, side=tk.TOP)

        title = tk.Label(
            header,
            text="MaxITCare : Accessibility & Inclusion Teleprompter",
            font=("Segoe UI", 14, "bold"),
            fg="#00E676",
            bg="#1a1a1e"
        )
        title.pack(side=tk.LEFT, padx=20, pady=10)

        status = tk.Label(
            header,
            text="笳� ENGINE ACTIVE",
            font=("Segoe UI", 10, "bold"),
            fg="#00E676",
            bg="#1a1a1e"
        )
        status.pack(side=tk.RIGHT, padx=20)

        # Main Layout Container
        main_body = tk.Frame(self.root, bg="#121214")
        main_body.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)

        # Left Column: Video Viewport
        video_frame = tk.Frame(main_body, bg="#1e1e24", bd=2, relief=tk.FLAT)
        video_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        video_label_title = tk.Label(
            video_frame,
            text="Real-Time Gesture Tracking (OpenCV + MediaPipe)",
            font=("Segoe UI", 10),
            fg="#a1a1aa",
            bg="#1e1e24"
        )
        video_label_title.pack(anchor="w", padx=10, pady=5)

        self.video_canvas = tk.Label(video_frame, bg="#000000")
        self.video_canvas.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))

        # Right Column: Teleprompter Dashboard
        tele_panel = tk.Frame(main_body, bg="#1e1e24", width=420)
        tele_panel.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        tele_panel.pack_propagate(False)

        # Gesture Detection Card
        card = tk.Frame(tele_panel, bg="#27272a", padx=15, pady=12)
        card.pack(fill=tk.X, padx=15, pady=(15, 10))

        tk.Label(card, text="CURRENT SIGN DETECTED", font=("Segoe UI", 9, "bold"), fg="#a1a1aa", bg="#27272a").pack(anchor="w")
        self.sign_display = tk.Label(card, text="WAITING...", font=("Segoe UI", 22, "bold"), fg="#00E676", bg="#27272a")
        self.sign_display.pack(anchor="w", pady=(4, 6))

        # Hold Progress Bar
        self.progress = ttk.Progressbar(card, orient="horizontal", mode="determinate", maximum=self.DEBOUNCE_THRESHOLD)
        self.progress.pack(fill=tk.X)

        # Transcript Output Area
        tk.Label(tele_panel, text="LIVE SPEECH-TO-TEXT STREAM", font=("Segoe UI", 9, "bold"), fg="#a1a1aa", bg="#1e1e24").pack(anchor="w", padx=15, pady=(10, 4))

        self.tele_box = tk.Text(
            tele_panel,
            wrap=tk.WORD,
            font=("Segoe UI", 15),
            bg="#121214",
            fg="#ffffff",
            insertbackground="#ffffff",
            bd=0,
            padx=12,
            pady=12
        )
        self.tele_box.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))

        # Control Buttons
        btn_frame = tk.Frame(tele_panel, bg="#1e1e24")
        btn_frame.pack(fill=tk.X, padx=15, pady=(0, 15))

        clear_btn = tk.Button(
            btn_frame,
            text="Clear (C)",
            command=self.clear_teleprompter,
            bg="#3f3f46",
            fg="#ffffff",
            relief=tk.FLAT,
            font=("Segoe UI", 10, "bold"),
            padx=12,
            pady=8,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        copy_btn = tk.Button(
            btn_frame,
            text="Copy Text",
            command=self.copy_text,
            bg="#0284c7",
            fg="#ffffff",
            relief=tk.FLAT,
            font=("Segoe UI", 10, "bold"),
            padx=12,
            pady=8,
            cursor="hand2"
        )
        copy_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        exit_btn = tk.Button(
            btn_frame,
            text="Exit (Q)",
            command=self.on_closing,
            bg="#e11d48",
            fg="#ffffff",
            relief=tk.FLAT,
            font=("Segoe UI", 10, "bold"),
            padx=12,
            pady=8,
            cursor="hand2"
        )
        exit_btn.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))

    def update_frame(self):
        if not self.is_running:
            return

        success, frame = self.cap.read()
        if not success:
            self.root.after(30, self.update_frame)
            return

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        # MediaPipe Detection
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        detection_result = detector.detect(mp_image)

        detected_token = None

        if detection_result.hand_landmarks:
            for idx, landmarks in enumerate(detection_result.hand_landmarks):
                handedness = "Right"
                if detection_result.handedness and idx < len(detection_result.handedness):
                    handedness = detection_result.handedness[idx][0].category_name

                # Draw skeleton
                for start_idx, end_idx in HAND_CONNECTIONS:
                    pt1 = (int(landmarks[start_idx].x * w), int(landmarks[start_idx].y * h))
                    pt2 = (int(landmarks[end_idx].x * w), int(landmarks[end_idx].y * h))
                    cv2.line(frame, pt1, pt2, (0, 230, 118), 2)

                for lm in landmarks:
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(frame, (cx, cy), 4, (255, 120, 0), -1)

                finger_states = get_finger_states(landmarks, handedness)
                detected_token = classify_gesture(finger_states)

        # Teleprompter stream debounce
        if detected_token:
            self.sign_display.config(text=detected_token, fg="#00E676")
            if detected_token == self.last_stable_gesture:
                self.consecutive_frames += 1
                if self.consecutive_frames == self.DEBOUNCE_THRESHOLD:
                    self.teleprompter_text += f"{detected_token} "
                    self.tele_box.delete("1.0", tk.END)
                    self.tele_box.insert(tk.END, self.teleprompter_text)
                    self.tele_box.see(tk.END)
            else:
                self.last_stable_gesture = detected_token
                self.consecutive_frames = 1
        else:
            self.sign_display.config(text="No Hand Detected", fg="#71717a")
            self.consecutive_frames = 0

        self.progress["value"] = self.consecutive_frames

        # Fast OpenCV resize to avoid GUI lag
        display_frame = cv2.resize(frame, (620, 465))
        display_rgb = cv2.cvtColor(display_frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(display_rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        self.video_canvas.imgtk = imgtk
        self.video_canvas.configure(image=imgtk)

        self.root.after(15, self.update_frame)

    def clear_teleprompter(self):
        self.teleprompter_text = ""
        self.tele_box.delete("1.0", tk.END)

    def copy_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.teleprompter_text.strip())
        messagebox.showinfo("Copied", "Teleprompter text copied to clipboard!")

    def on_closing(self):
        self.is_running = False
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
        self.root.quit()
        self.root.destroy()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = MaxITCareApp(root)
    root.mainloop()
