from flask import (Flask, render_template, flash, redirect, url_for)
from flask_mail import Message, Mail
import json

import forms

mail = Mail()

app = Flask(__name__)
app.secret_key = 'aopddoawijdoawijd@EW@D2doijd'

with open('./local/auth.json') as data_file:
    data = json.load(data_file)
    app.config["MAIL_USERNAME"] = data["email"]
    app.config["MAIL_PASSWORD"] = data["password"]

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True

mail.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/videos')
def videos():
    return render_template("videos.html")


@app.route('/faq')
def faq():
    return render_template("faq.html")


@app.route('/testimonials')
def testimonials():
    return render_template("testimonials.html")


@app.route('/photos')
def photos():
    return render_template("photos.html")


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = forms.ContactForm()
    if form.validate_on_submit():
        flash("Yay, you registered!", "success")
        msg = Message(form.name.data, sender='krutonslol@gmail.com', recipients=['crutonslol@gmail.com'])
        msg.body = """
        From: {}, {};
        {}
        """.format(form.name.data, form.email.data, form.message.data)
        mail.send(msg)
        return redirect(url_for('index'))
    return render_template("contact.html", form=form)


if __name__ == '__main__':
    app.run()
