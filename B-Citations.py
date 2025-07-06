N = int(input())
A = list(map(int, input().split()))

max_value = 0
for x in range(N + 1):  # 0～N だけ調べればOK！
    count = sum(1 for a in A if a >= x)
    if count >= x:
        max_value = x

print(max_value)
