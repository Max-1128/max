# 讀取一整行原始帳號（完整讀取整行，保留換行前的字串）
line = input()

# 1. 移除頭尾的半形空白
stripped = line.strip()

# 2. 把英文字母轉成小寫
lowered = stripped.lower()

# 3. 將中間每一段連續半形空白改成一個底線（使用 split() 與 join()）
words = lowered.split()
formatted_account = "_".join(words)

# 4. 檢查是否合法
# 合法條件：長度 6 至 16，每個字元只能是 a-z、0-9 或底線，開頭可為數字或底線
is_valid = True
length = len(formatted_account)

if length < 6 or length > 16:
    is_valid = False
else:
    # 檢查每個字元是否合法
    for char in formatted_account:
        if not (('a' <= char <= 'z') or ('0' <= char <= '9') or char == '_'):
            is_valid = False
            break

# 輸出結果：第一行輸出整理後的帳號，第二行輸出 VALID 或 INVALID
print(formatted_account)
if is_valid:
    print("VALID")
else:
    print("INVALID")