def count_primes(nums):
    if nums < 2:
        return 0
    result = [2]
    while True:
        if nums % 2 == 0 and nums % 3 == 0:
            return 0
        else:
            lst = result.append(nums)
            return lst
        result2 = len(lst)
print(count_primes(100))

