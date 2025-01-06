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

# fruits = ['apple', 'banana', 'cherry', 'pineapple']
# print(fruits)
# print(f'First eliment : {fruits[0]} \nLast eliment : {fruits[3]}')

# # Task 02

# fruits.append('orange')
# print(fruits)
# fruits.insert(2, 'grape')
# print(fruits)
# fruits[0] = 'kiwi'
# print(fruits)

# # Task 03

# ln = [5,3,8,6,7,3]
# ln.sort()
# print(ln)
# ln.reverse()
# print(ln)
# ln.pop()
# print(ln)

# print(ln.count(3))

# Tuple
# t = tuple((1,2,3,'hi'))
# print(t)

# print(t[0:3:2]) # Slicing

# t1 = (1,2,3,4)
# l1 = [11,22,33,44]
# l2t = tuple(l1)
# print(l2t)

# # Task 01

# fruits = 'apple', 'banana', 'cherry'
# numbers = 1,2,3,4,5
# nested_tuple = fruits, numbers
# print(nested_tuple)

# # Task 02
# print(fruits[0])
# print(numbers[4])
# n2 = nested_tuple[1]
# print(n2)
# print(n2[0])

# # Task 03
# fruits += 'orange', 'grape'
# print(fruits)

# numbers *= 3
# print(numbers)

# if ('banana' in fruits):
#     print('banana is present in the tuple !')
# else:
#     print('banana is not present in the tuple !')
    
# # Task 04

# print(len(numbers))
# print(max(numbers))
# print(min(numbers))

# numbers = list(numbers)
# print(numbers)

# # Task 05

# info = 'Hasib', 21, 'ICE'
# print(info[0])
# info = list(info)
# info[1] = 22
# info = tuple(info)
# print(info)

# More Tasks

n = int(input('Enter N : '))

list = []

for i in range(n):
    number = int(input(f'Enter number {i+1} : '))
    list.append(number)

t = tuple(list)
print(id(t))

print(t[0], t[n-1])
list.reverse()
t = tuple(list)
print(id(t))