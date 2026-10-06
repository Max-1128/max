n = int(input())

# 拆解百位、十位、個位數
a = n // 100
b = (n // 10) % 10
c = n % 10

# 計算總和、乘積與反轉整數
total_sum = a + b + c
total_prod = a * b * c
reversed_num = c * 100 + b * 10 + a

# 依序輸出結果
print(f"{a} {b} {c}")
print(total_sum)
print(total_prod)
print(reversed_num)