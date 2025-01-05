# print(bin(12))
# print(bin(12 >> 1))
# print(int('00001100',2))

# a = 60
# b = 13

# print(f'{a&b} {a|b} {a^b} {~a} {a<<2} {a>>2}')
# print(f'{bin(a&b)} {bin(a|b)} {bin(a^b)} {bin(~a)} {bin(a<<2)} {bin(a>>2)}')

# print(5//2)
# print(5/2)

# a = 2
# b = 1.4
# print(type(a-b))

# a = 6 + 4j
# b = 3 + 6j
# print(abs(a-b))


# list = [1,2,3,4,5,6,7,8,9]
# print(41 in list)

# a = [1,2,3,4,5,6,7,8,9]
# b = [1,2,3,4,5,6,7,8,9]
# c = a
# # is , is not for memory location check
# print(a is not c)

## Control flow 

## Sir problem

id1 = '2010977137'
pass1 = '1234'

while True:
    id2 = input('Enter ID :')
    if(id1 != id2):
        print('Invalid ID !! Try again....')
    else:
        pass2 = input('Enter password :')
        if(pass1 == pass2):
            print('Login Successfull !!')
            break
        else:
            print('Invalid Psaaword !! Try again....')



