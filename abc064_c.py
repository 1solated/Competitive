n = int(input())
A = list(map(int, input().split()))

l = [0] * 9
mn = 0
for i in A:
    t = min(i // 400, 8)
    l[t] += 1
for i in range(8):
    if l[i] != 0:
        mn += 1
if mn == 0:
    mn = 1
    mx = l[8]
else:
    mx = mn + l[8]

print(mn, mx)
