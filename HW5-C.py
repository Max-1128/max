# 讀取非負整數 n
n = int(input())

# 初始化階乘結果變數為 1
factorial = 1

# 使用 for 迴圈累乘從 1 到 n 的所有整數
for i in range(1, n + 1):
    factorial *= i

# 輸出階乘結果
print(factorial)