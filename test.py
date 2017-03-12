from particles.dataTypes import Integer

def test1():
    x = Integer("Int1")
    y = Integer("Int2")
    t = x + y
    z = Integer("Int3")
    print t

if __name__ == '__main__':
    test1()
