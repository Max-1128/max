# 讀取向後移動的位置數 K
k = int(input())

# 完整讀取第二行的原始訊息 S（保留頭尾與連續空白）
s = input()

# 初始化加密後的結果字串串列
encrypted_chars = []

for char in s:
    ascii_val = ord(char)
    
    # 檢查是否為大寫英文字母 (A-Z 的 ASCII 範圍為 65 至 90)
    if 65 <= ascii_val <= 90:
        # 在 0-25 範圍內進行位移，並使用 % 26 處理字母表循環，再轉回大寫 ASCII
        new_ascii = 65 + (ascii_val - 65 + k) % 26
        encrypted_chars.append(chr(new_ascii))
        
    # 檢查是否為小寫英文字母 (a-z 的 ASCII 範圍為 97 至 122)
    elif 97 <= ascii_val <= 122:
        # 在 0-25 範圍內進行位移，並使用 % 26 處理字母表循環，再轉回小寫 ASCII
        new_ascii = 97 + (ascii_val - 97 + k) % 26
        encrypted_chars.append(chr(new_ascii))
        
    else:
        # 非英文字母（數字、空白、標點符號等）保持原樣
        encrypted_chars.append(char)

# 將串列組合成完整字串並輸出
print("".join(encrypted_chars))