# 讀取非負整數 n
n = int(input())

# 初始化各位數總和變數
total_sum = 0

# 針對 n = 0 的邊界情況，若 n 為 0 則總和為 0
if n == 0:
    total_sum = 0
else:
    # 使用 while 迴圈逐位剝離並加總
    while n > 0:
        total_sum += n % 10  # 取得目前個位數並累加
        n = n // 10          # 去掉個位數

# 輸出各位數總和
print(total_sum)