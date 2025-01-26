numerator = int(input('Enter numerator : '))
denominator = int(input('Enter denominator : '))

try:
    n = numerator//denominator
    print(n)
except:
    print('Cant divided by zero !!')
