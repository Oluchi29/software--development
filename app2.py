from flask import Flask,render_template
app=Flask(__name__)
@ app.route("/")
def home():
    return "welcome to my website"

@app.route("/aboutus")
def aboutus():
    name="mrs apere"
    email="oluchi@gmail.com"
    return "This are my details" + name + "," + email


@app.route("/multiplication")
def multiply():
    a=40
    b=20
    c=a*b
   # return str(c)
    return render_template("multiplication.html" ,multiplicationscore=c)

@app.route("/subtraction")
def subtract():
    a=40
    b=20
    c=a-b
    #return str(c)
    return render_template("subtractraction.html" , subtractionscore=c)

@ app.route("/addition")
def add():
    a=40
    b=20
    c=a+b
   # return str(c)
    return render_template("addition.html" , additionscore= c)





if __name__ == '__main__':
   app.run(debug=True, port=5000,host="127.0.0.1")