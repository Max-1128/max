# 讀取非負整數 n
n = int(input())

# 處理 n 等於 0 的邊界情況
if n == 0:
    print(0)
else:
    # 初始化前兩項 F(0) = 0, F(1) = 1
    a, b = 0, 1
    # 使用 for 迴圈從第 2 項迭代到第 n 項
    for i in range(2, n + 1):
        a, b = b, a + b
    # 輸出第 n 項的值
    print(b)