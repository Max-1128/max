# 讀取菜單筆數 M
m = int(input())

drink_names = []
drink_prices = []
drink_counts = []

for _ in range(m):
    parts = input().split()
    drink_names.append(parts[0])
    drink_prices.append(int(parts[1]))
    drink_counts.append(0)

# 讀取訂單筆數 N
n = int(input())

order_names = []
order_drinks = []
order_qtys = []

for _ in range(n):
    parts = input().split()
    s_name = parts[0]
    d_name = parts[1]
    qty = int(parts[2])
    
    order_names.append(s_name)
    order_drinks.append(d_name)
    order_qtys.append(qty)
    
    # 累計該飲料總杯數
    idx = drink_names.index(d_name)
    drink_counts[idx] += qty

# 計算每種飲料優惠後的單價
discounted_prices = []
for i in range(m):
    price = drink_prices[i]
    if drink_counts[i] >= 10:
        price -= 5
    discounted_prices.append(price)

# 輸出 M 行：DRINK 飲料名稱 總杯數（依菜單順序）
for i in range(m):
    print(f"DRINK {drink_names[i]} {drink_counts[i]}")

# 統計每位同學應付金額（依姓名在訂單首次出現的順序排列）
student_names = []
student_totals = []

for i in range(n):
    s_name = order_names[i]
    d_name = order_drinks[i]
    qty = order_qtys[i]
    
    # 找出該飲料對應的優惠後單價
    d_idx = drink_names.index(d_name)
    cost = qty * discounted_prices[d_idx]
    
    if s_name not in student_names:
        student_names.append(s_name)
        student_totals.append(cost)
    else:
        s_idx = student_names.index(s_name)
        student_totals[s_idx] += cost

# 輸出每位同學的應付金額
for i in range(len(student_names)):
    print(f"STUDENT {student_names[i]} {student_totals[i]}")

# 輸出 TOTAL 全班總額
total_sum = sum(student_totals)
print(f"TOTAL {total_sum}")