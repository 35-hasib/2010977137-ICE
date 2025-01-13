# set

# set1 = {1, 2, 3,3,3,3,3,3,3, 4, 5}
# set2 = {4, 5, 6, 7, 8}  
# dic = {} # This is not a set, it is a dictionary
# set3 = set() # This is an empty set
# set3 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # This is a set with 10 elements
# set4 = set((1,2,3,4,'kjghkjf'))
# print(set1)
# print(set2)
# print(set3)
# print(set4)

# set1.add(6)
# print(set1)
# # set1.remove(4)
# # print(set1)
# set1.discard(4)
# print(set1)

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 5, 6, 7, 8}
# set3 = set1.union(set2)
# print(set3)
# set4 = set1.intersection(set2)
# print(set4)
# set5 = set2.difference(set1)
# print(set5)
# set6 = set1.symmetric_difference(set2)
# print(set6)

# my_set = {1, 2, 3, 4, 5}
# for i in my_set:
#     print(i)

# my_set = {1, 2, 3, 4, 5}
# print(1 in my_set)

# my_set = {15,3.55,'hello',True,False}
# print(my_set)

# Union = |, Intersection = &, Difference = -, Symmetric Difference = ^

## Dictionary
# Syntax: dic = {'key1':'value1', 'key2':'value2', 'key3':'value3'} or dict(key1='value1', key2='value2', key3='value3')
# for empty dictionary: dic = {} or dic = dict()

# dic = {'name':'John', 'age':25,'color':['red','green','blue']}
# print(dic['name'])
# print(dic['age'])
# print(dic['color'][2])

# dic['name'] = 'Smith'
# print(dic)

# d = {'name':'John', 'age':25,'color':['red','green','blue']}
# dk = d.keys()
# dk = list(dk)
# print(dk)
# dp = d.values()
# dp = list(dp)
# print(dp)
# ditem = d.items()
# ditem = list(ditem)
# print(ditem)


#Task 01


# # Task 02

# def remove_duplicates(lst):
#     return list(set(lst))

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
# print(remove_duplicates(lst))

# # Task 03

# dic = {'s1':{'name': 'Hasib', 'age': 23, 'grade': {'math':82, 'phy':79, 'chem':49}}}
# print(dic)

# More Excercise
# # 1. Write a Python provide sentance and count the number of latter in the sentence value pair using set

# def count_letter(sentence):
#     letter = set(sentence)
#     letter_dict = {}
#     for i in letter:
#         if(i == ' '):
#             continue
#         letter_dict[i] = sentence.count(i)
#     return letter_dict

# sentence = '''Tarik : Hello hasib how are you doing today ? 
#             Hasib : I am doing good, how about you ? 
#             Tarik : I am also doing good, thank you for asking'''

# print(count_letter(sentence))

# 1. Write a Python provide sentance and count the number of word in the sentence value pair using set

# def count_word(sentence):
#     word = sentence.split()
#     word_dict = {}
#     for i in word:
#         word_dict[i] = sentence.count(i)
#     return word_dict

# sentence = '''Tarik : Hello hasib how are you doing today ?
#             Hasib : I am doing good, how about you ?
#             Tarik : I am also doing good, thank you for asking'''

# print(count_word(sentence))


# from collections import Counter
# import string

# text = input("Enter a text: ")
# translator = str.maketrans('', '', string.punctuation)
# normalized_text = text.translate(translator)
# words = normalized_text.split()
# word_counts = Counter(words)

# for word, count in word_counts.items():
#     print(f'{word}: {count}')

def fac(n):
    if n == 0 or n == 1:
        return 1
    return n * fac(n-1)
print(fac(5))