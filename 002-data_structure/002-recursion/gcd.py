def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a%b)

if __name__ == '__main__':
    print(gcd(12, 4))
