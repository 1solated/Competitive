a,b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    c = str(i)[::-1]
    if str(i) == c:
        cnt+=1
print(cnt)
