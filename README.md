# Stackoverflow-lite-challenge-3
Integrating Api with database

[![Build Status](https://travis-ci.org/kizzanaome/Challenge3-Stackoverflow-lite.svg?branch=develop)](https://travis-ci.org/kizzanaome/Challenge3-Stackoverflow-lite)
[![Coverage Status](https://coveralls.io/repos/github/kizzanaome/Level-up/badge.svg?branch=develop)](https://coveralls.io/github/kizzanaome/Level-up?branch=develop)
# -Stack-Overflow-lite


- This branch contains API endpoints for the above application intergrated with a database

# Features
 - Users can create an account and log in.
 - Users can post questions
 - Users can delete the questions they post.  
 - Users can post answers.
 - Users can view the answers to questions.  
 - Users can accept an answer out of all the answers to his/her question as the preferred  answer.  

- This branch contains API endpoints for the above application intergrated with a database
## Installation
**Clone this _Repository_**
```
https://github.com/kizzanaome/Challenge3-Stackoverflow-lite/tree/develop
```
**Create virtual environment and install it**
```
$ virtualenv --python=python3 venv
$ source /venv/bin/activate
```
**Install all the necessary _dependencies_ by**
```
$ pip install -r requirements.txt
$ Install PostgreSQL
$ CREATE DATABASE stackover flow
$ CREATE TABLE users
$ CREATE TABLE questions
$ CREATE TABLE replies

```
**Run _app_ by**

```
Run the server At the terminal or console type
$ Python run.py
```
## Versioning
```
This API is versioned using url versioning starting, with the letter 'v'
This is version one"v1" of the API
```
## End Points
|           End Point                      |     Functionality     |   Access   | Requirements|
|   -------------------------------------- |-----------------------|------------|-------------|
|     POST   api/v1/users/signup           | Registers a new user  |   PUBLIC   | email, password, username
|     POST api/v1/question/user_id         | Post User Questions   |   PRIVATE  | description, title, subject, user_id |
|     GET  api/v1/question/user_id/qtn_id  | Get one user Question |   PRIVATE  |user_id, question_id
|     GET  api/v1/questions/user_id        | Get users Question    |    PRIVATE  |user_id
|     PUT api/v1/question/user_id/qtn_id   | Edit user Question    |   PRIVATE  |user_id, question_id
|    DELETE api/v1/question/user_id/qtn_id | Delete user Question  |   PRIVATE  |user_id, question_id
|    POST   api/v1/users/login             | Login User            |   PUBLIC   |Email, password
|POST api/v1/question/qtnid/answer         | Post areply for a question|PRIVATE |user_id, question_id
|DELETE api/v1/question/qtnid/answer/reply_id|Delete a user reply  | PRIVATE    |user_id, qtn_id, reply
|PUT api/v1/question/qtnid/answer/reply_id|Update user reply       |PRIVATE |user_id, reply_id, qtn_id

