s = input()
t = s
t = t[::-1]
ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans+=1
print(int(ans/2))