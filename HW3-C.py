x1, x2, x3 = map(int, input().split())

# 計算平均數
m = (x1 + x2 + x3) / 3

# 計算母體變異數
v = ((x1 - m)**2 + (x2 - m)**2 + (x3 - m)**2) / 3

# 格式化輸出保留小數點後 2 位
print(f"{m:.2f}")
print(f"{v:.2f}")