# 定義 normalize(text) 函式，回傳整理後的字串（只保留英文字母與數字，並轉成小寫）
def normalize(text):
    result = []
    for char in text:
        # 檢查是否為英文大寫字母、小寫字母或數字
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('0' <= char <= '9'):
            result.append(char.lower())
    return "".join(result)

# 定義 is_palindrome(text, left, right) 函式，使用遞迴比較兩端並縮小範圍
def is_palindrome(text, left, right):
    # 基準情形：當左右指標相遇或交錯時，代表確認完畢，回傳 True
    if left >= right:
        return True
    # 若兩端字元不同，則不是迴文
    if text[left] != text[right]:
        return False
    # 遞迴呼叫自身，縮小範圍檢查內側字元
    return is_palindrome(text, left + 1, right - 1)

# 讀取一整行原始密碼
line = input()

# 呼叫 normalize 進行前處理
cleaned_text = normalize(line)

# 判斷整理後是否為空字串或只有一個字元（均視為迴文）
if len(cleaned_text) <= 1:
    is_pal = True
else:
    is_pal = is_palindrome(cleaned_text, 0, len(cleaned_text) - 1)

# 輸出結果：若是迴文輸出 YES，否則輸出 NO（輸出必須為大寫）
if is_pal:
    print("YES")
else:
    print("NO")