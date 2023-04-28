from flask import Flask, render_template, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'podcast'

@app.route('/')
#index
def index():
    return render_template("index.html")

@app.route('/Aboutus')
#aboutus
def Aboutus():
    return render_template("Aboutus.html")

@app.route('/Health_podcast')
#healthPodacst
def Health_podcast():
    return render_template("Health_podcast.html")

@app.route('/Healthy_Recipes')
#Healthy_Recipes
def Healthy_Recipes():
    return render_template("Healthy_Recipes.html")

@app.route('/healthy_blogs')
#Healthy_blogs
def healthy_blogs():
    return render_template("healthy_blogs.html")

@app.route('/JoinUs')
#Joinus
def JoinUs():
    return render_template("JoinUs.html")
@app.route('/Analytics')
#Analytics
def Analytics():
    return render_template("Analytics.html")


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database2.db'
db = SQLAlchemy(app)

class joinustable (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    dob = db.Column(db.String(20))
    gender = db.Column(db.String(25))
    address = db.Column(db.String(60))
    username = db.Column(db.String(30))
    password = db.Column(db.String(20))

@app.route('/submitForm', methods=['POST','GET'])
def register_form_submit():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    phone = request.form['phone']
    dob = request.form['dob']
    gender = request.form['gender']
    address = request.form['address']
    username = request.form['username']
    password = request.form['password']

    signupdata = joinustable(firstname=firstname,lastname=lastname, phone=phone, dob=dob,gender=gender, address=address, username=username, password=password)
    db.session.add(signupdata)
    db.session.commit()
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def submit_form():
    username = request.form.get('username')
    password = request.form.get('password')
    user = joinustable.query.filter_by(username=username, password=password).first()

    if user:
        return redirect(url_for('index'))
    else:
        error_message = 'Invalid username or password'
        return f"""<script>alert('{error_message}'); window.history.back();</script>"""


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(debug=True)

