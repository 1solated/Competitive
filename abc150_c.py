def main():
    from itertools import permutations
    n = int(input())
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))

    p = list(permutations(range(1, n + 1)))
    d = {i: j for j, i in enumerate(p)}
    print(abs(d[a] - d[b]))


main()