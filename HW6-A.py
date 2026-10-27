# 讀取原餐費 B、人數 N、服務費百分比 C、折價券金額 R
b, n, c, r = map(int, input().split())

# 計算服務費（原餐費乘以服務費百分比，不足 1 元的部分捨去，使用整數運算）
service_fee = (b * c) // 100

# 計算應付總額（原餐費 + 服務費 - 折價券金額；若小於 0 改為 0）
total = b + service_fee - r
if total < 0:
    total = 0

# 計算每人基礎分攤金額 q 與餘數 a（人數）
q = total // n
a = total % n

# 剩餘的餘數分配給 b 人（每人多付 1 元），使總人數為 n
b_count = a

# 輸出應付總額與分帳方式（共三行）
print(total)
print(f"{q} {n - a}")
print(f"{q + 1} {a}")