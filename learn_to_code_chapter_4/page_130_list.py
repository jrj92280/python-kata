eighties = ['', 'duran duran', 'B-52s', 'muse']
newwave = ['flock of seagulls', 'postal service']

remember = eighties[1]

eighties[1] = 'culture club'

band = newwave[0]

eighties[3] = band

eighties[0] = eighties[2]

eighties[2] = remember

print(eighties)

length = len(eighties)
print(length)
last = eighties[length - 1]
print(last)
second_last = eighties[length - 2]
print(second_last)
third_last = eighties[length - 3]
print((third_last))
