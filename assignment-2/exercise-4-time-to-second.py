hour, minute, second = int(input('Enter the Hour: ')), int(input('Enter the Minute: ')), int(input('Enter the Second: '))
while hour < 0 or minute < 0 or second < 0 or minute >= 60 or second >= 60:
    print('Enter Positive Numbers for Time and also Smaller than 60 for Minute and Second!')
    hour, minute, second = int(input('Enter the Hour: ')), int(input('Enter the Minute: ')), int(
        input('Enter the Second: '))
minutes = hour * 60 + minute
seconds = minutes * 60 + second
print('The Time You Entered Equals to: ', seconds, ' Second(s)')