def my_ints(n):
    for i in range(90, 111):
        if n == i:
            return True
    for j in range(190, 211):
        if n == j:
            return True
    return False
print(my_ints(111))
