# -*- coding: utf-8 -*-

import Cookie

# set http header
print "Content-Type: text/html"

# unset the Cookie
thiscookie = Cookie.SimpleCookie()
thiscookie['logged_in'] = ''
print thiscookie

# redirect to login page
print "Refresh: 0; url=../login.html\n"

print #cerrar cabecera