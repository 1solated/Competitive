import math


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


n = int(input())
s = factorization(math.factorial(n))

ans = 0
# 2,4,4
a = 0
b = 0
print(s)
for t in s:
    print(t)
    if t[1]==2:
        a+=1
    elif t[1]==4:
        b+=1
ans += a*b*(b-1)

# 2,24

print(ans)