num1, num2 = int(input('Enter 1st Number: ')), int(input('Enter 2nd Number: '))
gcd = 0
while num1 == 0 or num2 == 0:
    print('Don\'t Enter Zero :|')
    num1 = int(input('Enter 1st Number: '))
    num2 = int(input('Enter 2nd Number: '))
smaller = min(abs(num1), abs(num2))
for i in range(1, smaller + 1):
    if (num1 % i == 0) and (num2 % i == 0):
        gcd = i
print('GCD: ', gcd)
