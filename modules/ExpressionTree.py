from modules.Node import Node


class ExpressionTree():

    def __init__(self, expression):
        self.Expression = expression
        self.RootNode = self.GetRootNode(expression)
        self.ExpressionTreePostOrderTraversal = []
        self.ExpressionTreePreOrderTraversal = []
        self.ExpressionTreeInOrderTraversal = []

    def GetRootNode(self, exp):
        def compute(operands, operators):
            right, left = operands.pop(), operands.pop()
            operands.append(Node(val=operators.pop(), left=left, right=right))

        precedence = {'+':0, '-':0, '*':1, '/':1}
        operands, operators, operand = [], [], 0
        isSignedNumber = False
        for i in range(len(exp)):
            if exp[i].isdigit():
                operand = operand*10 + int(exp[i])
                if i == len(exp)-1 or not exp[i+1].isdigit():
                    operands.append(Node(val=str(operand)))
                    operand = 0
                if not exp[i+1].isdigit() and isSignedNumber:
                    value = operands.pop().val
                    operands.append(Node(val=str('-') + str(value)))
                    isSignedNumber = False
            elif exp[i] == '(':
                operators.append(exp[i])
            elif exp[i] == ')':
                while operators[-1] != '(':
                    compute(operands, operators)
                operators.pop()
            elif exp[i] in precedence:
                if ((i - 1) >= 0) and ((i - 1) < len(exp)) and exp[i - 1] in precedence:
                    isSignedNumber = True
                    continue
                while operators and operators[-1] in precedence and \
                      precedence[operators[-1]] >= precedence[exp[i]]:
                    compute(operands, operators)
                operators.append(exp[i])
        while operators:
            compute(operands, operators)
        return operands[-1]
    
    def GetPostOrderTraversal(self, root):
        if root == None:
            return None
        self.GetPostOrderTraversal(root.left)
        self.GetPostOrderTraversal(root.right)
        self.ExpressionTreePostOrderTraversal.append(root.val)
    
    def GetPreOrderTraversal(self, root):
        if root == None:
            return None
        self.ExpressionTreePreOrderTraversal.append(root.val)
        self.GetPreOrderTraversal(root.left)
        self.GetPreOrderTraversal(root.right)
    
    def GetInOrderTraversal(self, root):
        if root == None:
            return None
        self.GetInOrderTraversal(root.left)
        self.ExpressionTreeInOrderTraversal.append(root.val)
        self.GetInOrderTraversal(root.right)
        

    def PostOrderTraversal(self):
        self.GetPostOrderTraversal(self.RootNode)
        return self.ExpressionTreePostOrderTraversal
    
    def PreOrderTraversal(self):
        self.GetPreOrderTraversal(self.RootNode)
        return self.ExpressionTreePreOrderTraversal
    
    def InOrderTraversal(self):
        self.GetInOrderTraversal(self.RootNode)
        return self.ExpressionTreeInOrderTraversal
