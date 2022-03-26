#hello

x = open("text1.txt", 'r+')
content = x.readlines()
x.write("something else")
print(content)
x.close()

x = open("text1.txt", 'w+')
x.writelines(['this is first line. ', 'this is second line of code. ', 'this is third line of code.'])
x.close()

x = open("text1.txt", 'a')
x.write("this is fourth line of code")
x.close()



