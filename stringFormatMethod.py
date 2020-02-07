print('we adalah {} yang ngomong "{}!"'.format('knights', 'ni'))

###

daftar = ['spoon', 'forrk']
print('{0} and {1}'.format(daftar[:], 'eggs'))
print('{1} and {0}'.format('eggs',daftar[0]))

###

print('this {food} is {adjective}'.format(
    food='spam', adjective='absolutely horrible'
))

###

print('cerita dari {1}, {0}, dan {lainnya}'.format('boll', 'bull', lainnya='gogon'))

###

table = {'a': 221, 'b':435, 'c': 113}
print('{0[a]:d}, {0[b]:d}, {0[c]:d}'.format(table))

###

print('{a:d}, {b:d}, {c:d}'.format(**table))

###
#Manual string formatting
###

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:d}'.format(x, x*x, x*x*x))

###


