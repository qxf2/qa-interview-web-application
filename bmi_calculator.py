"""
Purpose:
A Flask application to calculate the BMI of the user.

"""

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

def calculate_bmi(weight_of_the_user,height_of_the_user):
    # Calculate the BMI of the user according to height and weight
    bmi_of_the_user = round(weight_of_the_user/(height_of_the_user * height_of_the_user),1)
    return bmi_of_the_user

@app.route("/", methods=['GET', 'POST'])
@app.route("/bmi", methods=['GET', 'POST'])
def bmi():
    "Endpoint for calculating the bmi of a user"
    if request.method == 'GET':
        #return the form
        return render_template('bmi.html')
    if request.method == 'POST':
        #return the answer
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        
        result = calculate_bmi(weight,height)
        api_response = {"answer": result}
        return jsonify(api_response)


#---START OF SCRIPT
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6464, debug= True)