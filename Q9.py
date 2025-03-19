def factorial_maker(n):
    product = 1
    for item in range(1,n+1):
        product*=item

    return product

number = int(input("enter a number to get its factorial: "))

print(f"the factorial of {number} is {factorial_maker(number)}")