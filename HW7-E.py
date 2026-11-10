# 定義 count_ways(step, n, blocked, memo) 遞迴記憶化函式
def count_ways(step, n, blocked, memo):
    # 基準情形 1：如果超越目標階梯，或者目前位置是損壞的階梯，則此走法無效，回傳 0
    if step > n or blocked[step]:
        return 0
    # 基準情形 2：剛好走到第 n 階，代表找到一種有效走法，回傳 1
    if step == n:
        return 1
    # 記憶化檢查：若已經計算過從此階梯出發的走法數，直接回傳結果
    if memo[step] != -1:
        return memo[step]
    
    # 遞迴探索：分別計算再走 1 階與再走 2 階的走法數總和
    memo[step] = count_ways(step + 1, n, blocked, memo) + count_ways(step + 2, n, blocked, memo)
    
    return memo[step]

# 讀取階梯總數 N 與損壞階梯數 K
first_line = input().split()
n = int(first_line[0])
k = int(first_line[1])

# 建立長度 n + 1 的布林串列記錄損壞階梯（初始皆為 False）
blocked = [False] * (n + 1)

if k > 0:
    broken_steps = list(map(int, input().split()))
    for b in broken_steps:
        blocked[b] = True

# 建立長度 n + 1 的整數串列作為 memo 暫存表，初值皆為 -1
memo = [-1] * (n + 1)

# 主程式呼叫 count_ways(0, n, blocked, memo)
total_ways = count_ways(0, n, blocked, memo)

# 輸出不同走法數
print(total_ways)