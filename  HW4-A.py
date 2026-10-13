# 讀取一行中的兩個整數 a 與 b
a, b = map(int, input().split())

# 根據大小關係判斷並輸出對應的英文結果
if a > b:
    print("Greater")
elif a < b:
    print("Less")
else:
    print("Equal")