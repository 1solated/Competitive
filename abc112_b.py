N, T = map(int, input().split())
ans = 1000000
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        ans = min(ans, c)
print("TLE" if ans == 1000000 else ans)
