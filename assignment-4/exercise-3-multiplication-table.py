def draw_table(num1, num2):
    for i in range(1, num1 + 1):
        for j in range(1, num2 + 1):
            print(i * j, end='\t')
        print()


n, m = int(input('Enter for n: ')), int(input('Enter for m: '))
while n < 0 or m < 0:
    print('Enter Positive Numbers')
    n, m = int(input('Enter for n: ')), int(input('Enter for m: '))
draw_table(n, m)
