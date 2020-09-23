# SQL Twitterclone Database
## What this script does:
This is a Python script that creates a SQLite database and uses the <a href='https://github.com/lk-geimfari/mimesis'>Mimesis</a> Data Generator to populate the database.


## How it works:

If the database hasn't been created then the first part of the script will handle that.

### Each table in the database will be as follows and will have these fields in them:

* twitteruser- this has fields of id, username, password, and display name

* tweet- this has fields of id, tweet, and twitter user

* notification- this has fields of id, tweet, and receiver

### Afterwords it will run 3 different for loops:

* The first loop creates 500 randomly generated users and inserts them into the twitteruser table

* The second loop creates 1000 tweets randomly by the 500 users generated in the first loop and inserts them into tweet table

* Finally the last loop generates 200 notifications from 1 of 2 users chosen at random and chooses 200 random users to be notified

## How to get started:

### Dependencies required for this project 
* Python 3.8+

* SQLite

* <a href='https://github.com/lk-geimfari/mimesis'>Mimesis</a>

* Linux-based or Mac operating system

* Bash or Zsh shell

Once you have these dependencies satisfied Fork and Clone the repo.

In order to run the script simply type this command in your Vs Code terminal:

```
python twitterdata.py

```
Thanks and make sure to go check out <a href='https://github.com/lk-geimfari/mimesis'>Mimesis</a> to see what else you can do.

