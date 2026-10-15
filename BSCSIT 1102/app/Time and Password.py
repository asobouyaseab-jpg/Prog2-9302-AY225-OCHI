import time
import sys
import threading

def custom_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end='\r'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write(print_end + '\n')

def progress_bar_thread(seconds, stop_event):
    for i in range(seconds + 1):
        if stop_event.is_set():
            break
        custom_progress_bar(i, seconds, prefix='Time Remaining:', suffix=f'{seconds - i} seconds left', length=50)
        time.sleep(1)
    custom_progress_bar(seconds, seconds, prefix='Time Remaining:', suffix='0 seconds left', length=50)

def countdown_with_password(seconds, password="nobutoshi", max_attempts=3):
    print("\n=== Time-Limited Password Entry ===")
    attempts = max_attempts
    stop_event = threading.Event()

    # Start progress bar in a separate thread
    progress_thread = threading.Thread(target=progress_bar_thread, args=(seconds, stop_event))
    progress_thread.start()

    for t in range(seconds, -1, -1):
        # Move cursor below progress bar and clear previous input lines
        sys.stdout.write('\033[2J')  # Clear screen (works in most terminals)
        sys.stdout.flush()
        
        # Redisplay progress bar at the top
        custom_progress_bar(seconds - t, seconds, prefix='Time Remaining:', suffix=f'{t} seconds left', length=50)
        
        # Add separation
        print("\n\n=== Password Input ===")

        # Display warning at 5 seconds
        if t == 5:
            print("Warning: Only 5 seconds remaining!\n")

        # Display password prompt
        if attempts > 0:
            guess = input(f"Enter password ({attempts} attempts left): ")
            if guess == password:
                print("\nCorrect! You Win!")
                stop_event.set()
                progress_thread.join()
                return True
            else:
                print("\nWrong password!")
                attempts -= 1
        else:
            print("\nToo many wrong tries. You failed.")
            stop_event.set()
            progress_thread.join()
            return False

        time.sleep(1)

    print("\nTime's up! You failed.")
    stop_event.set()
    progress_thread.join()
    return False

def main():
    try:
        seconds = int(input("Enter the time in seconds for the countdown: "))
        if seconds <= 0:
            print("Please enter a positive number of seconds.")
        else:
            countdown_with_password(seconds)
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
    