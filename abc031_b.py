l, h = map(int, input().split())
a = [int(input()) for _ in range(int(input()))]
for t in a:
    print(l - t if l > t else "0" if h >= t else "-1")
