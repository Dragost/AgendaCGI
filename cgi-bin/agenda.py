# -*- coding: utf-8 -*-


# import the sqlite3 library
import sqlite3
import Cookie
import os #para leer variables de entorno
import cgi
import cgitb
cgitb.enable()

# set http header
print "Content-Type: text/html"

logged_in = False
# check if the user is authenticated through a Cookie named 'logged_in'
thiscookie = Cookie.SimpleCookie()

if os.environ.has_key('HTTP_COOKIE'):
    thiscookie.load(os.environ['HTTP_COOKIE'])
    if 'logged_in' in thiscookie:
        logged_in = bool(thiscookie['logged_in'].value)

# redirect to login page if not authenticated
if not logged_in:
    print "Refresh: 0; url=/login.html"

print #final cabecera

# get post data
form = cgi.FieldStorage()
Nombre = form.getfirst('Nombre', '')
Apellidos = form.getfirst('Apellidos', '')
Email = form.getfirst('Email', '')

# create a new database if the database doesn't already exist
with sqlite3.connect("agenda.db") as connection:
    # get a cursor object used to execute SQL commands
    c = connection.cursor()
    
    # insert data to db if not empty
    if Nombre != "" and Apellidos != "" and Email !="":
        # insert data into table
        c.execute('INSERT INTO agenda VALUES(?, ?, ?)', (Nombre, Apellidos, Email))

    
    # total posts
    c.execute("SELECT COUNT(Email) FROM agenda")
    total = c.fetchone()[0]
    
    # query posts
    c.execute("SELECT * FROM agenda ORDER BY Apellidos")
    # fetchall() retrieves all records from the query
    posts = c.fetchall()
    
    
    
    tabla_datos = ''' <table border=1> 
        <tr> <th>Nombre</th> <th>Apellidos</th> <th>Email</th></tr> '''
    
    # output the rows to the screen, row by row
    for p in posts: 
        linea = '<tr> <td>%s</td> <td>%s</td> <td>%s</td></tr> ' % (p[0], p[1], p[2])
        tabla_datos += linea
       
    tabla_datos += '</table>'
    
    
    
    #imprimimos el total y la tabla de datos
    doc_html = '''
        <html>
            <head>
                <title>blog</title>
                <meta charset="utf-8">
                <link href="../estilos.css" rel="stylesheet">
            </head>
            <body>
               <h1><center>AGENDA</center></h1>
               <h2>Contactos</h2>
               <p>Total Post: {total}</p>
              {tabla}
               
                <div class="form">
                    <form method="POST" action="agenda.py">
                        <h2>Añadir un nuevo contacto:</h2>
                        <p>Nombre: <input type="text" name="Nombre" value=""></p>
                        <p>Apellidos: <input type="text" name="Apellidos" value=""></p>
                        <p>Email: <input type="text" name="Email" value=""></p>
                        <input type="submit" value="Enviar">
                    </form>
                     <form method="POST" action="logout.py">
+                        <input type="submit" value="Logout">
+                    </form>
                </div>

               
               
            </body>
        </html>'''

    print doc_html.format(total=total, tabla=tabla_datos)