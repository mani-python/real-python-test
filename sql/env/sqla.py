#!/usr/bin/env python
import sqllite3

conn = sqllite3.connect("new.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE population (city TEXT,state TEXT, population INT)""")
conn.close()
