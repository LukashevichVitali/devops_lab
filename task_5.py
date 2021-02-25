def slf_number(left, right):
    def self_dividing(number):
        for d in str(number):
            if d == '0' or n % int(d) > 0:
                return False
        return True
    out = []
    for n in range(left, right + 1):
        if self_dividing(n):
            out.append(n)
    return out


print(slf_number(int(input()), int(input())))
