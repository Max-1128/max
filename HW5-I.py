# 讀取非負整數 n
n = int(input())

# 初始化反轉結果變數
reversed_num = 0

# 若 n 為 0，直接處理；否則使用 while 迴圈反轉數字
if n == 0:
    reversed_num = 0
else:
    while n > 0:
        digit = n % 10             # 取得目前個位數
        reversed_num = reversed_num * 10 + digit  # 累積反轉結果
        n = n // 10                # 去掉個位數

# 輸出反轉後的整數（自動不保留前導零）
print(reversed_num)