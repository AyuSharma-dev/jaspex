from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from JsonToApexGen import getApexCode
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


class AForm(FlaskForm):
    apexCode = TextAreaField('Text', render_kw={"rows": 30, "cols": 80})
    jsonCode = TextAreaField('Text', render_kw={"rows": 30, "cols": 80})


@app.route('/', methods=['POST', 'GET'])
def home():
    form = AForm()
    if form.validate_on_submit():
        if str(form.jsonCode.data) != '':
            form.apexCode.data = getApexCode(str(form.jsonCode.data))
        else:
            form.apexCode.data = ''
    return render_template("home.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
