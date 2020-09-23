import sqlite3
import random
from mimesis import Person, Text
text = Text('en')
person = Person('en')
conn = sqlite3.connect('twitterdata.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS twitteruser(id SERIAL NOT NULL PRIMARY KEY,
          username VARCHAR(150)NOT NULL, password VARCHAR(128)NOT NULL,
          display_name VARCHAR(150)NOT NULL)""")
c.execute("""CREATE TABLE IF NOT EXISTS tweet(id SERIAL NOT NULL PRIMARY KEY,
          tweet VARCHAR(600)NOT NULL,
          twitter_user INT REFERENCES twitteruser ON DELETE CASCADE NOT NULL)""")
c.execute("""CREATE TABLE IF NOT EXISTS notifications(id SERIAL NOT NULL PRIMARY KEY,
          tweet REFERENCES tweet_table ON DELETE CASCADE NOT NULL,
          receiver INT REFERENCES twitteruser ON DELETE CASCADE NOT NULL)""")


conn.commit()

for new_user in range(500):
    c.execute('INSERT INTO twitteruser(id, username, password, display_name) VALUES(?,?,?,?)',
            [new_user + 1, person.username(), person.password(), person.full_name()],)
    

for new_tweet in range(1000):
    c.execute('INSERT INTO tweet(id, tweet, twitter_user) VALUES(?,?,(SELECT id FROM twitteruser ORDER BY RANDOM() LIMIT 1001))',
            [new_tweet + 1, text.text(quantity=1)])


for new_notification in range(200):
    rand_user = random.sample(range(1,500), 2)
    rand_sender = random.choice(rand_user)
    c.execute('INSERT INTO notifications(id, tweet, receiver) VALUES(?,?,(SELECT id FROM twitteruser ORDER BY RANDOM() LIMIT 201) )',
            [new_notification + 1, rand_sender])

conn.commit()
conn.close()