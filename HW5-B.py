# 讀取區間起點 a、終點 b 與整數 k
a, b, k = map(int, input().split())

# 初始化倍數個數與總和變數
count = 0
total_sum = 0

# 使用 for 迴圈遍歷區間 [a, b]
for i in range(a, b + 1):
    if i % k == 0:
        count += 1
        total_sum += i

# 輸出倍數個數及總和，以空白分隔
print(f"{count} {total_sum}")