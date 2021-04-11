locations = ['sao paualo', 'rio de janeiro', 'lisboa', 'madrid']

print('\nordem original:')
print(locations)

print('\nalfabetica:')
print(sorted(locations))

print('\nordem original:')
print(locations)

print('\nreversa alfabetica:')
print(sorted(locations, reverse=True))

print('\nordem original:')
print(locations)

print('\nreversa:')
locations.reverse()
print(locations)

print('\nordem original:')
locations.reverse()
print(locations)

print('\nalfabetica')
locations.sort()
print(locations)

print('\nalfabetica reversa')
locations.sort(reverse=True)
print(locations)