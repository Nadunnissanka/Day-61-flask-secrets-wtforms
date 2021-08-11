from flask import Flask, render_template
from login_form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thesecretkey'
EMAIL = "admin@email.com"
PASSWORD = "12345678"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # <form_object>.<form_field>.data
        entered_email = str(form.email.data)
        entered_password = str(form.password.data)
        if entered_email == EMAIL and entered_password == PASSWORD:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
