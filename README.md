# Twitter Clone API

## Project Description

---

Twitter clone is a social media platform. Designed for users to share their thoughts, opinions, or best moments. The App will be made using react in the front end, this is the Django Rest Framework API for the app.

## Manual Testing

---

Manual testing showed that:

## Manual Testing (Front-End)

---

Manual testing showed that users can:

### Create an account.

To test this during the development process. I ran the command to create a superuser. 
The command is as follows:
`
python manage.py createsuperuser
`

This created an account on the backend.

### Login/logout

    I tested login/logout functionality on the back end by:
    - signing in as superuser 1. 
        This showed be the dashboard with my username in the top right. 
    - signing out of the account by selecting logout in the dropdown. 
    - This showed me the option to login. 

    In conclusion, logging in and out of the back end was succesfull

### Listing all accounts. 

To test the accounts view to list all accounts I :
    - added '/accounts' to the end of the url. 
    - this displayed a list of all accounts that have been registered. Including the new accounts created. 

    - each account contains information such as: 
        account id, owner, username, following id, fololowers count and following count. 

### Listing individuall accounts. 

To test that the API could list individual accounts, I :
    - added an Id to the end of the url. /accounts/1.
    - This displayed the first account created. 
    This step was repeated with the numbers 2, 3 and 99. 
        2 returned the second account created.
        3 returned the third account created. 
        99 returned a detail not found message, showing the account does not exist. 

### Updating account details 

To test the API's ability to update the account details, I :
    - Visited my accounts url in the development back end.
    - Edited the name, image and content. 
    - This resulted in the json data being updated to match the previous updates. 

### Testing all followers instances. 
To test the api's ability to list all followers, I:
    - added '/followers' to the end of the url. 
    - This resulted in all follower instances being displayed. 
        The information returned included :
        id, owner,created at, followed, followed name

To test that the API could list individual followers, I :
    - added an Id to the end of the url. /followers/1.
    - This displayed the first follower created. 
    This step was repeated with the numbers 2, 3 and 99. 
        2 returned the second follower created.
        3 returned the third follower created. 
        99 returned a detail not found message, showing the follow does not exist. 

To test I could unfollow a user, I: 
    - found a follow which I owned, 
    - clicked 'delete'
    - reurned to the list of all follower instances
    - count decrease by 1 

To test I could follow a new account, I 
    - set a post request to follow a new account.
    - returned to the followers count
    - the count had increased by 1 

### Like/Unlike tweets

To test the api's ability to list all likes, I:
    - added '/likes' to the end of the url. 
    - This resulted in all like instances being displayed. 
        The information returned included :
        id, owner,created at, tweet

To test that the API could list individual likes, I :
    - added an Id to the end of the url. /likes/1.
    - This displayed the first likes created. 
    This step was repeated with the numbers 2, 3 and 99. 
        2 returned the second likes created.
        3 returned the third likes created. 
        99 returned a detail not found message, showing the like does not exist. 

    To test I could like a tweet, I 
    - set a post request to like a new tweet that i did not own.
    - returned to the likes list
    - the count had increased by 1
    - likes on the tweet increased by 1 

    - To test I could unlike tweets, I:
        -found a like id that I owned. 
        - deleted the like instance. 
        - reviewed the update like list, the count had decrese by one and the it had been removed from the list. 
        

### Listing and creating tweets

    To test the api's ability to list all likes, I:
    - added '/tweets' to the end of the url. 
    - This resulted in all tweet instances being displayed. 

    To test that the API could list individual tweets, I :
    - added an Id to the end of the url. /tweets/1.
    - This displayed the first tweet created. 
    This step was repeated with the numbers 2, 3 and 99. 
        2 returned the second like created.
        3 returned the third like created. 
        99 returned a detail not found message, showing the like does not exist

    To test that I could create a new tweet:
        -created a tweet, I sent a post request to the api with text content
        - returned to the list of tweets
        - saw the tweet count had increased by one. 
        - my new tweet was present on the page. 

    To test that I could edit a tweet I: 
        - located a tweet that I owned
        - entered new content to the tweet using a put request. 
        - returned to the tweet that I owned. 
        - noticed the content matched the updated text that I entered. 

    To test that I could delete a tweet, I :
        - visted a tweet that I owned
        - put in a delete request
        - returned to the tweet list
        - noticed that the count had decreased by one and the tweet was no longer present. 

### Reply to tweets

    To test the api's ability to list all replies, I:
    - added '/replies' to the end of the url. 
    - This resulted in all reply instances being displayed. 

    To test that the API could list individual replies, I :
    - added an Id to the end of the url. /replies/1.
    - This displayed the first reply created. 
    This step was repeated with the numbers 2, 3 and 99. 
        2 returned the second reply created.
        3 returned the third reply created. 
        99 returned a detail not found message, showing the like does not exis
   
     To test I could post a reply on the tweet I :
        - sent a post request to the reply end point (content, image and tweet selected). 
        I returned to the reply count 
        Noticed an increase of 1. 

    To test I could edit my own reply, I :
        - found a reply that I owned. 
        - updated the text content of the tweet. 
        - sent the put request to the api
        - returned to the reply. 
        - noticed to content had been updated to the content within the recent put request. 

    To test that I could delete my reply I:
        - found a reply that I owned.
        - sent a delete request to the api. 
        - returned to the replies list.
        - noticed that the count had been decreased by 1 
        - my reply was no longer present in the list. 


### Deployment Steps

1.**Set up your files**
    Before deployment, it is very important that you have both a procfile and an env.py file. 
    The *procfile* is the connection between your app and heroku. It is critical that it is included. 
    `release: python manage.py makemigrations && python manage.py migrate
    web: gunicorn twitter_clone_api.wsgi` 
    This version retains the essential commands for running database migrations during the release phase and starting the Gunicorn server for the web application.

    The *env.py* should contain variables that are private. For example, the sites secret key. 
        The settings.py file should be configured to enter this file and pull the variables from there as the private details and keys should not be public. 
        The env.py works effectively for this as it is included in the git ignor file. 

2. **Login to Heroku:**

3. **Create new app**

4. **Select your app name and region**

5. **Add your configuratinon variables**
    The configuration variables allow you to link between multiple resources in your API. 
    Within the api, the configuartion vars include: 
        Allowed host: Allowed host declares which url can access the api data. In this case is the front end app deployed on heroku. 
        Client origin: This allows for Cross-Origin Resource Sharing between the api and the front end. 
        client origin dev: This variable allows for the development enviorment (gitpod) to access the api. This is key for development of the site before final deployment.
        Cloudinary Url: The cloudinary variable connects the api to the image hosting site. 
        Database url: allows for a connection between the api and ElephantSQL database
        Disable collectstatic: this value means that django will not collect the static files of the site. 
        Secret key: The secret key variable is key for the security of the app. 

6. **Deploying the app** 

    - To the deploy the app, enter the deploy tab of your heroku app. 
    - Connect it to the relevant github repository. 
    - Select the branch which you would like to deploy. 
    - Once that is selcted, click the deploy button. 
    - This will deploy your api to heroku. 

## Credits.

---

The code used in this API was heavily inspired by the course content from Code Institute. In particular, the DRF API repository. Which can be found [here.](https://github.com/Code-Institute-Solutions/drf-api)