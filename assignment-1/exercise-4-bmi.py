w, h = float(input('Enter the Weight(kg): ')), float(input('Enter the Height(m): '))
bmi = w/(h*h)
if 0 < bmi < 18.5:
    print('BMI: ', bmi, 'Result: Underweight.')
elif 18.5 <= bmi <= 24.9:
    print('BMI: ', bmi, 'Result: Normal.')
elif 25 <= bmi <= 29.9:
    print('BMI: ', bmi, 'Result: Overweight.')
elif 30 <= bmi <= 34.9:
    print('BMI: ', bmi, 'Result: Obese.')
elif bmi >= 35:
    print('BMI: ', bmi, 'Result: Extremely Obese.')
else:
    print('Enter Data Correctly')
