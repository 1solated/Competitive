n = int(input())
S = [input() for i in range(n)]

d = {}
for s in S:
    c = s[0]
    if c not in 'MARCH': continue
    if c in d:
        d[c]+=1
    else:
        d[c] = 1

if len(d) <= 2:
    print(0)
    exit()

d_list = list(d.values());
n = len(d_list)
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            ans += d_list[i] * d_list[j] * d_list[k]

print(ans)
