fruits = {}
fruits['apples'] = 10
print(fruits)
print('apples' in fruits)
if 'bananas' in fruits:
    fruits['bananas'] += 1
else:
    fruits['bananas'] = 1
print(fruits)

fruits['bananas'] = fruits['bananas'] + 1
fruits['bananas'] += 1

print(fruits)

if 'pears' not in fruits:
    fruits['pears'] = 0

print(fruits)
fruits['pears'] += 1
print(fruits)

fruits.setdefault('pears', 0)
fruits['pears'] += 1
print (fruits)