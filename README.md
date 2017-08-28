[![Build Status](https://travis-ci.org/amartya18x/easyGrad.svg?branch=master)](https://travis-ci.org/amartya18x/easyGrad)
# Easy Grad
__EasyGrad__ is now available via pip and it is the easiest way to use it. To install __easyGrad__ via pip

```bash
   pip install easyGrad
```

To install it from source, clone this repository and run

```bash
   python setup.py install
```
This library aims to provide an easy implementation of doing symbolic operations in python
## Operators allowed

- *exp(x)* and *log(x)*
```Python
def testOps():
    x = Integer('x')
    y = ops.log(x)
    z = ops.exp(y)
    graph = GradGraph(z)
    graph.getOutput({x: 1})
    graph.getGradients(wrt=x)
    print x.gradient
```
- *Sigmoid(x)*
```Python

def activ_fns():
    x = Double('x')
    z = ops.sigmoid(x)
    graph = GradGraph(z)
    graph.getOutput({x: 110.5})
    graph.getGradients(wrt=x)
    print x.gradient
```
- *Tanh(x)*
```Python

def activ_fns():
    x = Double('x')
    z = ops.tanh(x)
    graph = GradGraph(z)
    graph.getOutput({x: 110.5})
    graph.getGradients(wrt=x)
    print x.gradient
```

## Testing

```Python
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
```
### Here is a more complex example.
```Python
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
```
### This is the same examples as above but the commands are not three op commands.

```Python
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
    print x.gradient, y.gradient, z.gradient, p.gradient
```
Tensor Operations
```Python

def dotProduct():
    x = DoubleTensor("Tensor1")
    y = x.dot([3, 4])
    z = y.dot([4, 5])
    graph = GradGraph(z)
    output = graph.getOutput({x: [3, 4]})
    graph.getGradients(wrt=x)
    assert(np.all(output == [100, 125]))
    assert(np.all(x.gradient == [[ 12., 16.], [ 15., 20.]]))
	


def TensorOp():
    x = DoubleTensor("Tensor1")
    y = x - [3, 4]
    z = ops.log(y * x)
    graph = GradGraph(z)
    output = graph.getOutput({x: [10]})
    assert(np.all(np.isclose(output, np.log(10 * (10 - np.asarray([3, 4]))))))
    graph.getGradients(wrt=x)
    a = 2 * 10 - np.asarray([3, 4])
    b = 1.0/np.exp(np.asarray(output))
    assert(np.all(np.isclose(x.gradient, a * b)))


```

