# Movie Discovery - Shams Sikder

This is a web app to show my favorite movies and link to their wikipedia pages. The data is retrieved dynamically through the use of third-party APIs from Wikipedia and TheMovieDataBase. This app also has a signup and login functionality. It also allows the users to to leave reviews for the movies. This is done through the use of postgresql databases. There is also a page where you can edit and delete comments built on a react framework.

## Heroku

This web app was deployed on heroku which can be accessed here: [Movie Discovery](https://shamsmovie.herokuapp.com/)

## Technologies

1. Python
2. HTML
3. CSS
4. Javascript

## Frameworks

1. Flask
2. React

## Libraries

1. os
2. random
3. requests
4. dotenv
5. flask_login
6. flask_wtf
7. flask_bcrypt
8. wtforms 
9. email_validator
10. psycopg2-binary
11. Flask-SQLAlchemy

## APIs

1. TMDB
2. Wikipedia

## Setup

Anyone trying to fork this project will need to pip install Flask, requests, python-dotenv, flask_login, flask_wtf, flask_bcrypt, wtforms, email_validator, psycopg2-binary, and Flask-SQLAlchemy==2.1. Additionally, an API key is needed from TMDB and substituted in for "TMDB_KEY" in order to retreive the data. They will also have to install react.
