# list = ['Hasib', 'Abir', 'Hasan', 'Tanzim', 'Tarik', 'Zisan']

# print(list[-6].title())
# list.append('Hello')
# print(list)
# list.extend(['how', 'are', 'you'])
# print(list)
# list.insert(2,'Hi')
# print(list)
# list.remove('Hi')
# print(list)
# x = list.pop()
# print(list)


# list = [-5,-1,3,-2,8,-10]
# list.sort(key=abs,reverse=True)
# print(list)

# n_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(n_list[0][1])

# Task 01

fruits = ['apple', 'banana', 'cherry', 'pineapple']
print(fruits)
print(f'First eliment : {fruits[0]} \nLast eliment : {fruits[3]}')

# Task 02

fruits.append('orange')
print(fruits)
fruits.insert(2, 'grape')
print(fruits)
fruits[0] = 'kiwi'
print(fruits)

# Task 03

ln = [5,3,8,6,7,3]
ln.sort()
print(ln)
ln.reverse()
print(ln)
ln.pop()
print(ln)

print(ln.count(3))
