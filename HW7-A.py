# 定義停車費計算函式 parking_fee(minutes)
def parking_fee(minutes):
    if minutes == 0:
        return 0
    
    # 計算 30 分鐘的區間數（不足 30 分鐘也算一個區間，使用向上取整的整數運算）
    intervals = (minutes + 29) // 30
    fee = intervals * 30
    
    # 單次停車費最高 200 元
    if fee > 200:
        fee = 200
        
    return fee

# 讀取記錄數 N
n = int(input())

# 讀取 N 個停車分鐘數
minutes_list = list(map(int, input().split()))

# 計算各車費用並存入串列
fees = []
for m in minutes_list:
    fees.append(parking_fee(m))

# 計算總收入
total_revenue = sum(fees)

# 輸出第一行：N 個費用，以一個空白分隔，順序與輸入相同
print(*(fees))

# 輸出第二行：所有費用的總和
print(total_revenue)