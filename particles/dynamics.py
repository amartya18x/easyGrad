import math
import numpy as np

class ValNodes(object):

    def __init__(self):
        self.type_node = ValNodes
        #For future work to define common properties
        
class MonoNodeVal(ValNodes):

    def __init__(self, name, operand, operator):
        super(MonoNodeVal, self).__init__()
        self.name = name
        self.operand = operand
        self.operator = operator
        
    def forward(self):
        pass

    def backward(self):
        pass

    def __str__(self):
        string = self.operator + " : " +\
                 str(self.operand) + '\n' + '=' * 10
        return string


class DiNodeVal(ValNodes):

    def __init__(self, name, operand1, operand2, operator):
        super(DiNodeVal, self).__init__()
        self.name = name
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator

    def forward(self):
        pass

    def backward(self):
        pass

    def __str__(self):
        string = "Operating on : " + '\n' +\
                 str(self.operand1) + '\n' +\
                 str(self.operand2) + '\n' + '=' * 10
        return string

class TensorDiNodeVal(ValNodes):

    def __init__(self, name, operand1, operand2, operator):
        super(TensorDiNodeVal, self).__init__()
        self.name = name
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator

    def forward(self):
        self.operand1.type_cast_tensor()
        self.operand2.type_cast_tensor()
        
        
        self.shape1 = self.operand1.val.shape
        self.shape2 = self.operand2.val.shape
        

    def backward(self):
        pass

    def __str__(self):
        string = "Operating on : " + '\n' +\
                 str(self.operand1) + '\n' +\
                 str(self.operand2) + '\n' + '=' * 10
        return string


# This is for operations involving two nodes

# Scalar operations
class AddVarNode(DiNodeVal):

    def __init__(self, operand1, operand2, operator='+'):
        name = str(operand1) + " + " + str(operand2)
        super(AddVarNode, self).__init__(name, operand1, operand2, operator)
        self.inpNodes = [operand1, operand2]
        self.gradients = []

    def forward(self):
        self.gradients = {self.operand1: 1,
                          self.operand2: 1}
        self.val = self.operand1.val + self.operand2.val


class SubVarNode(DiNodeVal):

    def __init__(self, operand1, operand2, operator='-'):
        name = str(operand1) + " - " + str(operand2)
        super(SubVarNode, self).__init__(name, operand1, operand2, operator)
        self.inpNodes = [operand1, operand2]
        self.gradients = []

    def forward(self):
        self.gradients = {self.operand1: 1,
                          self.operand2: -1}
        self.val = self.operand1.val - self.operand2.val


class MultVarNode(DiNodeVal):

    def __init__(self, operand1, operand2, operator='*'):
        name = str(operand1) + " * " + str(operand2)
        super(MultVarNode, self).__init__(name, operand1, operand2, operator)
        self.inpNodes = [operand1, operand2]
        self.gradients = []

    def forward(self):
        self.gradients = {self.operand1: self.operand2.val,
                          self.operand2: self.operand1.val}
        self.val = self.operand1.val * self.operand2.val


class DivVarNode(DiNodeVal):

    def __init__(self, operand1, operand2, operator='*'):
        name = str(operand1) + " * " + str(operand2)
        super(DivVarNode, self).__init__(name, operand1, operand2, operator)
        self.inpNodes = [operand1, operand2]
        self.gradients = []

    def forward(self):
        assert(self.operand2.val != 0), "Dividing by zero."
        self.gradients = {self.operand1: self.operand1.val,
                          self.operand2: self.operand1.val *
                          math.log(self.operand2.val)}
        self.val = self.operand1.val / self.operand2.val

# Tensor operations
class TensorAddVarNode(TensorDiNodeVal):

    def __init__(self, operand1, operand2, operator='+'):
        name = str(operand1) + " + " + str(operand2)
        super(TensorAddVarNode, self).__init__(name, operand1, operand2, operator)
        self.inpNodes = [operand1, operand2]
        self.gradients = []

    def forward(self):
        super(TensorAddVarNode, self).forward()
        self.gradients = {self.operand1: np.ones(self.shape1),
                          self.operand2: np.ones(self.shape2)}
        self.val = self.operand1.val + self.operand2.val


