def draw_table(num1, num2):
    for i in range(num1):
        for j in range(num2):
            if i % 2 == 0:
                if j % 2 == 0:
                    print('#', end='')
                else:
                    print('*', end='')
            else:
                if j % 2 == 0:
                    print('*', end='')
                else:
                    print('#', end='')
        print()


n, m = int(input('Enter for n: ')), int(input('Enter for m: '))
while n < 0 or m < 0:
    print('Enter Positive Numbers')
    n, m = int(input('Enter for n: ')), int(input('Enter for m: '))
draw_table(n, m)
