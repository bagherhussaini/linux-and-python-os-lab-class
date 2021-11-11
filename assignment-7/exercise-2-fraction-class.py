class Fraction:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError('The numerator must be an integer!')
        if not isinstance(denominator, int):
            raise TypeError('The denominator must be an integer!')
        if denominator == 0:
            raise ZeroDivisionError('The Denominator can\'t be zero.')
        if numerator == 0:
            self.num = 0
            self.den = 1
        else:
            self.num = numerator
            self.den = denominator

    def get_numerator(self):
        return self.num

    def get_denominator(self):
        return self.den

    def __repr__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        num = self.get_numerator() * other.get_denominator() + other.get_numerator() * self.get_denominator()
        den = self.get_denominator() * other.get_denominator()
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.get_numerator() * other.get_denominator() - other.get_numerator() * self.get_denominator()
        den = self.get_denominator() * other.get_denominator()
        return Fraction(num, den)

    def __mul__(self, other):
        if self.num == 0 or other.num == 0:
            return 0
        else:
            num = self.get_numerator() * other.get_numerator()
            den = self.get_denominator() * other.get_denominator()
            return Fraction(num, den)

    def __truediv__(self, other):
        if self.num == 0:
            return 0
        else:
            num = self.get_numerator() * other.get_denominator()
            den = self.get_denominator() * other.get_numerator()
            return Fraction(num, den)


def show_menu():
    print('┌─────────────────────────────────────────────────┐')
    print('│         Choose Operation for Fractions          │')
    print('│         1.Add                                   │')
    print('│         2.Subtract                              │')
    print('│         3.Multiplication                        │')
    print('│         4.Division                              │')
    print('│         5.Exit                                  │')
    print('└─────────────────────────────────────────────────┘')


def user_input():
    a = int(input('Enter Numerator: '))
    b = int(input('Enter Denominator: '))
    return a, b


def main():
    print('Enter for First Fraction: ')
    num1, den1 = user_input()
    print('Enter for Second Fraction: ')
    num2, den2 = user_input()
    fraction1 = Fraction(num1, den1)
    fraction2 = Fraction(num2, den2)
    while True:
        show_menu()
        choice = int(input('Please Take a Choice: '))
        if choice == 1:
            print('Result: ', fraction1 + fraction2)
        elif choice == 2:
            print('Result: ', fraction1 - fraction2)
        elif choice == 3:
            print('Result: ', fraction1 * fraction2)
        elif choice == 4:
            print('Result: ', fraction1 / fraction2)
        elif choice == 5:
            exit()
        else:
            print('Choose Correctly!')


if __name__ == '__main__':
    main()
