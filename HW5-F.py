# 讀取正整數 n
n = int(input())

# 使用巢狀 for 迴圈產生乘法表
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 計算乘積並以欄寬 4 靠右對齊格式印出，不換行
        print(f"{i * j:4d}", end="")
    # 完成一列後換行
    print()