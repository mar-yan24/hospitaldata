from website import create_app
from flask import Flask, render_template

app = create_app()

if __name__ == '__main__':
    #only run server if you run this file
    app.run(debug = True) #auto rerun server

''''
I did not create all of the code in this model, I did follow a guide online to help me with some of this flask code:

techwithtim
4/11/21
Version 2.0
Source code
https://github.com/techwithtim/Flask-Web-App-Tutorial

''''

#shivani code

#app = Flask(__name__)
#@app.route('/')
#def index():
#	return render_template('data.html')

#app.run('0.0.0.0',8080)


@app.route("data.html")
def data():
    return jsonify(result=app.run(debug = True)) 