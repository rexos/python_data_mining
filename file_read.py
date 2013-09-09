from sys import argv

def perform_operation(a):
    return map(lambda y: map(lambda x: x*2, y), a)

data = []

fd = open( argv[1], 'r' )
for line in fd:
    line = line.split(' ')
    data.extend([[int(x) for x in line]])
fd.close()

print( perform_operation(data) )
