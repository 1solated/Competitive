a, b, k = map(int, input().split())

if k > a:
    k -= a
    a = 0
else:
    print(a - k, b)
    exit()

if k > b:
    print(0, 0)
    exit()
else:
    print(0, b - k)
