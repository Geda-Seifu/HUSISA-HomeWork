Data = {
    'kidus' : 22,
    'musab' : 23,
    'AJ' : 22
}

Data['robel'] = 23

print(Data)

Data['robel'] = 22
print(f'the age of robel is updated to : {Data['robel']}')

del Data['AJ']

print(f"after deletion : {Data}")

