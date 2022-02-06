class EvaluateExpressionTree:
    def __init__(self):
        pass
    
    def EvaluateExpressionTree(self, expressionTreeNode):
        if expressionTreeNode is None: 
            return 0
        if expressionTreeNode.left is None and expressionTreeNode.right is None: 
            return int(expressionTreeNode.val)
        left_sum = self.EvaluateExpressionTree(expressionTreeNode.left)
        right_sum = self.EvaluateExpressionTree(expressionTreeNode.right) 
        if expressionTreeNode.val == '+': 
            return left_sum + right_sum 
        elif expressionTreeNode.val == '-': 
            return left_sum - right_sum 
        elif expressionTreeNode.val == '*': 
            return left_sum * right_sum 
        else: 
            return left_sum // right_sum 