# 讀取三個邊長並轉換為串列後排序
sides = sorted(map(int, input().split()))
a, b, c = sides[0], sides[1], sides[2]

# 判斷是否能構成面積大於 0 的三角形（任意兩邊長度之和嚴格大於第三邊）
if a + b <= c:
    print("Invalid")
elif a == b and b == c:
    print("Equilateral")
elif a == b or b == c:
    print("Isosceles")
else:
    print("Scalene")