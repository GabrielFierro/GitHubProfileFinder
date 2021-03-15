from flask import Flask, render_template, request, redirect, url_for
from requestAPI import Consulta
import requests
import forms

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    input_form = forms.InputForm(request.form)

    if request.method == 'POST':
        username = input_form.username.data
        return redirect(url_for('user', name=username))

    return render_template('base/base.html', form=input_form)


@app.route('/user/<name>')
def user(name):
    form = forms.InputForm(request.form)
    response = Consulta.getResponse(name)

    if response.status_code == 200:
        data = Consulta.getDatos(response.json())
        return render_template("profile.html", form=form, data=data)
    else:
        return redirect(url_for('error'))


@app.route('/error')
def error():
    form = forms.InputForm(request.form)
    return render_template('error.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
