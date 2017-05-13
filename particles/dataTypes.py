from dynamics import AddVarNode, SubVarNode, MultVarNode, DivVarNode


class AbstractScalar(object):

    def __init__(self, name, parent=None):
        self.name = name
        self.val = None
        self.initialized = False
        self.parent = parent
        self.gradient = 0
        self.children = []
        self.grad_calc = False
        self.grad_make = False
        self.gradient_node = None

    def __add__(self, s):
        pass

    def __mul__(self, s):
        pass

    def __sub__(self, s):
        pass

    def __div__(self, s):
        pass

    def __str__(self):
        if self.val is not None:
            return "{Integer : " + self.name + " = " + str(self.val) + " }"
        else:
            return "{Integer : " + self.name + " }"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)


class Integer(AbstractScalar):

    def __init__(self, name, parent=None, val=None):
        super(Integer, self).__init__(name, parent)
        if parent is not None:
            self.inpNodes = parent.inpNodes
        else:
            self.inpNodes = []
        self.val = val

    def __add__(self, t):
        if type(t) in [int]:
            t = Integer("Constant", val=t)
        inp_fn = AddVarNode(self, t)
        node = Integer(inp_fn.name, inp_fn)

        # Append children for gradient
        t.children.append(node)
        self.children.append(node)
        return node

    def __sub__(self, t):
        if type(t) in [int]:
            t = Integer("Constant", val=t)
        inp_fn = SubVarNode(self, t)
        node = Integer(inp_fn.name, inp_fn)

        # Append children for gradient
        t.children.append(node)
        self.children.append(node)
        return node

    def __mul__(self, t):
        if type(t) in [int]:
            t = Integer("Constant", val=t)
        inp_fn = MultVarNode(self, t)
        node = Integer(inp_fn.name, inp_fn)

        # Append children for gradient
        t.children.append(node)
        self.children.append(node)
        return node

    def __div__(self, t):
        if type(t) in [int]:
            t = Integer("Constant", val=t)
        inp_fn = DivVarNode(self, t)
        node = Integer(inp_fn.name, inp_fn)

        # Append children for gradient
        t.children.append(node)
        self.children.append(node)
        return node

    def forward(self):
        self.parent.forward()
        self.val = self.parent.val


class Double(AbstractScalar):

    def __init__(self, name, parent=None, val=None):
        super(Double, self).__init__(name, parent)
        if parent is not None:
            self.inpNodes = parent.inpNodes
        else:
            self.inpNodes = []
        self.val = val

    def __add__(self, t):
        if type(t) in [int]:
            t = Double("Constant", val=t)
        inp_fn = AddVarNode(self, t)
        node = Double(inp_fn.name, inp_fn)

        # Append children for gradient
        t.children.append(node)
        self.children.append(node)
        return node

    def __sub__(self, t):
        if type(t) in [float]:
            t = Double("Constant", val=t)
        inp_fn = SubVarNode(self, t)
        node = Double(inp_fn.name, inp_fn)

        # Append children for gradient
        t.children.append(node)
        self.children.append(node)
        return node

    def __mul__(self, t):
        if type(t) in [float]:
            t = Double("Constant", val=t)
        inp_fn = MultVarNode(self, t)
        node = Double(inp_fn.name, inp_fn)

        # Append children for gradient
        t.children.append(node)
        self.children.append(node)
        return node

    def __div__(self, t):
        if type(t) in [float]:
            t = Double("Constant", val=t)
        inp_fn = DivVarNode(self, t)
        node = Double(inp_fn.name, inp_fn)

        # Append children for gradient
        t.children.append(node)
        self.children.append(node)
        return node

    def forward(self):
        self.parent.forward()
        self.val = self.parent.val
