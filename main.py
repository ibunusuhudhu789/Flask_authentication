from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\ibunu\\Downloads\\003 Starting-Files-flask-auth-start\\users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


@app.route('/')
def home():
    user = current_user
    return render_template("index.html", user=user)


@app.route('/secrets')
@login_required
def secrets():
    user = current_user.name
    print(user)
    return render_template("secrets.html", user=user)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        email = request.form["email"]
        users_email = User.query.filter_by(email=email).first()
        if users_email is None:
            hashed_password = generate_password_hash(password, "pbkdf2:sha256", 20)
            new_user = User(email=email, password=hashed_password, name=name)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("secrets"))
        else:
            flash("The user already exists. Try to login.")
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=user_name).first()
        if user is not None:
            user_password = user.password
            if check_password_hash(user_password, password):
                login_user(user)
                return redirect(url_for("secrets"))
            else:
                flash("Invalid password")
        else:
            flash("Invalid email")

    return render_template("login.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory("C:\\Users\\ibunu\\Downloads\\003 Starting-Files-flask-auth-start\\static\\files",
                               "cheat_sheet.pdf")




if __name__ == "__main__":
    app.run(debug=True)
