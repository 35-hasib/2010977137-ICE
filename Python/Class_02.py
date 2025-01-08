def is_palindrom(s):
    s2 = list(s)
    s1 = []
    n = len(s)
    for i in range(n):
        s1.append(s[n-i])
    if s2 == s1:
        print('palindrom !!')
    else:
        print(' not palindrom !!')

is_palindrom('maam')