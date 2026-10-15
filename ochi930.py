import cv2
import numpy as np

def inspect_product(image_path):
    # 1. 画像の読み込みと前処理 (メンバー2の担当パート)
    img = cv2.imread(image_path)
    if img is None:
        print("エラー: 画像が見つかりません。")
        return
        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # 二値化処理（背景と製品を分離）
    _, thresh = cv2.threshold(blurred, 50, 255, cv2.THRESH_BINARY_INV)

    # 2. 輪郭の抽出と検出 (メンバー3の担当パート)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    output = img.copy()
    
    # 良品判定の基準面積（ピクセル数。対象の画像に合わせて調整してください）
    EXPECTED_AREA = 50000 
    TOLERANCE = 5000       # 許容誤差

    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        # 一定数値以下の小さすぎるノイズは無視させる
        if area < 1000:
            continue
            
        # 3. 判定ロジックと結果の描画 (メンバー4の担当パート)
        # 基準値の範囲内なら良品(PASS)、外れていれば不良品(FAIL)
        if (EXPECTED_AREA - TOLERANCE) <= area <= (EXPECTED_AREA + TOLERANCE):
            status = "PASS (OK)"
            color = (0, 255, 0) # 緑色
        else:
            status = "FAIL (DEFECT)"
            color = (0, 0, 255) # 赤色

        # 輪郭とステータスを画像に描き出す
        cv2.drawContours(output, [cnt], -1, color, 3)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.putText(output, f"{status} Area: {int(area)}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # 結果の表示
    cv2.imshow("Original Product", img)
    cv2.imshow("Preprocessed (Threshold)", thresh)
    cv2.imshow("Inspection Result", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# テスト実行 (任意の製品画像を 'product.jpg' として用意してください)
# inspect_product('product.jpg')
