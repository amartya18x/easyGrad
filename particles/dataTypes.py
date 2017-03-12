class AbstractScalar(object):

    def __init__(self, name, parent=None):
        self.name = name
        self.val = None
        self.initialized = False
        self.parent = parent

    def __add__(self, s):
        pass

    def __multiply__(self, s):
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


class NodeVal(object):

    def __init__(self, name, operand1, operand2, operator):
        self.name = name
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator

    def forward(self):
        pass

    def backward(self):
        pass

    def __str__(self):
        string = "Adding : " + '\n' +\
                 str(self.operand1) + '\n' +\
                 str(self.operand2) + '\n' + '=' * 10
        return string


class AddVarNode(NodeVal):

    def __init__(self, operand1, operand2, operator='+'):
        name = str(operand1) + " + " + str(operand2)
        super(AddVarNode, self).__init__(name, operand1, operand2, operator)
        self.inpNodes = [operand1, operand2]

    def forward(self):
        self.val = self.operand1.val + self.operand2.val


class SubVarNode(NodeVal):

    def __init__(self, operand1, operand2, operator='-'):
        name = str(operand1) + " - " + str(operand2)
        super(SubVarNode, self).__init__(name, operand1, operand2, operator)
        self.inpNodes = [operand1, operand2]

    def forward(self):
        self.val = self.operand1.val - self.operand2.val


class MultVarNode(NodeVal):

    def __init__(self, operand1, operand2, operator='*'):
        name = str(operand1) + " * " + str(operand2)
        super(MultVarNode, self).__init__(name, operand1, operand2, operator)
        self.inpNodes = [operand1, operand2]

    def forward(self):
        self.val = self.operand1.val * self.operand2.val


class Integer(AbstractScalar):

    def __init__(self, name, parent=None):
        super(Integer, self).__init__(name, parent)
        if parent is not None:
            self.inpNodes = parent.inpNodes
        else:
            self.inpNodes = []

    def __add__(self, t):
        inp_fn = AddVarNode(self, t)
        node = Integer(inp_fn.name, inp_fn)
        return node

    def __sub__(self, t):
        inp_fn = SubVarNode(self, t)
        node = Integer(inp_fn.name, inp_fn)
        return node

    def __mul__(self, t):
        inp_fn = MultVarNode(self, t)
        node = Integer(inp_fn.name, inp_fn)
        return node

    def forward(self):
        self.parent.forward()
        self.val = self.parent.val
