from numpy import *
from sys import argv

fd = open(argv[1])
lines = fd.readlines()
lines = [line.strip().split() for line in lines]
lines = mat( map( lambda x: map(lambda y: int(y), x), lines ) )
U,s,V = linalg.svd(lines)
print('rank --> 'size(filter(lambda x: x!=0, s)))
