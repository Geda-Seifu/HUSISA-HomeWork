a = int(input('enter the first number: '))
b = int(input('enter the second number: '))

n = input('enter the operation(+,-,*,/): ')

if n == '+':
    print(f"The result is: {a + b}")
elif n == '-':
    print(f"The result is: {a - b}")
elif n == '*':
    print(f"The result is: {a * b}")
elif n == '/':
    print(f"The result is: {a / b}")