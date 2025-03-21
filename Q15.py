list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = []

for m in list1:
    for n in list2:
        if m==n:
            list3.append(m)

print(f"the common elements are: {list3}")
