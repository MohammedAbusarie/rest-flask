# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, redirect, url_for, request,jsonify
from algorithm import *

# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "hello world"
        return jsonify({'data': data})
  

#correctify
@app.route('/evaluate',methods = ['POST',"GET"])
def login():
   if request.method == 'POST':
      #obj = request.form['yes']
      try:
        jsonf=request.json
        user_answers=jsonf["user_answers"]
        model_answers=jsonf["model_answers"]
        return jsonify(correct_answers(user_answers,model_answers))
      except Exception as e:
        return e
        
      
   else:
      #user = request.args.get('nm')
      #return "shade"
      return ""
      pass
  
  
# driver function
if __name__ == '__main__':
    app.run(debug = True)
