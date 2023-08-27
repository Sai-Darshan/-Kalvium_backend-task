from flask import Flask, request, jsonify
from collections import deque
import json

app = Flask(__name__)

# Initialize operation history as a deque with max length 20
operation_history = deque(maxlen=20)

def calculate(expression):
    return eval(expression)


@app.route('/history', methods=['GET'])
def get_history():
    history_list = list(operation_history)

    return jsonify(history_list)

@app.route('/<path:expression>', methods=['GET'])
def perform_operation(expression):
    expression = expression.replace("/","").replace("plus","+").replace("minus","-").replace("by","/").replace("into","*")
    ans = {"question":expression, "ans":eval(expression)}
    operation_history.append(str(ans))
    return json.dumps(ans)

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
