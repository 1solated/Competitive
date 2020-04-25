n = int(input())
s = []
p = []
for i in range(n):
    ss, pp = input().split()
    s.append(ss)
    p.append(int(pp))

for x,y in zip(s,p):
    if y > sum(p)/2:
        print(x)
        exit()
else:
    print('atcoder')