# 讀取一行中的三個整數 a、b、c
a, b, c = map(int, input().split())

# 利用條件判斷找出最大值（不使用 max() 函式）
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c

# 輸出最大值整數
print(max_val)