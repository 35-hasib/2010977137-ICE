# list = [x**2 for x in range(1,6)]
# print(list)

# list = [(i, 'even')if i%2==0 else (i, 'odd') for i in range(1,10)]

# print(list)

# n = [[1,2,3,4,5,6,7], [8,9,10]]
# result = []
# for sublist in n:
#     sqrt = [ x**2 for x in sublist if x%2==0 ]
#     result.extend(sqrt)
# print(result)

# list_2d = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# print(list_2d)
# flatten_list = [i for sublist in list_2d for i in sublist]
# print(flatten_list)

# list_3d = [[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]]
# flatten_list = [i for sub in [i for sub in list_3d for i in sub] for i in sub]
# print(flatten_list)

# i for sublit in 2dlist for i in sublist               17

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# row = len(matrix)
# column = len(matrix[0])
# out = []
# for i in range(row):
#     for j in range(column):
#         if i == j:
#             out.append(matrix[i][j] * matrix[i][j])
#         else:
#             out.append(0)

# print(out)

matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix2 = [
    [1,2],
    [4,5],
    [7,8]
]

row_1 = len(matrix1)
row_2 = len(matrix2)
col_1 = len(matrix1[0])
col_2 = len(matrix2[0])

if col_1 != row_2:
    print('Multiplication not possible !!')
else:
    out = [[0 for row in range(col_2)] for col in range(row_1)]
    print(out)
    for i in range(row_1):
        for j in range(col_2):
            for k in range(col_1):
                out[i][j] += matrix1[i][k] * matrix2[k][j]

    print(out)