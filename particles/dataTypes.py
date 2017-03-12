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
            val = " without any value"
            return "{Integer : " + self.name + val+" }"
        else:
            return "{Integer : " + self.name + " }"


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

    def forward(self):
        self.val = self.operand1.val + self.operand2.val


class Integer(AbstractScalar):

    def __init__(self, name, parent=None):
        super(Integer, self).__init__(name, parent)

    def __add__(self, t):
        inp_fn = AddVarNode(self, t)
        node = Integer(inp_fn.name, inp_fn)
        return node
