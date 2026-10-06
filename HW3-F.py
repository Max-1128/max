# 讀取矩陣 A (第 1、2 行)
a, b = map(int, input().split())
c, d = map(int, input().split())

# 計算行列式 det
det = a * d - b * c

# 計算反矩陣元素
r1c1 = d / det
r1c2 = -b / det
r2c1 = -c / det
r2c2 = a / det

# 輸出結果 (分 2 行，保留小數點後 4 位)
print(f"{r1c1:.4f} {r1c2:.4f}")
print(f"{r2c1:.4f} {r2c2:.4f}")