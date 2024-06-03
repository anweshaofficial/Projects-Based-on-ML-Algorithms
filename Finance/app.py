
import flask
from flask import Flask, request, jsonify
#cant name flask
app = Flask(__name__)

@app.route('/process_income', methods=['POST'])
def process_income():
    data = request.json
    income = data['income']
    
    # Simple logic to divide income
    investments = income * 0.3
    expenditure = income * 0.5
    savings = income * 0.2

    return jsonify({
        'investments': investments,
        'expenditure': expenditure,
        'savings': savings
    })

if __name__ == '__main__':
    app.run(debug=True)
