str = 'print every word in this sentence that has even number of letters'
list = str.split()
for i in list:
    if len(i) % 2 == 0:
        print(i)