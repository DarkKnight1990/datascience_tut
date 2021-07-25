import math

def reverse(n):
    if n == 0:
        return 0

    digit = int(math.log10(n))
    return (n%10 * pow(10, digit)) + reverse(n//10)

def checkPalindrome(n):
    reversed = reverse(n)
    return n == reversed

if __name__ == '__main__':
    print(checkPalindrome(999))
