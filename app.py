from flask import Flask, request, render_template,url_for
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
#print('----------------hii-----------------')

@app.route('/',methods=['GET'])
# @cross_origin()
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Min_Temp= float(request.form["Min_Temp"])
        Max_Temp= float(request.form["Max_Temp"])
        Wind_Direc= float(request.form["Wind_Direc"])
        Wind_Speed = float(request.form["Wind_Speed"])
        Humidity = float(request.form["Humidity"])
        Pressure = float(request.form["Pressure"])/100
        Cloud = float(request.form["Cloud"])
        Temperature_C = float(request.form["Temperature_C"])
        Today_Rain=request.form["Today_Rain"]
        location=request.form['location']

        feature_list=[]

        if(Today_Rain=="Yes"):
             Today_Rain= 1
        else:
            Today_Rain=0

        location_list=["Vijayawada",
                       "Guntur",
                       "Amaravathi",
                       "Visakhapatnam",
          "Kurnool",
          "Mumbai",
          "Hyderabad",
          "Bengaluru",
          "Delhi",
          "London",
          "Paris",
          "New York",
          "Tokyo",
          "Beijing",
          "Istanbul",
          "Moscow",
          "Berlin",
          "Bangkok",
          "Rome",
          "Madrid",
          "Mexico City"
          "Shanghai",
          "Buenos Aires",
          "Sydney",
          "Johannesburg",
          "Mawsynram",
          "Cherrapunji",
          "Panama City",
          "Puerto Lopez",
          "Sydney"]
          
        feature_list.append(Min_Temp)
        feature_list.append(Max_Temp)
        feature_list.append(Wind_Direc)
        feature_list.append(Wind_Speed)
        feature_list.append(Humidity)
        feature_list.append(Pressure)
        feature_list.append(Cloud)
        feature_list.append(Temperature_C)
        feature_list.append(Today_Rain)


        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        
        traverse_list(location_list, location)

        ml = model.predict([feature_list])
        #print(ml)
        output=''
        if ml==1:
            output="There will be Rain tomorrow "
        else:
            output="There will be NO rain tomorrow"

        return render_template('index.html', result=output)
        
       
if __name__ == "__main__":
    app.run(debug=True)


    
