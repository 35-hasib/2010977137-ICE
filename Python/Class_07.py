# # import os

# # os.chdir(r"F:/2010977137-ICE/Python")
# with open('test.txt', 'r') as file:
#     content = file.read()
#     file.close()

# print(content)

# with open('test.txt', 'a') as file: # if use 'w' it will not overwrite the file
#     file.write("\nThis is the appended line")
#     file.close()



# file = open('test.txt', 'r')
# content = file.readlines()
# # print(content)
# print(len(content))
# count = 0
# for i in content:
#     count += 1
#     print(f'{count}: {i}', end='')
# file.close()


file = open('test.txt', 'r')
# content = file.readlines()
# n = len(content)
# print(n)
# line = file.readline()
# print(line)
for i in range(5):
    line = file.readline()
    if(line == 'hasib\n'):
        print(5)
    else:
        print(0)
file.close()