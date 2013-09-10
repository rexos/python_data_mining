from sys import argv

def perform_operation(a):
    return map(lambda y: map(lambda x: x*2, y), a)

data = []

with open( argv[1], 'r' ) as f:
    for line in f:
        line = line.split(' ')
        data.extend([[int(x) for x in line]])

print( perform_operation(data) )
