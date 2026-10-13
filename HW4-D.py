# 讀取停車小時數 h
h = int(input())

# 累進計費計算
if h <= 2:
    cost = h * 30
elif h <= 5:
    cost = 2 * 30 + (h - 2) * 20
else:
    cost = 2 * 30 + 3 * 20 + (h - 5) * 10

# 輸出總停車費（不包含貨幣符號或單位）
print(cost)