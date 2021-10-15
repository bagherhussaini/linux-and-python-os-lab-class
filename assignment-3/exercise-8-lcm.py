num1 = int(input('Enter 1st Number: '))
num2 = int(input('Enter 2nd Number: '))
lcm = 0
while num1 == 0 or num2 == 0:
    print('Don\'t Enter Zero :|')
    num1 = int(input('Enter 1st Number: '))
    num2 = int(input('Enter 2nd Number: '))
greater = max(abs(num1), abs(num2))
for i in range(1, abs(num1) * abs(num2) + 1):
    if (greater % num1 == 0) and (greater % num2 == 0):
        lcm = greater
print('LCM: ', lcm)
