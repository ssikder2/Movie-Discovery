# Movie Discovery - Shams Sikder

This is a web app to show my favorite movies and link to their wikipedia pages. The data is retrieved dynamically through the use of third-party APIs from Wikipedia and TheMovieDataBase. This app also has a signup and login functionality. It also allows the users to to leave reviews for the movies. This is done through the use of postgresql databases.

## Technologies

1. Python
2. HTML
3. CSS

## Frameworks

1. Flask

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

Anyone trying to fork this project will need to pip install Flask, requests, python-dotenv, flask_login, flask_wtf, flask_bcrypt, wtforms, email_validator, psycopg2-binary, and Flask-SQLAlchemy==2.1. Additionally, an API key is needed from TMDB and substituted in for "TMDB_KEY" in order to retreive the data.

## Heroku

This web app was deployed on heroku which can be accessed here: [Movie Discovery](https://shamsmovie.herokuapp.com/)

## Expectation vs. Reality

Overall I expected to work on the user authentication aspect of it first, then work on the user input, and then worry about small details and heroku deployment. Overall, that worked out the way I planned, but I expected the user authentication part to not take as long as it did and looking back, I should have started from the inside elements before addressing the outer ones to be more efficient. 

## Technical Issues

1. The first technical issue I had was when I set up the database for the login credentials, but everytime I entered the information on the signup page, I would get an error relating to the password field being too long. I understood this was because the password was hashed, so I changed the max length of that column inside the credentials database. That did not change anything and I was getting the same error. I researched the error online and looked at a lot of Stack Overflow links, but they essentially said the same things about increasing the length, but I wasn't sure how to implement that through my tech stack aside from the way I did it. I later realized that in order to update the specifications of a table you must drop the table first. So I dropped the table, ran it again, and it worked.

2. Another issue I had was deploying to heroku. I put in everything I thought I needed, and then I remembered there were extra imports compared to milestone 1 so I added those in and it still did not work. I then realized that the config variable for the database was not the same because it was postgres instead of postgresql, and did what the professor said in the discord to do about it. It still did not work which is when I looked at the heroku logs again to see the specific error messages and it essentially said the main.py file was not found. I was confused about this, but then I looked at my milestone 1 files and realized my main file was called main.py. After renaming my app.py to main.py, it finally worked.