import numpy as np
class GradGraph(object):

    def __init__(self, output):
        self.output = output
        self.evaluated = False

    def getOutput(self, inpNodes):
        for nodes in inpNodes.keys():
            nodes.val = inpNodes[nodes]
        outVal = self.evalDFS(self.output, inpNodes)
        return outVal.val

    def evalDFS(self, currNode, inpNodes):
        if currNode.parent is None:
            if currNode.val is None:
                assert(currNode in inpNodes), str(
                    currNode) + " does not have an input."
            return currNode
        else:
            for nodes in currNode.inpNodes:
                if nodes.val is None:
                    self.evalDFS(nodes, inpNodes)
            currNode.forward()
            currNode.forward_done = True
        self.evaluated = True
        return currNode

    def getGradients(self, wrt):
        assert(self.evaluated), "Do the forwarded pass"
        self.output.gradient = 1
        self.calcGrad(wrt)

    def calcGrad(self, currNode):
        for idx, nodes in enumerate(currNode.children):
            if not nodes.grad_calc:
                assert(nodes.forward_done), "Forward not done with "+str(nodes)
                self.calcGrad(nodes)
                nodes.grad_calc = True
            if isinstance(nodes.parent.gradients[currNode], (list, tuple, np.ndarray)):
                if nodes.parent.gradients[currNode].size == 1 or nodes.parent.no_outer:
                    currNode.gradient = currNode.gradient + nodes.gradient * nodes.parent.gradients[currNode]
                else:
                    currNode.gradient = currNode.gradient + np.outer(nodes.gradient, nodes.parent.gradients[currNode])
            else:
                currNode.gradient = currNode.gradient + nodes.gradient *\
                                    nodes.parent.gradients[currNode]
                
