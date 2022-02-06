# #!flask/bin/python
# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return jsonify({'Item':"Hello, World!"})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)
from modules.EvaluateExpressionTree import EvaluateExpressionTree
from modules.ExpressionTree import ExpressionTree
from modules.ValidateExpression import ValidateExpression


def callMe(exp):
    print(exp)
    ValidateExpressionObj = ValidateExpression(exp)
    e = ExpressionTree(exp)
    rn = e.GetRootNode()
    print(e.PostOrderTraversal(exp))
    print(e.PreOrderTraversal(exp))
    print(e.InOrderTraversal(exp))
    EvaluateExpressionTreeObj = EvaluateExpressionTree()
    print(EvaluateExpressionTreeObj.EvaluateExpressionTree(rn))
    return ValidateExpressionObj.ValidateExpression()
if __name__ == '__main__':
    exp = '(15/(7-(1+1))*-3)-(2+(1+1))'
    print(callMe(exp))