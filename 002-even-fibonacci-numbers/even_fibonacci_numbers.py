import sys

num = int(sys.argv[1])


def fibo_even_sum(n):
    i = 1
    x = 1
    y = 1
    sum = 0
    while i < n:
        z = x + y
        if z % 2 == 0:
            sum += z
        x = y
        y = z
        i += 1
    return sum


print(fibo_even_sum(num))
