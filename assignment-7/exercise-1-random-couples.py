from random import randint
boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
random_boys = []
random_girls = []
while len(random_boys) != (len(boys)):
    r1 = randint(0, len(boys) - 1)
    if boys[r1] not in random_boys:
        random_boys.append(boys[r1])
while len(random_girls) != len(girls):
    r2 = randint(0, len(girls) - 1)
    if girls[r2] not in random_girls:
        random_girls.append(girls[r2])
for i in range(len(boys)):
    print(random_boys[i], ' ❤️', random_girls[i])
