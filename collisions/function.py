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
        self.evaluated = True
        return currNode

    def getGradients(self, wrt):
        assert(self.evaluated), "Do the forwarded pass"
        self.output.gradient = 1
        self.calcGrad(wrt)

    def calcGrad(self, currNode):
        for idx, nodes in enumerate(currNode.children):
            if not nodes.grad_calc:
                self.calcGrad(nodes)
                nodes.grad_calc = True
            currNode.gradient += nodes.gradient *\
                nodes.parent.gradients[currNode]
