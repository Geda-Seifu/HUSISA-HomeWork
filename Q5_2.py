items = [2, 4, 6, 8, 10]
# function to delete element from a list 
def item_deleter(number):
    n = int(number)
    for item in items:
        if item == n:
            items.remove(number)

item_deleter(8)
print(items)