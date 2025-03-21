def digit_counter(number):
    count = 0
    for item in number:
        count+=1
    return count

user1 = input("enter a number and i'll tell you the number of digits it have:")

print(f"{user1} has {digit_counter(user1)} digits.")