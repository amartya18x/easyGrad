from particles.dataTypes import Integer
from collisions.function import GradGraph


def divtest():
    x = Integer("Int1")
    y = Integer("Int2")
    z = x / y
    graph = GradGraph(z)
    output = graph.getOutput({x: 6,
                              y: 2})
    print output
    return output == 3


def test1():
    x = Integer("Int1")
    y = Integer("Int2")
    z = Integer("Int3")
    p = Integer("Int4")
    k = p + z
    t = x - k
    s = t * z
    graph = GradGraph(s)
    output = graph.getOutput({x: 6,
                              y: 2,
                              z: 3,
                              p: 9})
    print output

if __name__ == '__main__':
    test1()
    divtest()
