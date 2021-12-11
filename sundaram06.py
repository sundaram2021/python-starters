def summer_69(array):
    array = []
    for i in array:
        if i == 6:
            return sum(array)-6
        elif i == 9:
            return sum(array)-9
        else:
            pass
    return sum(array)
print(summer_69([1,3,6,7]))

