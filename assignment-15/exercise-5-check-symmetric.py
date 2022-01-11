def check_symmetric(lst):
    array_length = len(lst)
    flag = True
    for i in range(array_length):
        if lst[i] != lst[array_length - 1 - i]:
            flag = False
            break
    if flag:
        print('Result: Symmetric')
    else:
        print('Result: Not Symmetric')


print('Enter some numbers with an space:')
array = list(map(int, input().split()))
check_symmetric(array)
