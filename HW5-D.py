# 讀取學生人數 n
n = int(input())

# 讀取 n 個學生成績
scores = list(map(int, input().split()))

# 初始化總分與及格人數
total_score = 0
pass_count = 0

# 使用 for 迴圈逐筆累加總分並統計及格人數
for score in scores:
    total_score += score
    if score >= 60:
        pass_count += 1

# 計算平均分數
average_score = total_score / n

# 輸出結果（平均分數保留小數點後 2 位，及格人數分行輸出）
print(f"{average_score:.2f}")
print(pass_count)