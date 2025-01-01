# 01
name = input('Enter Your Name :')
age = input('Enter Your Age :')

print(f'Hello {name}, you are {age} years old.')

# 02

n1 = int(input('Enter Number 1 : '))
n2 = int(input('Enter Number 2 : '))

print(f'Addition        : {n1} + {n2} = {n1+n2}')
print(f'Subtraction     : {n1} - {n2} = {n1-n2}')
print(f'Multiplication  : {n1} * {n2} = {n1*n2}')
if (n2 == 0): print('Cant divide by 0')
else: print(f'Division        : {n1} / {n2} = {n1/n2}')

# 03

n = int(input('Enter a number : '))
if(n%2==1): print('Odd !!')
else: print('Even !!')
if(n%3 == 0 and n%5 == 0):
    print('Diviaible by 3 and 5 !!')
else: print('Not Diviaible by 3 and 5 !!')