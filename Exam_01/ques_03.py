

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("Multiple35")
    elif num % 3 == 0:
        print("Multiple3")
    elif num % 5 == 0:
        print("Multiple5")
    else:
        print(num)