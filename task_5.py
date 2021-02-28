def slf_number(numbers_x):
    def self_dividing(number):
        for d in str(number):
            if d == '0' or n % int(d) > 0:
                return False
        return True

    out = []
    for n in range(numbers_x[0], numbers_x[1] + 1):
        if self_dividing(n):
            out.append(n)
    return out


numbers_x = [int(x) for x in input().split()]
print(slf_number(numbers_x))
