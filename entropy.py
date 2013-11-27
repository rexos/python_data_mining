"""
Python module that computes clusters validity
based on entropy
"""
from math import log

def class_prob( part, total ):
    """
    simple probability computation
    """
    return part / float( total )

def local_entropy( classes ):
    """
    returns entropy value for a single cluster
    """
    clust_size = sum( classes )
    num_class = len( classes )
    logs_data = map( lambda c: class_prob( c, clust_size ), classes )
    logs_data = map( lambda x: x * log( x, 2 ) if x > 0 else 0, logs_data )
    return -sum( logs_data ) * num_class

def entropy( clusters ):
    """
    returns the entropy of a dict of clusters where
    the keys could be of any type
    """
    total_len = sum( [ len(x) for x in clusters.values() ] )
    entropies = [ local_entropy( data ) /
                  total_len for data in clusters.values() ]
    return sum( entropies )

