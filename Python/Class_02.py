# Data type

# name = '    Hasib  '      # String
# age = 23            # integer
# height = 5.7        # Float
# is_student = True   # Boolean



# name = input('Enter Your name : ')
# print(f'Its good to meet you {name}')
# print(f'Length of your name is : {len(name)}')
# age = int(input('What is your age :'))
# print(f'It will be {age+1} in a yesr')
# a = 100
# b = 80
# c = 79
# d = 19
# e = 5
# print(a>b>c>d>e)


# while True:
#     n1 = input('Enter 1st person name : ')
#     a1 = int(input('Enter age : '))
#     n2 = input('Enter 1st person name : ')
#     a2 = int(input('Enter age : '))

#     if(a1 > a2): print(f'{n1} is older than {n2}')
#     elif(a2 > a1): print(f'{n2} is older than {n1}')
#     else: print('Same age !!')

pw = float(input('Enter Weight : '))

if(pw <= 0.1): print(1,'$')
elif(pw <= 5): print(5,'$')
elif(pw <= 10): print(10,'$')
elif(pw <= 15): print(15,'$')
elif(pw <= 20): print(20,'$')
else: print('Not supported !!')

