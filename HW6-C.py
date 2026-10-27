# 讀取每日目標 G 與七天的步數串列
goal = int(input())
steps = list(map(int, input().split()))

# 1. 計算總步數
total_steps = sum(steps)

# 2. 計算達標天數（步數大於或等於每日目標 G）
achieve_days = 0
for s in steps:
    if s >= goal:
        achieve_days += 1

# 3. 找出最高步數出現的所有日期（第 1 至第 7 天，若有多天最高則全部輸出）
max_step = max(steps)
max_days = []
for i in range(7):
    if steps[i] == max_step:
        max_days.append(i + 1)

# 4. 計算最長連續達標天數（只計本週，不把第 7 天與第 1 天接起來）
max_consecutive = 0
current_consecutive = 0
for s in steps:
    if s >= goal:
        current_consecutive += 1
        if current_consecutive > max_consecutive:
            max_consecutive = current_consecutive
    else:
        current_consecutive = 0

# 輸出四行結果
print(total_steps)
print(achieve_days)
print(*(max_days))
print(max_consecutive)