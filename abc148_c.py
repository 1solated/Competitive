from fractions import gcd

a, b = map(int, input().split())
t = gcd(a, b)
print(a // t * b)
