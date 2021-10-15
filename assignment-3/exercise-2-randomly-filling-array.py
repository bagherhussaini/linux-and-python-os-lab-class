from random import randint
numbers_list = []
n = randint(1, 50)
for i in range(n):
    unique_number = randint(-100, 100)
    if unique_number not in numbers_list:
        numbers_list.append(unique_number)
repeated_numbers = n - len(numbers_list)
print('Array(List) Length: ', n, '\nRandomly Repeated Numbers: ',
      repeated_numbers, '\nArray(List) with No Duplicates: ', numbers_list)
