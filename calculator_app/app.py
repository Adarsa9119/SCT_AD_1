from flask import Flask, render_template, request, jsonify
from simpleeval import simple_eval, SimpleEval, FunctionNotDefined

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")
    try:
        result = simple_eval(expression)  # safer evaluation
        return jsonify(result=str(result))
    except (FunctionNotDefined, SyntaxError, ZeroDivisionError):
        return jsonify(result="Error")

if __name__ == "__main__":
    app.run(debug=True)