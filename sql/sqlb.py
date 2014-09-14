#!/usr/bin/env python
import sqlite3
with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO population VALUES('Newark','NY', 1000)")
    cursor.execute("INSERT INTO population VALUES('SD','CA',20000)")
