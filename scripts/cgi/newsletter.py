#!/usr/bin/env python3
import os, sys, inspect
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(os.path.dirname(currentdir))

# Make sure this is not in the webserver root
# Activate the virtualenv
activate_this = os.path.join(rootdir, "virtualenv/bin/activate_this.py")
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this} )

sys.path.append(os.path.join(rootdir, "scripts/"))

from wsgiref.handlers import CGIHandler
from subscribe import app
import os

os.environ['SCRIPT_NAME'] = '/newsletter-subscribe'
CGIHandler().run(app)
