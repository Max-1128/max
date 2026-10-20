# 讀取目前存款 s、每天新增金額 d 及目標金額 t
s, d, t = map(int, input().split())

# 初始化經過的天數為 0
days = 0

# 使用 while 迴圈模擬每天存款增加，直到存款達到或超過目標為止
while s < t:
    s += d
    days += 1

# 輸出最少需要的天數
print(days)