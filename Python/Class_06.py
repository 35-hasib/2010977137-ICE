
# # Prime 


# def cal_prime(start, end):
#     c=0
#     for i in range(start, end + 1):
#         if i < 2: 
#             continue
#         k = 0
#         for j in range(2, int(i**0.5) + 1):
#             if i % j == 0:
#                 k = 1
#                 break
#         if k == 0:
#             print(i, end=' ')
#             c += 1
#     print(c)

# start = 1
# end = 200
# cal_prime(start, end)


# def find_longest_word(s):
#     list = []
#     c = 0
#     for i in range(len(s)):
#         if(s[i] != ' '): c+=1
#         else:
#             list.append(c)
#             c = 0
#     for i in range(len(s)):
#         if(s[i] != ' '): c+=1
#         else:
#             i
#             c = 0
#     return list

# print(find_longest_word('The quick brown fox jumps over the lazy dog'))

# def find_longest_word(sentence: str):
#     words = sentence.split()
    
#     longest_word = ""
#     max_length = 0
    
#     for word in words:
#         if len(word) > max_length:
#             longest_word = word
#             max_length = len(word)
    
#     return longest_word, max_length

# sentence = "The quick brown fox jumps over the lazy dog"
# longest_word, length = find_longest_word(sentence)
# print(f"The longest word = {longest_word} and length =  {length}")

# def func(x, y=9):
#     print(x,y)
#     pass
# func(7,3)


# def func(a,b):
#     print(a,b)

# func(b=2,a=9)


# def num(*ar):
#     for i in ar:
#         print(i)

# num(1,2,3,4,5)
# num(1,4,5)

# num(1,2,3,5)


# Lambda

# mul = lambda x,y : x*y
# print(mul(5,3))

# mul = (lambda x,y : x*y)(3,7)
# print(mul)

# def fibo(n):
#     if n == 1: return 0
#     if n == 2: return 1
#     return fibo(n-1) + fibo(n-2)

# n = int(input('Enter N : '))
# for i in range(1,n+1):
#     print(fibo(i), end=' ')

# Task 01

def is_palindrom(s):
    s2 = s[::-1]
    print(s, s2)  
    if s == s2:
        print('palindrome !!')
    else:
        print('not palindrome !!')

is_palindrom('maam4')

