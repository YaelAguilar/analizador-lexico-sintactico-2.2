from flask import Flask, request, jsonify
from app.lexer import tokenize
from app.parser import parse

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.json.get('code')
    try:
        tokens = tokenize(code)
        print("Tokens generados por el lexer:", tokens)  # Imprimir tokens para verificación
        result = parse(code)
        return jsonify({"resultado": result, "tokens": tokens})
    except SyntaxError as e:
        return jsonify({"error": str(e), "tokens": tokens})

if __name__ == '__main__':
    app.run(debug=True)
