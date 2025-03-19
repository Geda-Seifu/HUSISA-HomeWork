def multiplication_table_maker(number):
    for item in range(1,number+1):
        for num in range(1,11):
            print(f"{item}*{num} = {item*num}")

multiplication_table_maker(5)