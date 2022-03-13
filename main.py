""""Main file"""
import os
from dotenv import find_dotenv, load_dotenv
from flask import Blueprint, Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from movies import get_movie_data, get_movie_id, get_wiki_data

app = Flask(__name__)
db = SQLAlchemy(app)
load_dotenv(find_dotenv())
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    """Load User"""
    return Credentials.query.get(int(user_id))


app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("HEROKU_DATABASE")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


class Credentials(db.Model, UserMixin):
    """User Credentials"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(300), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)


class Reviews(db.Model):
    """Reviews"""

    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(30), db.ForeignKey("credentials.username"))
    movie = db.Column(db.String(300))
    rating = db.Column(db.String(10))
    review = db.Column(db.String(1000))


db.create_all()


class SignupForm(FlaskForm):
    """SignupForm"""

    username = StringField(
        validators=[InputRequired(), Length(min=5, max=30)],
        render_kw={"placeholder": "Username"},
    )
    password = PasswordField(
        validators=[InputRequired(), Length(min=5, max=300)],
        render_kw={"placeholder": "Password"},
    )

    submit = SubmitField("Register")

    def validate_username(self, username):
        """Username Validation"""
        current_username = Credentials.query.filter_by(username=username.data).first()
        if current_username:
            raise ValidationError(
                "This username already exists. Please log in instead."
            )


class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField(
        validators=[InputRequired(), Length(min=5, max=30)],
        render_kw={"placeholder": "Username"},
    )
    password = PasswordField(
        validators=[InputRequired(), Length(min=5, max=30)],
        render_kw={"placeholder": "Password"},
    )

    submit = SubmitField("Login")

    def validate_username(self, username):
        """Username Validation"""
        current_username = Credentials.query.filter_by(username=username.data).first()
        if current_username is None:
            raise ValidationError("This username does not exist. Please sign up.")


@app.route("/")
def index():
    """Default route"""
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login method"""
    form = LoginForm()
    if form.validate_on_submit():
        user = Credentials.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("homepage"))

    return render_template("login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Signup Method"""
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        new_user = Credentials(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("signup.html", form=form)


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    """Logout method"""
    logout_user()
    return redirect(url_for("login"))


@app.route("/review", methods=["POST"])
def moveie_review():
    """ "Movie Reviews"""
    user = request.form.get("user")
    movie = request.form.get("movie_name")
    rating = request.form.get("rating")
    review = request.form.get("review")
    new_review = Reviews(user=user, movie=movie, rating=rating, review=review)
    db.session.add(new_review)
    db.session.commit()
    return redirect(url_for("homepage"))


@app.route("/homepage", methods=["GET", "POST"])
@login_required
def homepage():
    """Homepage"""
    reviews = Reviews.query.all()
    movie_id = get_movie_id()
    data = get_movie_data(movie_id)
    wiki = get_wiki_data(data["title"])
    return render_template("ind.html", movie=data, wiki=wiki, reviews=reviews)


bp = Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)


@app.route("/reacts")
def commentsandratings():
    """Render React page"""
    return render_template("index.html")


@app.route("/comment/<id>", methods=["DELETE"])
def delete_comment(comment_id):
    """Delete Comment"""
    response = {}
    review = Reviews.query.get(comment_id)
    response["id"] = review.id
    db.session.delete(review)
    db.session.commit()


@app.route("/comments")
def comments():
    """Send Comments"""
    reviews = Reviews.query.all()
    info = []
    for i in reviews:
        review_list = {}
        review_list["id"] = i.id
        review_list["user"] = i.user
        review_list["movie"] = i.movie
        review_list["rating"] = i.rating
        review_list["review"] = i.review
        info.append(review_list)

    return jsonify(info)


app.register_blueprint(bp)

app.run(debug=True)