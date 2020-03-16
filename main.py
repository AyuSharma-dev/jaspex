from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField
from JsonToApexGen import getApexCode, parseQuotedJson
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from json import loads

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


class AForm(FlaskForm):
    apexCode = TextAreaField('Text', render_kw={"rows": 30, "cols": 80})
    jsonCode = TextAreaField('Text', render_kw={"rows": 30, "cols": 80})
    exampleJson = TextAreaField('Text', render_kw={"rows": 15, "cols": 80})
    quoted = BooleanField()


@app.route('/', methods=['POST', 'GET'])
def home():
    form = AForm()
    if form.validate_on_submit():
        jsonBody = form.jsonCode.data
        quoted = form.quoted.data
        if str(jsonBody) != '':
            if(quoted):
                jsonBody = parseQuotedJson(str(jsonBody))
            form.apexCode.data = getApexCode(str(jsonBody))
        else:
            form.apexCode.data = ''
    return render_template("home.html", form=form)

@app.route('/quotedHelp', methods=['POST', 'GET'])
def quotedJsonHelp():
    form = AForm()
    form.exampleJson.data = '''


            \'{"menu": {'+
                '"id": "file",'+
                '"value": "File",'+
                '"popup": {'+
                  '"menuitem": ['+
                    '{"value": "New", "onclick": "CreateNewDoc()"},'+
                    '{"value": "Open", "onclick": "OpenDoc()"},'+
                    '{"value": "Close", "onclick": "CloseDoc()"}'+
                  ']'+
                '}'+
            '}}\'
            '''
    return render_template("tooltip.html", form=form)

@app.route('/api/generateApexAPI', methods=['POST', 'GET'])
def getApexFromAPI():
    jsonBody = request.json.get('Body')
    quotedJson = request.json.get('quoted')
    #print( "quotedJson==>"+quotedJson )
    if str(jsonBody) != '':
        if(quotedJson):
            jsonBody = parseQuotedJson(str(jsonBody))
        apexCode = getApexCode(str(jsonBody))
    return apexCode


if __name__ == '__main__':
    app.run(debug=False)
