import math
import dataTypes as dt
from copy import deepcopy
import ops


class MonoNodeVal(object):

    def __init__(self, name, operand, operator):
        self.name = name
        self.operand = operand

    def forward(self):
        pass

    def backward(self):
        pass

    def __str__(self):
        string = self.operand + " : " +\
            str(self.operand) + '\n' + '=' * 10
        return string


class DiNodeVal(object):

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
        string = "Operating on : " + '\n' +\
                 str(self.operand1) + '\n' +\
                 str(self.operand2) + '\n' + '=' * 10
        return string


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
        self.gradient_nodes = {
            self.operand1: dt.Integer("Constant", val=1),
            self.operand2: dt.Integer("Constant", val=1)
        }


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
        self.gradient_nodes = {
            self.operand1: dt.Integer("Constant", val=1),
            self.operand2: dt.Integer("Constant", val=-1)
        }


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

        self.gradient_nodes = {
            self.operand1: dt.Integer("grad" + str(self.operand2),
                                      val=self.operand2.val),
            self.operand2: dt.Integer("grad" + str(self.operand1),
                                      val=self.operand1.val)
        }


class DivVarNode(DiNodeVal):

    def __init__(self, operand1, operand2, operator='*'):
        name = str(operand1) + " / " + str(operand2)
        super(DivVarNode, self).__init__(name, operand1, operand2, operator)
        self.inpNodes = [operand1, operand2]
        self.gradients = []

    def forward(self):
        assert(self.operand2.val != 0), "Dividing by zero."
        self.gradients = {self.operand1: 1.0/self.operand2.val,
                          self.operand2: self.operand1.val *
                          math.log(self.operand2.val)}
        self.val = self.operand1.val / self.operand2.val
        print vars(self.operand1)
        self.gradient_nodes = {
            self.operand1: dt.Integer("grad" + str(self.operand1),
                                      val=1.0/self.operand2.val),
            self.operand2: dt.Integer("grad" + str(self.operand1),
                                      val=self.operand1.val) *
            ops.log(dt.Integer("grad" + str(self.operand2),
                               val=self.operand2.val))
        }


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
