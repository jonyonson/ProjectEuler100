import sys

num = int(sys.argv[1])


def largest_prime_factor(n):
    i = 2
    max = 1
    while i <= n:
        if n % i == 0:
            max = i
            n /= i
        else:
            i += 1
    return max


print(largest_prime_factor(num))
