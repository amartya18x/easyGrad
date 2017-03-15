[![Build Status](https://travis-ci.org/amartya18x/easyGrad.svg?branch=master)](https://travis-ci.org/amartya18x/easyGrad)
# Easy Grad

This library aims to provide an easy implementation of doing symbolic operations in python

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
