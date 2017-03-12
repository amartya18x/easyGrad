from particles.dataTypes import Integer
from collisions.function import GradGraph


def test1():
    x = Integer("Int1")
    y = Integer("Int2")
    t = x + y
    z = Integer("Int3")
    s = t + z
    graph = GradGraph(s)
    output = graph.getOutput({x: 1, y: 2, z: 3})
    print output
if __name__ == '__main__':
    test1()
