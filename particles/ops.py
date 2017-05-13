import dataTypes as dt
import dynamics as dy


def create_node(inp_fn, x):
    node = dt.Double(inp_fn.name, inp_fn)
    x.children.append(node)
    return node


def exp(x):
    inp_fn = dy.ExpNode(x)
    return create_node(inp_fn, x)


def log(x):
    inp_fn = dy.LogNode(x)
    return create_node(inp_fn, x)


def sigmoid(x):
    inp_fn = dy.SigmNode(x)
    return create_node(inp_fn, x)


def tanh(x):
    inp_fn = dy.TanhNode(x)
    return create_node(inp_fn, x)


def makeGrad(currNode):
    for idx, nodes in enumerate(currNode.children):
        print nodes
        if not nodes.grad_make:
            makeGrad(nodes)
            print vars(nodes)
            print "==================="
            nodes.grad_make = True
        if currNode.gradient_node is None:
            currNode.gradient_node = nodes.parent.gradient_nodes[currNode]
        else:
            if nodes.gradient_node is None:
                currNode.gradient_node =\
                    nodes.parent.gradient_nodes[currNode] +\
                    currNode.gradient_node
            else:
                currNode.gradient_node = (currNode.gradient_node +
                                          nodes.parent.gradient_nodes[
                                              currNode]) *\
                    nodes.gradient_node

    return currNode.gradient_node
