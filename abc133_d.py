n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] *= 2

offset = 0
for i in range(n):
    offset = a[i]-offset
x = offset/2

cur = x
for i in range(n):
    print(int(cur), end=' ')
    cur = a[i]-cur
