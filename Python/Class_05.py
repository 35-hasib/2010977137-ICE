# # Task 01

# n = int(input('Enter N : '))

# list = []
# for i in range(n):
#     list.append(int(input(f'Enter number {i+1} : ')))
# t = int(input('Enter terget number : '))

# if (t in list):
#     print('Number Found !')
# else:
#     print('Number not found !')

# # Task 02

# n = int(input('Enter N : '))

# for i in range(n):
#     if(i % 2 == 0): print(i+1 , end=' ')

# # Task 03

# n = int(input('Enter N : '))

# list = []
# for i in range(n):
#     list.append(int(input(f'Enter number {i+1} : ')))

# for i in range(len(list)):
#     if(list[i]%5 == 0):
#         print(list[i])
#         break

# # Task 04
# sum = 0
# while True:
#     i = int(input('Enter a number : '))
#     if(i < 0):
#         print(f'Sum of positive number : {sum}')
#         break
#     else:
#         sum += i

# # Task 05

# n = 20
# for i in range(n):
#     if((i+1)%3 == 0):
#         continue
#     else:
#         print(i+1, end=' ')



# h = input('Enter Hello : ')
# for i in h:
#     print(i,end=",")

# list = [1,2,3,4]

# for i,j in enumerate(list):
#     print(i,j)

# Login

list_id = ['hasib','tarik','zisan','abir','zisan','touhid']
list_pass = ['11','22','33','44','55','66']

id = input('ID : ')
if(id in list_id):
    for i in range(len(list_id)):
        if(list_id[i] == id):
            pas = input('Password : ')
            if(list_pass[i] == pas):
                print('Loged in')
                exit()
            else:
                print('Invalid Password !!')
                break
else:
    print('Invalid ID !!')


