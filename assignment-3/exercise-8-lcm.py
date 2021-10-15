num1 = int(input('Enter 1st Number: '))
num2 = int(input('Enter 2nd Number: '))
lcm = 0
while num1 == 0 or num2 == 0:
    print('Don\'t Enter Zero :|')
    num1 = int(input('Enter 1st Number: '))
    num2 = int(input('Enter 2nd Number: '))
greater = max(abs(num1), abs(num2))
for i in range(greater, abs(num1) * abs(num2) + 1):
    if (i % num1 == 0) and (i % num2 == 0):
        lcm = i
        break
print('LCM: ', lcm)
