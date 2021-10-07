import math
print("What Operation You Want to Choose?\n1.Add\n2.Subtract\n3.Multiply\n4.Divide"
      "\n5.Log (optional base)\n6.Log (base 10)\n7.Sin\n8.Cos\n9.Tan\n10.Cot\n")
while True:
    op_choice = int(input("Enter Your Choice (1 to 10): "))
    if op_choice in range(1, 6):
        num1, num2 = float(input("Enter First Number: ")), float(input("Enter Second Number: "))
        if op_choice == 1:
            print(num1, " + ", num2, " = ", num1 + num2)

        elif op_choice == 2:
            print(num1, " - ", num2, " = ", num1 - num2)

        elif op_choice == 3:
            print(num1, " * ", num2, " = ", num1 * num2)

        elif op_choice == 4:
            if num2 == 0:
                print('Can\'t Divide by Zero!')
            else:
                print(num1, " / ", num2, " = ", num1 / num2)

        elif op_choice == 5:
            if num1 <= 0 or num2 <= 0 or num2 == 1:
                print(
                    'Domain Error! Don\'t Enter 0 or Negative for Logarithm. Also Don\'t Enter 1 for Base.')
            else:
                print('Log (', num1, ', ', num2, ')', ' = ', math.log(num1, num2))

        next_cal = int(input('Enter 1 to Continue or 0 to Exit: '))
        if next_cal == 0:
            break

    elif op_choice in range(6, 11):
        num = float(input("Enter Number: "))
        if op_choice == 6:
            if num <= 0:
                print('Domain Error! Don\'t Enter 0 or Negative for Logarithm.')
            else:
                print('Log (', num, ') = ', math.log(num))

        elif op_choice == 7:
            print('Sin (', num, ') = ', math.sin(math.radians(num)))

        elif op_choice == 8:
            print('Cos (', num, ') = ', math.cos(math.radians(num)))

        elif op_choice == 9:
            print('Tan (', num, ') = ', math.tan(math.radians(num)))

        elif op_choice == 10:
            if math.tan(math.radians(num)) == 0:
                print('Undefined!')
            else:
                print('Cot (', num, ') = ', 1/math.tan(math.radians(num)))

        next_cal = int(input('Enter 1 to Continue or 0 to Exit: '))
        if next_cal == 0:
            break

    else:
        print("Please Enter Your Choice Correctly")
