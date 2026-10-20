# 初始化總和與讀取第一個整數
total = 0
num = int(input())

# 使用 while 迴圈持續讀取，直到遇到 0 為止
while num != 0:
    total += num
    num = int(input())

# 輸出 0 之前所有數值的總和
print(total)