from random import randint
boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
size, random_boys, random_girls = len(boys), [], []
while len(random_boys) != size or len(random_girls) != size:
    random_boy = randint(0, size - 1)
    if boys[random_boy] not in random_boys:
        random_boys.append(boys[random_boy])
    random_girl = randint(0, size - 1)
    if girls[random_girl] not in random_girls:
        random_girls.append(girls[random_girl])
for i in range(size):
    print('(', random_boys[i], ',',  random_girls[i], ')', end='')
