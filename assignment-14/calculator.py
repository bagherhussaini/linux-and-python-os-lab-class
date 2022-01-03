from math import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from functools import partial


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('calculator.ui')
        self.ui.show()
        self.ui.zeroButton.clicked.connect(partial(self.func_number_x, 0))
        self.ui.oneButton.clicked.connect(partial(self.func_number_x, 1))
        self.ui.twoButton.clicked.connect(partial(self.func_number_x, 2))
        self.ui.threeButton.clicked.connect(partial(self.func_number_x, 3))
        self.ui.fourButton.clicked.connect(partial(self.func_number_x, 4))
        self.ui.fiveButton.clicked.connect(partial(self.func_number_x, 5))
        self.ui.sixButton.clicked.connect(partial(self.func_number_x, 6))
        self.ui.sevenButton.clicked.connect(partial(self.func_number_x, 7))
        self.ui.eightButton.clicked.connect(partial(self.func_number_x, 8))
        self.ui.nineButton.clicked.connect(partial(self.func_number_x, 9))
        self.ui.plusButton.clicked.connect(partial(self.input_num1, '+'))
        self.ui.minusButton.clicked.connect(partial(self.input_num1, '-'))
        self.ui.multiplyButton.clicked.connect(partial(self.input_num1, '*'))
        self.ui.divisionButton.clicked.connect(partial(self.input_num1, '/'))
        self.ui.sinButton.clicked.connect(partial(self.function_x, 'sin'))
        self.ui.cosButton.clicked.connect(partial(self.function_x, 'cos'))
        self.ui.tanButton.clicked.connect(partial(self.function_x, 'tan'))
        self.ui.cotButton.clicked.connect(partial(self.function_x, 'cot'))
        self.ui.logButton.clicked.connect(partial(self.function_x, 'log'))
        self.ui.sqrtButton.clicked.connect(partial(self.function_x, 'sqrt'))
        self.ui.equalButton.clicked.connect(self.equal)
        self.ui.cButton.clicked.connect(self.reset)
        self.ui.plusminusButton.clicked.connect(self.plusminus)
        self.ui.decimalButton.clicked.connect(self.decimal)

    def func_number_x(self, x):
        self.ui.output_label.setText(self.ui.output_label.text() + str(x))

    def input_num1(self, op):
        try:
            if self.ui.output_label.text() != '':
                self.num1 = float(self.ui.output_label.text())
                self.ui.output_label.setText('')
                self.operator = op
        except:
            self.ui.output_label.setText('Error')

    def equal(self):
        try:
            if self.ui.output_label.text() != '':
                self.num2 = float(self.ui.output_label.text())

                if self.operator == '+':
                    result = self.num1 + self.num2
                elif self.operator == '-':
                    result = self.num1 - self.num2
                elif self.operator == '*':
                    result = self.num1 * self.num2
                elif self.operator == '/':
                    result = self.num1 / self.num2

                self.ui.output_label.setText(str(result))
        except:
            self.ui.output_label.setText('Error')

    def reset(self):
        self.ui.output_label.setText('')

    def plusminus(self):
        if '-' in self.ui.output_label.text():
            negative = float(self.ui.output_label.text()) * -1
            self.ui.output_label.setText(str(negative))
        else:
            self.ui.output_label.setText('-' + self.ui.output_label.text())

    def decimal(self):
        if '.' not in self.ui.output_label.text() and self.ui.output_label.text() != '':
            self.ui.output_label.setText(self.ui.output_label.text() + '.')

    def function_x(self, sym):
        try:
            if self.ui.output_label.text() != '':
                text = radians(float(self.ui.output_label.text()))

                if sym == 'sin':
                    result = sin(text)
                elif sym == 'cos':
                    result = cos(text)
                elif sym == 'tan':
                    result = tan(text)
                elif sym == 'cot':
                    result = cos(text) / sin(text)
                elif sym == 'log':
                    result = log(float(self.ui.output_label.text()))
                elif sym == 'sqrt':
                    result = sqrt(float(self.ui.output_label.text()))

                result = round(result, 6)
                self.ui.output_label.setText(str(result))
        except:
            self.ui.output_label.setText('Error')


if __name__ == '__main__':
    app = QApplication()
    window = Calculator()
    app.exec()
