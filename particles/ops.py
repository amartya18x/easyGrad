from dataTypes import Double
import dynamics as dy

def create_node(inp_fn, x):
    node = Double(inp_fn.name, inp_fn)
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
