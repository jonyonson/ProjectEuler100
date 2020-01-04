import sys

num = int(sys.argv[1])


def multiples_of_3_and_5(n):
    sum = 0
    for i in range(3, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


print(multiples_of_3_and_5(num))
