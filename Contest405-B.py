N, M = map(int, input().split())
A = list(map(int, input().split()))

required = set(range(1, M + 1))

count = 0
for i in range(N):
    if required.issubset(A):
        A.pop()
        count += 1
    else:
        break

print(count)
