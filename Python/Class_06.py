
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

def find_longest_word(sentence: str):
    words = sentence.split()
    
    longest_word = ""
    max_length = 0
    
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    
    return longest_word, max_length

sentence = "The quick brown fox jumps over the lazy dog"
longest_word, length = find_longest_word(sentence)
print(f"The longest word = {longest_word} and length =  {length}")