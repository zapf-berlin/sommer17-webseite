import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(currentdir)

# Make sure this is not in the webserver root
# Activate the virtualenv
activate_this = os.path.join(rootdir, "virtualenv/bin/activate_this.py")
with open(activate_this) as f:
        exec(f.read(), {'__file__': activate_this} )

from flask import Flask, request, redirect
import newsletterConfig
import mailmanclient
from validate_email_address import validate_email

app = Flask(__name__)
app.config.from_object(newsletterConfig)

@app.route("/berlin/newsletter/newsletter-subscribe", methods=['POST'])
def newsletter_subscribe():
    password=request.form['password']
    email=request.form['mail']
    if password == app.config["NEWSLETTER_PASSWORD"]:
        if not validate_email(email, verify=True):
            app.logger.warn("Email verification failed for '%s'" % email)
            return redirect(app.config["NEWSLETTER_VERIFY_FAILED_PATH"])

        app.logger.info("Subscribing %s" % email)

        if not app.debug:
            client = mailmanclient.Client(
                    app.config["MAILMAN_REST_URL"],
                    app.config["MAILMAN_REST_USER"],
                    app.config["MAILMAN_REST_PASS"])
            newsletterList = client.get_list(app.config["NEWSLETTER_LIST_NAME"])

            try:
                newsletterList.get_member(email)
            except ValueError:
                newsletterList.subscribe(email, pre_approved=True)
            else:
                app.logger.warn("Already subscribed: %s", email)
                return redirect(app.config["NEWSLETTER_ALREADY_SUBSCRIBED_PATH"])

        return redirect(app.config["NEWSLETTER_SUCCESS_PATH"])
    else:
        return redirect(app.config["NEWSLETTER_FAIL_PATH"])

