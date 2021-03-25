""" Design a faulty keyboard that will generate faulty output for certain values and correct output for rest of the values
Take input of operation and numbers from user and perform the calculations after that """

operator = input("enter the operation you want to perform")
num1 = input("first number ")
num2 = input("second number ")
if num1 == '45' and num2 == '3' and operator == '*':
    calc = 555
    print("result is", calc)
elif num1 == '56' and num2 == '9' and operator == '+':
    calc = 77
    print("result is", calc)
elif num1 == '56' and num2 == '6' and operator == '/':
    cal = 4
    print("result is", calc)
elif operator == '+':
    calc = int(num1) + int(num2)
    print("result is", calc)
elif operator == '*':
    calc = int(num1) * int(num2)
    print("result is", calc)
elif operator == '-':
    calc = int(num1) - int(num2)
    print("result is", calc)
elif operator == '**':
    calc = int(num1) ** int(num2)
    print("result is", calc)
else:
    print("operator invalid")
