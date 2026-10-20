# 讀取兩個正整數 a 與 b
a, b = map(int, input().split())

# 使用 while 迴圈搭配輾轉相除法求最大公因數
while b != 0:
    r = a % b
    a = b
    b = r

# 當 b 為 0 時，當下的 a 就是最大公因數
print(a)