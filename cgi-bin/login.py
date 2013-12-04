# -*- coding: utf-8 -*-

import Cookie
import hashlib
import cgi
import cgitb
cgitb.enable()


# get post data
form = cgi.FieldStorage()
post_user = form.getfirst('user', '')
post_password = form.getfirst('password', '')

# password abierta --> cifrada
passwd = hashlib.sha1()
passwd.update(post_password)
post_password = passwd.hexdigest()  # password cifrada

# define username and password
username = "admin"
#pass cifrada, explicado arriba
password = "d033e22ae348aeb5660fc2140aec35850c4da997"  

# set http header
print "Content-Type: text/html"

if post_user == username and post_password == password: 
    #añadimos cookie para recordar user (es muy inseguro, no se usa para autentificaciones!!!)
    thiscookie = Cookie.SimpleCookie()
    thiscookie['logged_in'] = True
    print thiscookie

    # if authentication is ok
    print "Refresh: 0; url=/cgi-bin/agenda.py\n"
    print
else:
    # if authentication failed
    print "Refresh: 0; url=login.html\n"
    print
    
    
print #final cabecera
