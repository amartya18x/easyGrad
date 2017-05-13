from particles.dataTypes import Integer
from collisions.function import GradGraph
from particles import ops

def simpDiv():
    x = Integer("Int1")
    y = x * ( x  +  8)
    graph = GradGraph(y)
    output = graph.getOutput({x: 8})
    print output
    #assert(output == 32)
    gradient = ops.makeGrad(x)
    print gradient
    gG = GradGraph(gradient)
    print gG.getOutput({x:8})
    #print gradient.getOutput({x: 8})


if __name__ == '__main__':
    simpDiv()
