"""
This is a Flask application that can be used to interview QA engineers. 
All the application does is to calculate the factorial of a number. 
But there have been bugs seeded. For example, this application will go into an infinite loop if you pass it a negative number.
To learn more, see the README.md of this application.
"""

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

def calculate_factorial(n):
    "Calculate the factorial of a number"
    if n==0:
        return 1
    else:
        return n*calculate_factorial(n-1)

@app.route("/factorial", methods=['GET', 'POST'])
def factorial():
    "Endpoint for calculating the factorial of a number"
    if request.method == 'GET':
        #return the form
        return render_template('factorial.html')
    if request.method == 'POST':
        #return the answer
        number = int(request.args.get('number'))
        result = calculate_factorial(number)
        api_response = {"answer": result}
        return jsonify(api_response)

#---START OF SCRIPT
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6464, debug= True)