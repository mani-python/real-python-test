#!/usr/bin/env python
import sqlite3
with sqlite3.connect("new.db") as conn:
     c = conn.cursor()
     cities = [
                ('Boston','MA',60000),
                ('cbe','TN',5000),
                ('cud','TN',7000)
              ]
     c.executemany('INSERT INTO population VALUES(?,?,?)',cities)

