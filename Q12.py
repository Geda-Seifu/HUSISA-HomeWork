def fibonacci_generator(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=' ')
        temp = b
        b = a + b
        a = temp

user1 = int(input("enter an number to get its fibonacci series: "))

fibonacci_generator(user1)