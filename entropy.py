"""
Python module that computes clusters validity
based on entropy
"""
from math import log

def class_prob( part, total ):
    return part / float( total )

def local_entropy( classes ):
    clust_size = sum( classes )
    num_class = len( classes )
    res = float()
    logs_data = map( lambda c: class_prob( c, clust_size), classes )
    logs_data = map( lambda x: x * log( x, 2 ), logs_data )
    return -sum( logs_data ) * num_class

def entropy( clusters ):
    total_len = sum( [ len(x) for x in clusters.values() ] )
    total = float()
    for data in clusters.values():
        total = total + local_entropy( data ) / total_len
    print( total )
