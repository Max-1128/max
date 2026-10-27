# 讀取商品種類數 N
n = int(input())

# 初始化平行串列儲存商品資訊
names = []
subtotals = []

max_subtotal = -1
top_product = ""

# 迴圈讀取每種商品的名稱、單價、數量並計算優惠後小計
for i in range(n):
    line = input().split()
    name = line[0]
    price = int(line[1])
    quantity = int(line[2])
    
    # 計算買 3 送 1 優惠後的應付數量：每 3 件中 1 件免費
    # 也就是實際需付費的數量為 (quantity // 3) * 2 + (quantity % 3)
    paid_quantity = (quantity // 3) * 2 + (quantity % 3)
    subtotal = paid_quantity * price
    
    names.append(name)
    subtotals.append(subtotal)
    
    # 尋找花費最多的商品（最高小計，若同額選輸入較早者）
    if subtotal > max_subtotal:
        max_subtotal = subtotal
        top_product = name

# 計算總小計並套用滿 1000 折 100 優惠（限折一次）
total_sum = sum(subtotals)
if total_sum >= 1000:
    final_amount = total_sum - 100
else:
    final_amount = total_sum

# 輸出 N 行各商品的名稱與優惠後小計
for i in range(n):
    print(f"{names[i]} {subtotals[i]}")

# 輸出最後應付總額與花費最多的商品
print(f"TOTAL {final_amount}")
print(f"TOP {top_product}")