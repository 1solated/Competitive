a = sorted(list(map(int, input().split())))
ans = (a[2]-a[0])//2
a[0] += (a[2]-a[0])//2 * 2
ans += (a[2]-a[1])//2
a[1] += (a[2]-a[1])//2 * 2
a.sort()
if a[0]==a[1]==a[2]:
    print(ans)
elif a[0]==a[1]:
    print(ans+1)
else:
    print(ans+2)
