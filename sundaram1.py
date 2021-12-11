str = 'print only that word in this sentence which starts with letter s'
list = str.split()
for i in list:
    if i[0] == 's' :
        print(i)