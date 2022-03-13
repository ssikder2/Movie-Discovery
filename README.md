# Movie Discovery - Shams Sikder

This is a web app to show my favorite movies and link to their wikipedia pages. The data is retrieved dynamically through the use of third-party APIs from Wikipedia and TheMovieDataBase. This app also has a signup and login functionality. It also allows the users to to leave reviews for the movies. This is done through the use of postgresql databases. There is also a page where you can edit and delete comments built on a react framework.

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


## Technical Issues

1. The first issue I had was that I was not able to connect a react app via a flask app route. I used blueprint and everything but no matter what I did it would say that index.html is not found, even if I ran npm run build. I believe this might be due to the fact that I have an m1 mac but I am not 100% sure. I got around this by running npm start on another terminal and just linking localhost:3000 to my current homepage.

2. The next issue I had was that I could not load the comments specifically for the current user. I tried many different ways directly on the flask app to just send those comments to the react app. I realized that there is no current_user attribute directly on the python file because it does not track the users. I tried doing it directly on the App.js file but I could not find a way to do it.

3. Another issue I had was with my edits. I can create the logic to send the information back to the flask server, but I could not make it so that the input text box would allow me to type in a new rating. The only way I saw around it was to take out the value of the rating, but then it would just be an empty textbox which does not solve the issue.

## Hardest Part of Project

Overall, I think the hardest part of the project was working with React. It's definitely not the most intuitive and it isn't something I'm very used to. It's very different from anything I've worked with so there's a big learning curve. I will say though that it did challenge me in a good way and I definitely learned a lot from it.