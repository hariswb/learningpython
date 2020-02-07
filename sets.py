# empty set is set()
# defining set is with {}

keranjang={'pisang', 'palu', 'gergaji'}
print(keranjang)
print('pisang' in keranjang)

print('\n')

#mathematical operation on sets

x=set('asdfg')
y=set('asdqwe')
print(x, y)
print(x-y, y-x)

# | is in x or y or both 
print(x|y, len(x),'\t', y|x, len(y))

# & is in both 
print(x&y)

# ^ is in both x or b but not both 
print(x^y)

#set comprehension
z = {i for i in 'abracadabra' if i not in 'asdqwe'}
print(z)