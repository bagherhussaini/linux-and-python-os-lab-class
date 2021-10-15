numbers_list = []
list_length = int(input('Enter the Length of Array(List): '))
while list_length <= 0:
    list_length = int(input('Don\'t Enter Negative or Zero :|\nEnter the Length of Array(List): '))
for i in range(list_length):
    print('Enter Element[', i+1, ']: ', end='')
    numbers_list.append(int(input()))
flag = True
previous_item = numbers_list[0]
for number in numbers_list:
    if number < previous_item:
        flag = False
    previous_item = number
if flag:
    print('Yes')
else:
    print('No')
