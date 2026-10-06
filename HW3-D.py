# 讀取點 P 的座標 (x1, y1)
x1, y1 = map(int, input().split())

# 讀取點 Q 的座標 (x2, y2)
x2, y2 = map(int, input().split())

# 計算兩點距離平方：(x2 - x1)^2 + (y2 - y1)^2
distance_squared = (x2 - x1)**2 + (y2 - y1)**2

# 輸出整數結果
print(distance_squared)