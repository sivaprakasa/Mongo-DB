import flask
from flask import Flask
from flask_pymongo import PyMongo
from flask import request
from flask import render_template

app = Flask(__name__)

mongo_client = PyMongo(app,uri="mongodb://localhost:27017/flaskmongo")
db = mongo_client.db

@app.route('/')
def register():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')
        db.register.insert_many([{
            'name':name,
            'phone':phone,
            'password':password,
            'cpassword':cpassword
        }])
        return render_template('login.html',name=name,phone=phone,password=password,cpassword=cpassword)


if __name__ == '__main__':
    app.run(debug=True)