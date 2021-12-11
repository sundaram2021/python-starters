def num(a, b, c):
    for num in range(1, 12):
        sum = a+b+c

        if sum <= 21:
            return sum
        elif sum > 21 and (a == 11 or b == 11 or c == 11):
            return sum-10
        elif sum > 21:
            return 'bust'
        else:
            pass
print(num(9,4,2))






