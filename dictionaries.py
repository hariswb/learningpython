#dictioanry is a set of key; value pairs
kamus = {'a':1, 'b':2, 'c':3}
print(kamus)
print(kamus['b'])
del kamus['b']
print(kamus)
print('a' in kamus)
print('b' in kamus)
sorted(kamus)

# build dictionariy by  sequence with dict() constructor
kamusDua = dict([('e',4),('f',5),('g',6)])
print(kamusDua)

# Dict comprehensions
kamusTiga={i: i**2 for i in (7,8,9)}
print(kamusTiga)

# specify pairs using keyword arguments
kamusEmpat = dict(x=10, y=20, z=30)
print(kamusEmpat)