# -*- coding: utf-8 -*-

# import the sqlite3 library
import sqlite3
# create a new database if the database doesn't already exist
with sqlite3.connect("agenda.db") as connection:
    # get a cursor object used to execute SQL commands
    c = connection.cursor()
    # total posts
    c.execute("SELECT COUNT(agenda) FROM posts")
    total = c.fetchone()[0]
    print "Total Contactos: ", total
    # query posts
    c.execute("SELECT * FROM agenda ORDER BY Apellidos")
    # fetchall() retrieves all records from the query
    posts = c.fetchall()
    print "\nContactos agenda\n==========="
    # output the rows to the screen, row by row
    for p in posts:
        print "Nombre: ", p[0]
        print "Apellidos: ", p[1]
        print "Email: ", p[2]
        print
