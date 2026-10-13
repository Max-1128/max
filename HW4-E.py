# 讀取一元二次方程式的係數 a、b、c
a, b, c = map(int, input().split())

# 計算判別式 D = b^2 - 4 * a * c
d = b * b - 4 * a * c

# 根據判別式 D 的值判斷相異實根個數
if d > 0:
    print(2)
elif d == 0:
    print(1)
else:
    print(0)