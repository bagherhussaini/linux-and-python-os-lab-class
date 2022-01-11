def triangle(row):
    matrix = [[1 for i in range(row)] for j in range(row)]
    for i in range(row):
        for j in range(1, i):
            matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]
    for i in range(row):
        for j in range(i + 1):
            print(matrix[i][j], end=' ')
        print('')


r = int(input('Enter the row(s): '))
triangle(r)
