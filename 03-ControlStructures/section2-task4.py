number1 = float(input("Enter number:"))
number2 = float(input("Enter number:"))
operator = input('Enter operator(*, +, -, /): ')
result = 0

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
else:
    raise(ValueError("Wrong operator!!"))

print(f'{number1} {operator} {number2} = {result}')