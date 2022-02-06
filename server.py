from flask import Flask, jsonify, request
from modules.EvaluateExpressionTree import EvaluateExpressionTree
from modules.ExpressionTree import ExpressionTree
from modules.ValidateExpression import ValidateExpression

app = Flask(__name__)

def CheckInput(input):
    if not input or not 'exp' in input:
        return jsonify({'error':'expression not found'}), 500
    expression = input['exp']
    if expression == "" or expression == None:
        return jsonify({'error':'invalid expression'}), 500
    ValidateExpressionObj = ValidateExpression(expression)
    if not ValidateExpressionObj.ValidateExpression():
        return jsonify({'error':'invalid expression'}), 500
    return expression, 200

@app.route('/GetPreorderTraversal', methods=['POST'])
def GetPreorderTraversal():
    expression, code = CheckInput(request.json)
    if code != 200:
        return expression
    ExpressionTreeObj = ExpressionTree(expression)
    return jsonify({'result':ExpressionTreeObj.PreOrderTraversal()})

@app.route('/GetPostorderTraversal', methods=['POST'])
def GetPostorderTraversal():
    expression, code = CheckInput(request.json)
    if code != 200:
        return expression
    ExpressionTreeObj = ExpressionTree(expression)
    return jsonify({'result':ExpressionTreeObj.PostOrderTraversal()})

@app.route('/GetInorderTraversal', methods=['POST'])
def GetInorderTraversal():
    expression, code = CheckInput(request.json)
    if code != 200:
        return expression
    ExpressionTreeObj = ExpressionTree(expression)
    return jsonify({'result':ExpressionTreeObj.InOrderTraversal()})

@app.route('/EvaluateExpression', methods=['POST'])
def EvaluateExpression():
    expression, code = CheckInput(request.json)
    if code != 200:
        return expression
    ExpressionTreeObj = ExpressionTree(expression)
    EvaluateExpressionTreeObj = EvaluateExpressionTree()
    return jsonify({'result':EvaluateExpressionTreeObj.EvaluateExpressionTree(ExpressionTreeObj.RootNode)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)