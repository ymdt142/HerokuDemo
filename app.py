from flask import Flask,render_template,request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app=Flask(__name__) #flask is the class and __name__ is the defult parameter
@app.route('/',methods=['GET','POST'])
def home_page():
    print("rendering homepage")
    return render_template("index.html")
@app.route('/predict', methods=['POST'])
def index():
    print("here")
    if(request.method=="POST"):
        gre_score=float(request.form['gre_score'])
        print("1")
        toefl_score=float(request.form['toefl_score'])
        print("2")
        university_rating=float(request.form['university_rating'])
        print("3")
        sop=float(request.form['sop'])
        print("4")
        lor = float(request.form['lor'])
        print("5")
        cgpa = float(request.form['cgpa'])
        is_research = request.form['research']
        if(is_research=='yes'):
            research=1
        else:
            research=0
        print("loading model")
        model_name="my_first_model.pickle"
        print("Done")
        model=pickle.load(open(model_name,'rb'))
        print("Done")
        prediction=model.predict([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]])
        print('prediction is',prediction)
        return  render_template('result.html',prediction=round(100*prediction[0]))

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app

