# 讀取非負整數金額 m
m = int(input())

# 初始化硬幣總數
coin_count = 0

# 使用 while 迴圈搭配貪婪策略逐枚扣除硬幣
while m > 0:
    if m >= 50:
        m -= 50
    elif m >= 10:
        m -= 10
    elif m >= 5:
        m -= 5
    else:
        m -= 1
    coin_count += 1

# 輸出最少硬幣數
print(coin_count)