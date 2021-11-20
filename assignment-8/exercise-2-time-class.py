class Time:
    def __init__(self, hour=0, minute=0, second=0):
        if hour < 0 or minute < 0 or second < 0:
            raise ValueError('Please Enter Positive Value for Time.')
        else:
            self.hour = hour
            self.minute = minute
            self.second = second

    def __repr__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    # def print_time(self):
    #     print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def __add__(self, other):
        if isinstance(other, Time):
            return self.time_increment(other)
        else:
            return self.second_increment(other)

    # def __radd__(self, other):
    #     return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Time):
            return self.time_decrement(other)
        else:
            return self.second_decrement(other)

    # def __rsub__(self, other):
    #     return self.__sub__(other)

    def second_decrement(self, seconds):
        seconds -= self.time_to_second()
        while seconds < 0:
            self.minute -= 1
            self.second += 60
        return self.second_to_time(seconds)

    def time_decrement(self, other):
        seconds = self.time_to_second() - other.time_to_second()
        return self.second_to_time(seconds)

    def second_increment(self, seconds):
        seconds += self.time_to_second()
        return self.second_to_time(seconds)

    def time_increment(self, other):
        seconds = self.time_to_second() + other.time_to_second()
        return self.second_to_time(seconds)

    def second_to_time(self, seconds):
        minutes, self.second = divmod(seconds, 60)
        self.hour, self.minute = divmod(minutes, 60)
        return self

    def time_to_second(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds


def show_menu():
    print('┌─────────────────────────────────────────────────┐')
    print('│         Choose Operation for Times              │')
    print('│         1.Add                                   │')
    print('│         2.Subtract                              │')
    print('│         3.Second to Time                        │')
    print('│         4.Time to Second                        │')
    print('│         5.Exit                                  │')
    print('└─────────────────────────────────────────────────┘')


def user_input():
    h = int(input('Enter Hour: '))
    m = int(input('Enter Minute: '))
    s = int(input('Enter Second: '))
    return h, m, s


def main():
    while True:
        show_menu()
        choice = int(input('Please Take a Choice: '))
        if choice == 1:
            print('Enter for First Time: ')
            h1, m1, s1 = user_input()
            print('Enter for Second Time: ')
            h2, m2, s2 = user_input()
            time1 = Time(h1, m1, s1)
            time2 = Time(h2, m2, s2)
            print('Result: ', time1 + time2)
        elif choice == 2:
            print('Enter for First Time: ')
            h1, m1, s1 = user_input()
            print('Enter for Second Time: ')
            h2, m2, s2 = user_input()
            time1 = Time(h1, m1, s1)
            time2 = Time(h2, m2, s2)
            print('Result: ', time1 - time2)
        elif choice == 3:
            s = int(input('Enter Second to Convert to Time: '))
            obj = Time(second=s)
            print('Result: ', obj.second_to_time(s))
        elif choice == 4:
            print('Enter Time to Convert to Second: ')
            h, m, s = user_input()
            obj = Time(h, m, s)
            print('Result: ', obj.time_to_second())
        elif choice == 5:
            exit()
        else:
            print('Choose Correctly!')


if __name__ == '__main__':
    main()
