# 讀取西元年份 y
y = int(input())

# 依據閏年規則進行條件判斷
if y % 400 == 0:
    print("Leap")
elif y % 100 == 0:
    print("Common")
elif y % 4 == 0:
    print("Leap")
else:
    print("Common")