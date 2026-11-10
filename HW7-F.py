# 定義 best_total(prices, index, remaining) 遞迴函式
def best_total(prices, index, remaining):
    # 基準情形：如果已經檢查完所有商品，或者剩餘預算為 0，則無法再花費更多
    if index == len(prices) or remaining == 0:
        return 0
    
    # 分支 1：不選目前商品，直接考慮下一個商品
    exclude = best_total(prices, index + 1, remaining)
    
    # 分支 2：若買得起目前商品，考慮選擇目前商品並遞迴計算剩餘預算
    include = 0
    if prices[index] <= remaining:
        include = prices[index] + best_total(prices, index + 1, remaining - prices[index])
    
    # 回傳兩者中的最大值
    return max(exclude, include)

# 讀取商品件數 N 與預算 B
n, b = map(int, input().split())

# 讀取 N 個商品的價格
prices = list(map(int, input().split()))

# 主程式呼叫 best_total(prices, 0, b)
max_spending = best_total(prices, 0, b)

# 輸出不超過預算的最大購物總額
print(max_spending)