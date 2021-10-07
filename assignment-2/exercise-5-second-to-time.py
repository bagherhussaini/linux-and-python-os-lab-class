seconds = int(input('Enter Second(s): '))
while seconds < 0:
    print('Negative Seconds Entered :|')
    seconds = int(input('Enter Second(s): '))
second = seconds % (24 * 3600)
hour = second // 3600
second %= 3600
minute = second // 60
second %= 60
print(seconds, ' Second(s) Equals to: ', "%02d:%02d:%02d" % (hour, minute, second))
