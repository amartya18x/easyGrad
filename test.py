from particles.dataTypes import Integer
from collisions.function import GradGraph


def divtest():
    x = Integer("Int1")
    y = Integer("Int2")
    z = x / y
    graph = GradGraph(z)
    output = graph.getOutput({x: 6,
                              y: 2})
    assert(output == 3)


def simpSum():
    x = Integer("Int1")
    y = x + 3
    graph = GradGraph(y)
    output = graph.getOutput({x: 1})
    assert(output == 4)


def simpSub():
    x = Integer("Int1")
    y = x - 3
    graph = GradGraph(y)
    output = graph.getOutput({x: 1})
    assert(output == -2)


def simpMul():
    x = Integer("Int1")
    y = x * 3
    graph = GradGraph(y)
    output = graph.getOutput({x: 2})
    assert(output == 6)


def simpDiv():
    x = Integer("Int1")
    y = x / 4
    graph = GradGraph(y)
    output = graph.getOutput({x: 8})
    assert(output == 2)


def test1():
    x = Integer("Int1")
    y = Integer("Int2")
    z = Integer("Int3")
    p = Integer("Int4")
    k = p + z
    kd = k * 2
    t = x - kd
    td = t - 2
    s = td * z
    sd = s / 5
    graph = GradGraph(sd)
    output = graph.getOutput({x: 36,
                              y: 2,
                              z: 3,
                              p: 9})
    assert (output == 6), "Output : " + str(output)


def gradTestSimple():
    a = Integer("a")
    b = Integer("b")
    c = a + b
    d = b + 6
    e = c * d
    graph = GradGraph(e)
    graph.getOutput({a: 32,
                     b: 11})
    graph.getGradients(wrt=b)
    print a.gradient, b.gradient


def gradTest():
    x = Integer("Int1x")
    y = Integer("Int2y")
    z = Integer("Int3z")
    p = Integer("Int4p")
    k = p * z
    t = y * k
    m = k + t
    n = m * z
    graph = GradGraph(n)
    graph.getOutput({x: 9,
                     y: 9,
                     z: 9,
                     p: 2})
    graph.getGradients(wrt=z)
    print x.gradient, y.gradient, z.gradient, p.gradient

if __name__ == '__main__':
    simpSum()
    simpSub()
    simpMul()
    simpDiv()
    test1()
    divtest()
    gradTest()
    gradTestSimple()
