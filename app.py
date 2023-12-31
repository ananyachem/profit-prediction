from flask import Flask, render_template, request

app = Flask(__name__)

import pickle
model = pickle.load(open(r'D:/flask/profit prediction/model.pkl','rb'))

@app.route('/')
def helloworld():
    return render_template("index.html")

@app.route('/login', methods =['POST'])
def login():
    p =request.form["ms"]
    q= request.form["as"]
    r= request.form["rd"]
    s= request.form["s"]
    if (s=="cal"):
        s1,s2,s3=1,0,0
    if (s=="flo"):
        s1,s2,s3=0,1,0
    if (s=="ny"):
        s1,s2,s3=0,0,1
        
    t=[[int(s1),int(s2),int(s3),int(p),int(q),int(r)]]
    output= model.predict(t)
    print(output)  
        
    return render_template("index.html",y = "the predicted profit is  " + str(output[0]) )

if __name__ == '__main__' :
    app.run(debug= False)