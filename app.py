# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:45:30 2022

@author: anuaq
"""

from unicodedata import name

from flask import Flask,render_template,request,redirect
# import createfile
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('user.html')

@app.route('/showtext') 
def show():
    return("Just wanted to show you some text")

@app.route('/dietplans') 
def dietplans(): 
    return redirect("https://www.healthy-dietplans.com/")

@app.route('/greet/<name>')
def greet(name):
       return "Hello, "+ name
   
@app.route('/greet/<catname>/<product>')
def showproducts(catname,product):
    return f"Category: {catname}, Product: {product}"


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"Sum = {a + b}"


@app.route("/marks/<int:score>")
def marks(score):
    return render_template("result.html", score=score)   

@app.route("/calculate",methods=["POST","GET"])
def calculate():
        age=int(request.form['age'])
        height=int(request.form['height'])
        gender=request.form['gender']
        if(age<6):
            wt=2*(age+5)
        elif(age<14):
            wt=4*age
        else:
            if(gender=="male"):
                wt=22*(height/100)**2
            elif(gender=="female"):
                wt=22*((height - 10)/100)**2
        # createfile.append_to_csv([age, height, gender, round(wt)])
        return render_template('user.html',weight=round(wt),message="Your optimal weight in kgs is  ")
    
if __name__ == '__main__':
    app.run(port=8000)
    
    # html page image from static/images folder
    # <img src="{{ url_for('static', filename='images/munnar.jpg') }}" alt="Munnar">
#  <img src="{{ url_for('static', filename='images/munnar.jpg') }}" width="300"> <p>Munnar - Hill Station</p>

    # <a href="{{ url_for('about') }}">About</a>
    
#     @app.route("/user/<name>")
# def user(name):
#     return f"Hello {name}"
# in html
# <a href="{{ url_for('user', name='Anu') }}">Visit Profile</a>
    
    # return redirect(url_for("welcome", username=name))
            # return redirect(url_for("success"))


    
    
    

