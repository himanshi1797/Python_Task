
from flask import Flask, request, jsonify
from flask import render_template
from pymongo import MongoClient

# creates a Flask application, named app
app = Flask(__name__)
myclient=MongoClient('mongodb://localhost:27017')
mydb = myclient.user
userinfo = mydb.user_info

# a route where we will display a welcome message via an HTML template
#for login
@app.route("/")
def login():
   return render_template('login.html')

#for register
@app.route("/register")
def register():
   return render_template('register.html')

#for dashboard
@app.route('/register_submit', methods=['POST'])
def register_submit():
    result = request.form
    user_data = {'username': result['username'],
                 'email': result['email'],
                 'password': result['password']}
    userinfo.insert_one(user_data)
    return render_template('dashboard.html', message='hello {}'.format(result['username']))



@app.route('/user_detail', methods= ['POST'])
def user_info():
    inf = request.form
    info = userinfo.find_one({'email' : inf['email']})
    if info!=None and info['password'] == inf['password']:
        return render_template('dashboard.html', message='HELLO {}'.format(info['username']))
    else:
        return render_template('login.html')

# run the application
if __name__ == "__main__":
    app.run(debug=True)
