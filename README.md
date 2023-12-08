# Twitter Clone API

## Project Description

---

Twitter clone is a social media platform. Designed for users to share their thoughts, opinions, or best moments. The App will be made using react in the front end, this is the Django Rest Framework API for the app.

## Manual Testing

---

Manual testing showed that:

- Logged-out users ******************can not:******************
    - Create a tweet.
    - Like a tweet.
    - Reply to a tweet
    - Follow a user
- Logged-out users ********can :********
    - View a list of tweets
    - View individual tweets.
    - View account details
    - View a list of accounts.
    - View tweet replies.
    
    ---
    
- Logged-in users **can:**
    - Create a tweet.
    - Like a tweet.
    - Reply to a tweet.
    - Follow a user.
    - Edit their tweets.
    - Edit their replies.
    - View a list of tweets.
    - View individual tweets.
    - View account details.
    - View a list of accounts.
    - View tweet replies.
- Logged-in users **************can not**************:
    - Edit another user's tweet
    - Edit another user profile
    - Edit another user's response
    - Edit another user likes

## Deployment on Heroku.

---

- set the following environment variables:
    - CLIENT_ORIGIN
    - CLOUDINARY_URL
    - DATABASE_URL
    - DISABLE_COLLECTSTATIC
    - SECRET_KEY
- installed the following libraries to handle database connection:
    - psycopg2
    - dj-database-url
- configured dj-rest-auth library for JWTs
- set allowed hosts
- configured CORS:
    - set allowed_origins
- set default renderer to JSON
- added Procfile with release and web commands
- gitignored the env.py file
- generated requirements.txt
- deployed to Heroku.

## Credits.

---

The code used in this API was heavily inspired by the course content from Code Institute. In particular, the DRF API repository. Which can be found [here.](https://github.com/Code-Institute-Solutions/drf-api)