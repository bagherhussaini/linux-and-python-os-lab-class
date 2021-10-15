number = (input('Enter a Number: '))
s = 0
digits = []
for digit in number:
    s += int(digit) ** len(number)
    digits.append(int(digit))
if s == int(number):
    print('Yes')
    for i in range(len(digits)):
        print(digits[i], '^', len(number), end=' ')
        if i < len(digits) - 1:
            print('+', end=' ')
    print('=', s)
else:
    print('No')
