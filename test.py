from particles.dataTypes import Integer, Double, DoubleTensor
from collisions.function import GradGraph
from particles import ops
import numpy as np


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

# Tensor Test

def TensorSum():
    x = DoubleTensor("Tensor1")
    y = x + 3
    graph = GradGraph(y)
    output = graph.getOutput({x: 1})
    assert(output == 4)


def TensorOp():
    x = DoubleTensor("Tensor1")
    y = x - [3, 4]
    z = y * x
    graph = GradGraph(z)
    output = graph.getOutput({x: 10})
    assert(np.all(output == 10 * (10 - np.asarray([3, 4]))))
    graph.getGradients(wrt=x)
    assert(np.all(x.gradient == 2 * 10 - np.asarray([3, 4])))

def dotProduct():
    x = DoubleTensor("Tensor1")
    y = x.dot([3, 4])
    z = y.dot([4, 5])
    graph = GradGraph(z)
    output = graph.getOutput({x: [3, 4]})
    graph.getGradients(wrt=x)
    #graph.getGradients(wrt=y)
    print(output)
    #print(y.gradient)
    #print(x.gradient)
    
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
    e = (a + b) * (b + 1)
    graph = GradGraph(e)
    graph.getOutput({a: 2,
                     b: 1})
    graph.getGradients(wrt=b)
    assert(b.gradient == 5), "Gradient : " + str(b.gradient)


def gradTestShort():
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
    assert(z.gradient == 360 ), "Gradient : "+str(z.gradient)


def gradTestLong():
    x = Integer("Int1x")
    y = Integer("Int2y")
    z = Integer("Int3z")
    p = Integer("Int4p")
    k = p * z
    n = (k + (y * p * z)) * z
    graph = GradGraph(n)
    graph.getOutput({x: 9,
                     y: 9,
                     z: 9,
                     p: 2})
    graph.getGradients(wrt=z)
    assert(z.gradient == 360), "Gradient : "+str(z.gradient)


def testOps():
    x = Integer('x')
    y = ops.log(x)
    z = ops.exp(y)
    graph = GradGraph(z)
    graph.getOutput({x: 1})
    graph.getGradients(wrt=x)
    assert(x.gradient == 1), "Gradient :" + str(x.gradient)


def activ_fns():
    x = Double('x')
    z = ops.sigmoid(x)
    graph = GradGraph(z)
    graph.getOutput({x: 110.5})
    graph.getGradients(wrt=x)
    assert(x.gradient == 0), "Gradient : "+x.gradient


if __name__ == '__main__':
    simpSum()
    simpSub()
    simpMul()
    simpDiv()
    test1()
    divtest()
    gradTestShort()
    gradTestLong()
    gradTestSimple()
    testOps()
    activ_fns()
    TensorSum()
    TensorOp()
    dotProduct()
