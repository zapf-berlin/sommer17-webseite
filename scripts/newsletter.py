#!/usr/bin/python3

import cgi
import mailmanclient

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
rootdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0,rootdir)
from newsletterConfig import *

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
mail = form.getvalue('mail')
password  = form.getvalue('password')

if(password != newsletterPassword):
    print("Content-type:text/html\r\n\r\n")
    print("<head>")
    print("<title>Sommer17 Newsletter Anmeldung - Fehler</title>")
    print("</head>")
    print("<body>")
    print("Das eingegebene Passwort ist falsch. Bitte versuche es erneut!<br>")
    print("Solltest du vermuten, dass ein technischer Fehler aufgetreten ist, ")
    print("sende bitte eine Mail an ")
    print('<a href="mailto:it@zapf.in-berlin.de">it@zapf.in-berlin.de</a>.<br><br>')
    print('<a href="http://zapf.in/berlin">Zur&uuml;ck zur Website</a>')
    print("</body>")
    print("</html>")
    sys.exit(0)

# Create mailmanclient and add subscription request
client = mailmanclient.Client('http://localhost:8001/3.0', RESTadminUser,
          RESTadminPassword)
newsletterList = client.get_list('sommer17-newsletter@zapf.in')
newsletterList.subscribe(mail, pre_approved=True)

print("Content-type:text/html\r\n\r\n")
print("<head>")
print("<title>Sommer17 Newsletter Anmeldung - Erfolgreich</title>")
print("</head>")
print("<body>")
print("Um die Anmeldung abzuschließen, folge bitte den Anweisungen")
print("in der Mail, die an die angegebene Adresse verschickt wurde<br>")
print("Solltest du vermuten, dass ein technischer Fehler aufgetreten ist, ")
print("sende bitte eine Mail an ")
print('<a href="mailto:it@zapf.in-berlin.de">it@zapf.in-berlin.de</a>.<br><br>')
print('<a href="http://zapf.in/berlin">Zur&uuml;ck zur Website</a>')
print("</body>")
print("</html>")
