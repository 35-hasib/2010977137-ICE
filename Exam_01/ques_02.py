
from collections import Counter

def analize_text(text):
    text = text.split()
    print(len(text))
    c = 0
    for i in text:
        for j in i:
            c = c + len(j)
    print(c)
    most_com = Counter(text).most_common(1)[0][0]
    print(most_com)


# text = open('text.txt', 'r')
# line = text.readlines()
# line = str(line)
line = input('KKKK : ')
analize_text(line)
# text.close()


