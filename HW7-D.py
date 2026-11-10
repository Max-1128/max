# 定義遞迴 gcd(a, b) 函式，以 b == 0 為基底情況，gcd 函式內不得使用迴圈或推導式
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 定義 simplify_recipe(tea, milk, syrup) 函式，呼叫自訂 gcd 求三數的最大公因數，回傳三個最簡比例值
def simplify_recipe(tea, milk, syrup):
    # 找出所有大於 0 的數值來計算共同最大公因數
    vals = [tea, milk, syrup]
    current_gcd = 0
    for v in vals:
        if v > 0:
            if current_gcd == 0:
                current_gcd = v
            else:
                current_gcd = gcd(current_gcd, v)
    
    # 若全為 0 或找不到大於 1 的公因數，公因數視為 1
    if current_gcd == 0:
        current_gcd = 1
        
    return tea // current_gcd, milk // current_gcd, syrup // current_gcd

# 讀取配方數 N
n = int(input())

results = []
for _ in range(n):
    parts = input().split()
    tea = int(parts[0])
    milk = int(parts[1])
    syrup = int(parts[2])
    
    t_simp, m_simp, s_simp = simplify_recipe(tea, milk, syrup)
    results.append(f"{t_simp} {m_simp} {s_simp}")

# 輸出 N 行，依序輸出最簡比例
for res in results:
    print(res)