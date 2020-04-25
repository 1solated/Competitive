x = int(input())
cur = 0
for i in range(x+1):
    cur += i
    if cur >= x:
        print(i)
        exit()