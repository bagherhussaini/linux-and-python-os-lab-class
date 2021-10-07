s1, s2, s3 = float(input('Enter Side 1: ')), float(input('Enter Side 2: ')), float(input('Enter Side 3: '))
while s1 <= 0 or s2 <= 0 or s3 <= 0:
    print("Don't Insert Negative Numbers or Zero!")
    s1, s2, s3 = float(input('Enter Side 1: ')), float(input('Enter Side 2: ')), float(input('Enter Side 3: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Triangle is Valid')
else:
    print('Triangle is Invalid')
