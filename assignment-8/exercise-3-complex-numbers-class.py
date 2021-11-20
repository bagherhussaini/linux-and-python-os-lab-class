class ComplexNumbers:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return str(self.real) + ' + (' + str(self.imag) + ') i'

    # def print_complex_numbers(self):
    #     print(self.real, ' + (', self.imag, ') i')

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumbers(real, imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumbers(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumbers(real, imag)


def show_menu():
    print('┌─────────────────────────────────────────────────┐')
    print('│         Choose Operation for Complex Numbers    │')
    print('│         1.Add                                   │')
    print('│         2.Multiplication                        │')
    print('│         3.Subtract                              │')
    print('│         4.Exit                                  │')
    print('└─────────────────────────────────────────────────┘')


def user_input():
    a = int(input('Enter Real Part: '))
    b = int(input('Enter Imaginary Part: '))
    return a, b


def main():
    print('Enter for First Complex Number: ')
    real1, imag1 = user_input()
    print('Enter for Second Complex Number: ')
    real2, imag2 = user_input()
    complex_number1 = ComplexNumbers(real1, imag1)
    complex_number2 = ComplexNumbers(real2, imag2)
    while True:
        show_menu()
        choice = int(input('Please Take a Choice: '))
        if choice == 1:
            print('Result: ', complex_number1 + complex_number2)
        elif choice == 2:
            print('Result: ', complex_number1 * complex_number2)
        elif choice == 3:
            print('Result: ', complex_number1 - complex_number2)
        elif choice == 4:
            exit()
        else:
            print('Choose Correctly!')


if __name__ == '__main__':
    main()
