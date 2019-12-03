"""
This is a Flask application that can be used to interview QA engineers. 
All the application does is to calculate the factorial of a number. 
But there have been bugs seeded. For example, this application will go into an infinite loop if you pass it a negative number.
To learn more, see the README.md of this application.
"""

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

def calculate_bmi(weight_of_user,height_of_user):
    "Calculate the bmi of the user"
    user_bmi = round(((weight_of_user/(height_of_user * height_of_user))*10000),1)
    return user_bmi

@app.route("/", methods=['GET', 'POST'])
@app.route("/bmi", methods=['GET', 'POST'])
def bmi():
    "Endpoint for calculating the BMI of a user"
    if request.method == 'GET':
        #return the form
        return render_template('bmi.html')
    if request.method == 'POST':
        #return the answer
        weight = int(request.form.get('weight'))
        height = int(request.form.get('height'))
        result = calculate_bmi(weight,height)
        api_response = {"answer": result}
        return jsonify(api_response)

#---START OF SCRIPT
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6464, debug= True)