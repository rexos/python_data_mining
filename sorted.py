class MyDict:
    def __init__(self, d = {}):
        self.dict = d

    def keys(self):
        """
        >>> a = MyDict({'a': 1, 'b': 2, 'c': 3})
        >>> a.keys()
        ['a', 'b', 'c']
        """
        return self.dict.keys().sort()

    def values(self):
        return self.dict.values()


def main():
    d = MyDict({'a' : 1, 'b' : 2, 'c' : 3})
    d.keys()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
