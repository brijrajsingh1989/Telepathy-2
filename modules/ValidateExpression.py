class ValidateExpression:
    def __init__(self, expression):
        self.Expression = expression
    
    def ValidateExpression(self):
        stack = []
        for char in self.Expression:
            if char == '{' or char == '(' or char == '[':
                stack.append(char)
            
            elif char == '}' or char == ')' or char == ']':
                if len(stack) == 0:
                    return False
                top_element = stack.pop()
                if not self.Compare(top_element, char):
                    return False
        if len(stack) != 0:
            return False
        return True

    def Compare(self, opening, closing):
        if opening == '(' and closing == ')':
            return True
        if opening == '[' and closing == ']':
            return True
        if opening == '{' and closing == '}':
            return True  
        return False