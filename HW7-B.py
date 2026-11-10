# 定義 is_prime(n) 函式，回傳布林值 True 或 False
def is_prime(n):
    if n <= 1:
        return False
    # 只需檢查至除數平方不大于 n 的範圍
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# 讀取區間的兩個整數 L 與 R
l, r = map(int, input().split())

primes = []

# 主程式對區間內每個整數呼叫 is_prime(n)
for num in range(l, r + 1):
    if is_prime(num):
        primes.append(num)

# 計算個數與總和
count = len(primes)
total_sum = sum(primes)

# 輸出第一行：依遞增順序輸出所有質數，若沒有質數則輸出 NONE
if count == 0:
    print("NONE")
else:
    print(*(primes))

# 輸出第二行：質數個數與總和，以一個空白分隔；若沒有質數時輸出 0 0
print(f"{count} {total_sum}")