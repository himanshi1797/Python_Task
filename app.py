from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
#for login
@app.route("/login")
def login():
   return render_template('login.html')

#for register
@app.route("/register")
def register():
   return render_template('register.html')

#for dashboard
@app.route("/dashboard")
def dashboard():
   return render_template('dashboard.html')

# run the application
if __name__ == "__main__":
    app.run(debug=True)