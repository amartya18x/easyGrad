from particles.dataTypes import Integer, Double, DoubleTensor
from collisions.function import GradGraph
from particles import ops
import numpy as np
import unittest


def divtest():
    x = Integer("Int1")
    y = Integer("Int2")
    z = x / y
    graph = GradGraph(z)
    output = graph.getOutput({x: 6,
                              y: 2})
    return output == 3


def simpSum():
    x = Integer("Int1")
    y = x + 3
    graph = GradGraph(y)
    output = graph.getOutput({x: 1})
    return output == 4


def simpSub():
    x = Integer("Int1")
    y = x - 3
    graph = GradGraph(y)
    output = graph.getOutput({x: 1})
    return output == -2


def simpMul():
    x = Integer("Int1")
    y = x * 3
    graph = GradGraph(y)
    output = graph.getOutput({x: 2})
    return output == 6


def simpDiv():
    x = Integer("Int1")
    y = x / 4
    graph = GradGraph(y)
    output = graph.getOutput({x: 8})
    return output == 2

# Tensor Test


def TensorSum():
    x = DoubleTensor("Tensor1")
    y = x + 3
    graph = GradGraph(y)
    output = graph.getOutput({x: 1})
    return output == 4


def TensorOp():
    x = DoubleTensor("Tensor1")
    y = x - [3, 4]
    z = ops.log(y * x)
    graph = GradGraph(z)
    output = graph.getOutput({x: [10]})
    assert(np.all(np.isclose(output, np.log(10 * (10 - np.asarray([3, 4]))))))
    graph.getGradients(wrt=x)
    a = 2 * 10 - np.asarray([3, 4])
    b = 1.0 / np.exp(np.asarray(output))
    return np.all(np.isclose(x.gradient, a * b))


def dotProduct():
    x = DoubleTensor("Tensor1")
    y = x.dot([3, 4])
    z = y.dot([4, 5])
    graph = GradGraph(z)
    output = graph.getOutput({x: [3, 4]})
    graph.getGradients(wrt=x)
    flag1 = np.all(output == [100, 125])
    flag2 = np.all(x.gradient == [[12., 16.], [15., 20.]])
    return flag1 and flag2


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
    return output == 6


def gradTestSimple():
    a = Integer("a")
    b = Integer("b")
    e = (a + b) * (b + 1)
    graph = GradGraph(e)
    graph.getOutput({a: 2,
                     b: 1})
    graph.getGradients(wrt=b)
    return b.gradient == 5


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
    return z.gradient == 360


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
    return True


def testOps():
    x = Integer('x')
    y = ops.log(x)
    z = ops.exp(y)
    graph = GradGraph(z)
    graph.getOutput({x: 1})
    graph.getGradients(wrt=x)
    return x.gradient == 1


def activ_fns():
    x = Double('x')
    z = ops.sigmoid(x)
    graph = GradGraph(z)
    graph.getOutput({x: 110.5})
    graph.getGradients(wrt=x)
    return x.gradient == 0


class TestCase(unittest.TestCase):

    def test_simp_sum(self):
        """ Simple Summation Test"""
        self.assertTrue(simpSum())

    def test_simp_sub(self):
        """ Simple Subtraction Test"""
        self.assertTrue(simpSub())

    def test_simp_mul(self):
        """ Simple Multiplication Test"""
        self.assertTrue(simpMul())

    def test_simp_div(self):
        """ Simple Division Test"""
        self.assertTrue(simpDiv())

    def test_test1(self):
        """ Miscellaneous Test"""
        self.assertTrue(test1())

    def test_div(self):
        """ Division Test"""
        self.assertTrue(divtest())

    def test_short_grad(self):
        """ Short Grad Test"""
        self.assertTrue(gradTestShort())

    def test_long_grad(self):
        """ Long Gradient Test"""
        self.assertTrue(gradTestLong())

    def test_simp_grad(self):
        """ Simple gradient test"""
        self.assertTrue(gradTestSimple())

    def test_ops(self):
        """ Test Ops"""
        self.assertTrue(testOps())

    def test_activ_fn(self):
        """ Activation Function test"""
        self.assertTrue(activ_fns())

    def test_tensor_sum(self):
        """ Tensor Sum test"""
        self.assertTrue(TensorSum())

    def test_tensor_op(self):
        """ Tensor operations test"""
        self.assertTrue(TensorOp())

    def test_dot_prod(self):
        """ Dot Product"""
        self.assertTrue(dotProduct())


def run_test():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    run_test()
