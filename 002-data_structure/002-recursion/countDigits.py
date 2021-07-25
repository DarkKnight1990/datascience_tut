def count_digit(n, count=0):
    if n <= 9:
        return count + 1
    count += 1
    return count_digit(n//10, count)

if __name__ == '__main__':
    print(count_digit(8986600))
