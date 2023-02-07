# база данных
# sql язык базы данных
# СУБД - система управления базами данных


# crud create read update delete


import sqlite3

db = sqlite3.connect('test.db')

c = db.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS user(
name text,
title text,
view integer,
nick text
)
""");
# create
c.execute("INSERT INTO user VALUES('Самат','самата нет',10,'Samat')")
# update
c.execute("UPDATE user SET name = 'Даша' WHERE rowid=1")
c.execute("UPDATE user SET name = 'Даша' WHERE name='Самат'")
c.execute("UPDATE user SET name = 'x' WHERE rowid > 3")
c.execute("UPDATE user SET view = 11 WHERE view = 10")
c.execute("UPDATE user SET nick = 'proger' WHERE rowid=3 ")
# delete
c.execute("DELETE FROM user WHERE rowid <> 3")
# c.execute("DELETE FROM user WHERE rowid != 5")


c.execute("SELECT rowid,* FROM user")  # read
item = c.fetchall()
for el in item:
    print(el)

db.commit()
db.close()
