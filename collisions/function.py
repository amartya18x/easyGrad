class GradGraph(object):

    def __init__(self, output):
        self.output = output

    def getOutput(self, inpNodes):
        for nodes in inpNodes.keys():
            nodes.val = inpNodes[nodes]
        outVal = self.evalDFS(self.output, inpNodes)
        print outVal
        return outVal.val

    def evalDFS(self, currNode, inpNodes):
        if currNode.parent is None:
            assert(currNode in inpNodes), str(
                currNode) + " does not have an input."
            return currNode
        else:
            for nodes in currNode.inpNodes:
                self.evalDFS(nodes, inpNodes)
            currNode.forward()
        return currNode
