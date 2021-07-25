## reverse the given number
import math

def reverse(n):
    if n == 0:
        return 0

    digit = int(math.log10(n))
    return (n%10 * pow(10, digit)) + reverse(n//10)

if __name__ == '__main__':
    print(reverse(90))
