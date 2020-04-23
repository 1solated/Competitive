def solve():
    n = int(input())
    a, b = input().split()
    ans = []
    for i in range(n):
        ans.append(a[i])
        ans.append(b[i])
    print("".join(ans))


solve()
