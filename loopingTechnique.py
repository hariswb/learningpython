# looping through dict
prajurit = dict(arjuna='zzz', bima='yyy', gundala='ddd')
print(prajurit)

for key, value in prajurit.items():
    print(key, value)

# loop over two sequences at the same time
tanya=['nama','tugas','warna rambut']
jawab=['bambang', 'bawa air', 'hijau']

for i, j in zip(tanya,jawab):
    print('{0}?\t{1}'.format(i,j))

# changing a list while looping by creating new list

import math
raw_data = [1.3, float('NaN'), 55.4, 123.2, float('NaN'), 44.0]
filteredData = []
for value in raw_data:
    if not math.isnan(value):
        filteredData.append(value)

print(filteredData)