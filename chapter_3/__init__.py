
fruits {}
fruits['apples'] = 10
fruits
'apples : 10'
'apples'in fruits
if 'pears' not in fruits:
    fruits['pears'] = 0
fruits['pears'] += 1
fruits


if 'bananas' in fruits:
    fruits['bananas'] += 1
else:
    fruits['bananas'] = 1

fruits
{'bananas': 2,
 'pears':2,
 'apples': 10}


print (fruits)