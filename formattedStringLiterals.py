import math
print(f'Value of pi is approx {math.pi:.4f}.')

###

table = {'Sjoerd': 4125, 'Jack': 4121, 'budi': 5120}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

###

animals = 'belut'
print(f'My perahu penuh with {animals}')
print(f'My sampan full dengan {animals!r}')