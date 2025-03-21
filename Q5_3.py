items = [2, 4, 6, 8, 10]

# without using built in function 
def min_max_finder():
    min = 5
    max = 5
    for item in items:
        if item > max :
            max = item
        if item < min :
            min = item

    print(f"the maximum value is : {max}")
    print(f"the minimum value is : {min}")

min_max_finder()
    
# by using built in function 
def min_max_finder():
    print(f"the maximum value is : {max(items)}")
    print(f"the minimum value is : {min(items)}")

min_max_finder()