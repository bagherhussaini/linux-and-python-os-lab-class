n = int(input('Enter for n: '))


def fibonacci(num):
    fibonacci_list = [0, 1]
    while num <= 0:
        print('Enter Positive Number')
        num = int(input('Enter for n: '))
    if num == 1:
        print(fibonacci_list[0])
    else:
        for i in range(2, num):
            fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
        print(fibonacci_list)


fibonacci(n)
