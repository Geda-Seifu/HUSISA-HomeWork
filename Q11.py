def reverser(text):
    reversed = ''
    for item in text:
        reversed = item + reversed
        

    print(reversed)

reverser('Abcd')