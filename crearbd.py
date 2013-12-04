# -*- coding: utf-8 -*-

import sqlite3
# create a new database if the database doesn't already exist
with sqlite3.connect("agenda.db") as connection:
    # get a cursor object used to execute SQL commands
    c = connection.cursor()
    # create the table
    c.execute("""CREATE TABLE agenda(Nombre TEXT, Apellidos TEXT, Email TEXT)""")
    # insert multiple records using a tuple
    agenda = [
        ("Manolo", "Garcia Sanchez", "manologs@gmail.com"),
        ("Lucia", "Grecia Ritere", "luciagr@gmail.com"),
        ("Marta", "Pered Rigaldo", "martapr@gmail.com"),
    ]
    # insert data into table
    c.executemany('INSERT INTO agenda VALUES(? )', agenda)
