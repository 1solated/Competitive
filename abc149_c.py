import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    else:
        return True


x = int(input())
while (True):
    if (is_prime(x)):
        print(x)
        exit()
    else:
        x += 1
