n = input('Enter grades saparated by space : ')
n = n.split()
max_n = 0
min_n = int(n[0])
sum = 0

for i in n:
    nn = int(i)
    if nn > max_n:
        max_n = nn
    if nn < min_n:
        min_n = nn
    sum = sum + nn
avg = sum/len(n)

c = 0
for i in n:
    nn = int(i)
    if(nn > avg): c = c+1

print(f'Highest grade : {max_n}')
print(f'Lowest grade : {min_n}')
print(f'Average grade : {avg}')
print(f'Number of grades above average : {c}')