class TensorSubVarNode(TensorDiNodeVal):

    def __init__(self, operand1, operand2, operator='-'):
        name = str(operand1) + " - " + str(operand2)
        super(TensorSubVarNode, self).__init__(name, operand1, operand2, operator)
        self.inpNodes = [operand1, operand2]
        self.gradients = []

    def forward(self):
        super(TensorSubVarNode, self).forward()
        self.gradients = {self.operand1: np.ones(self.shape1),
                          self.operand2: -1*np.ones(self.shape2)}
        self.val = self.operand1.val - self.operand2.val


class TensorMultVarNode(TensorDiNodeVal):

    def __init__(self, operand1, operand2, operator='*'):
        name = str(operand1) + " * " + str(operand2)
        super(TensorMultVarNode, self).__init__(name, operand1, operand2, operator)
        self.inpNodes = [operand1, operand2]
        self.gradients = []

    def forward(self):
        super(TensorMultVarNode, self).forward()
        self.gradients = {self.operand1: self.operand2.val,
                          self.operand2: self.operand1.val}
        self.val = self.operand1.val * self.operand2.val


class TensorDivVarNode(TensorDiNodeVal):

    def __init__(self, operand1, operand2, operator='*'):
        name = str(operand1) + " * " + str(operand2)
        super(TensorDivVarNode, self).__init__(name, operand1, operand2, operator)
        self.inpNodes = [operand1, operand2]
        self.gradients = []

    def forward(self):
        super(TensorDivVarNode, self).forward()
        assert(self.operand2.val != 0), "Dividing by zero."
        self.gradients = {self.operand1: self.operand1.val,
                          self.operand2: self.operand1.val *
                          np.log(self.operand2.val)}
        self.val = self.operand1.val / self.operand2.val


class TensorDotVarNode(TensorDiNodeVal):

    def __init__(self, operand1, operand2, operator='(dot)'):
        name = str(operand1) + "(dot)" + str(operand2)
        super(TensorDotVarNode, self).__init__(name, operand1, operand2, operator)
        self.inpNodes = [operand1, operand2]
        self.gradients = []
        
    def forward(self):
        super(TensorDotVarNode, self).forward()
        self.gradients = {self.operand1: self.operand2.val.T,
                          self.operand2: self.operand1.val.T}
        self.val = np.dot(self.operand1.val, self.operand2.val)
        
# Element wise single node operations
# This includes operations for which you need only one operand

class ExpNode(MonoNodeVal):

    def __init__(self, operand):
        name = "Exp(" + str(operand) + ")"
        super(ExpNode, self).__init__(name, operand, operator='Exp')
        self.inpNodes = [operand]
        self.gradients = []

    def forward(self):
        self.val = math.exp(float(self.operand.val))
        self.gradients = {self.operand: self.val}


class LogNode(MonoNodeVal):

    def __init__(self, operand):
        name = "Exp(" + str(operand) + ")"
        super(LogNode, self).__init__(name, operand, operator='Log')
        self.inpNodes = [operand]
        self.gradients = []

    def forward(self):
        assert(self.operand.val != 0)
        self.val = math.log(float(self.operand.val))
        self.gradients = {self.operand: 1.0 / self.operand.val}


class SigmNode(MonoNodeVal):

    def __init__(self, operand):
        name = "Sigm(" + str(operand) + ")"
        super(SigmNode, self).__init__(name, operand, operator='Sigm')
        self.inpNodes = [operand]
        self.gradients = []

    def forward(self):
        self.val = 1.0 / (1 + math.exp(-float(self.operand.val)))
        self.gradients = {self.operand: self.val * (1.0 - self.val)}


class TanhNode(MonoNodeVal):

    def __init__(self, operand):
        name = "Tanh(" + str(operand) + ")"
        super(TanhNode, self).__init__(name, operand, operator='Tanh')
        self.inpNodes = [operand]
        self.gradients = []

    def forward(self):
        posex = math.exp(float(self.operand.val))
        negex = math.exp(-float(self.operand.val))
        self.val = (posex - negex) / (posex + negex)
        self.gradients = {self.operand: 1.0 - self.val**2}
