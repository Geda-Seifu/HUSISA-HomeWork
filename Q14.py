def prime_checker(number):
    if number <= 1:
        return False
    for item in range(2,number):
        if number%item==0:
            return False
    return True
        
userin= int(input("enter a number: "))


if prime_checker(userin):
    print(f"{userin} is indeed a prime number!")
else:
    print("it's not a prime number.")