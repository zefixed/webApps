from flask import Flask, render_template, make_response, request
import re

app = Flask(__name__)

application = app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/url')
def url():
    return render_template('url.html', title="Параметры URL", )


@app.route('/headers')
def headers():
    return render_template('headers.html', title="Заголовки")


@app.route('/cookies')
def cookies():
    resp = make_response(render_template('cookies.html', title="Куки"))
    if 'user' in request.cookies:
        resp.delete_cookie('user')
    else:
        resp.set_cookie('user', 'admin')
    return resp


@app.route('/forms', methods=['GET', 'POST'])
def forms():
    # if request.method == "POST"
    return render_template('forms.html', title="Параметры формы")


@app.route('/calc')
def calc():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    operator = request.args.get('operator')

    result = 0
    if operator == "+":
        result = a+b
    elif operator == "-":
        result = a-b
    elif operator == "*":
        result = a*b
    elif operator == "/":
        result = a/b

    return render_template('calc.html', title="Калькулятор", result=result)


@app.route("/phoneNumber", methods=["POST", "GET"])
def phoneNumber():
    if request.method == 'POST':
        phone = request.form["phone"]

        phoneNumbers = re.findall("\d{1}", phone)
        if not phoneNumbers:
            phoneNumbers.append("")

        error = ""
        if not all([symbol in [" ", "(", ")", "-", ".", "+", *list(map(str, list(range(10))))] for symbol in phone]):
            error = "Недопустимый ввод. В номере телефона встречаются недопустимые символы."
        elif phoneNumbers[0] in ["7", "8"] and len(phoneNumbers) != 11:
            error = "Недопустимый ввод. Неверное количество цифр."
        elif phoneNumbers[0] not in ["7", "8"] and len(phoneNumbers) != 10:
            error = "Недопустимый ввод. Неверное количество цифр."

        if error:
            return render_template("phoneNumber.html", title="Проверка номера телефона", phone=error)

        if len(phoneNumbers) == 10:
            phoneNumbers.insert(0, "8")

        return render_template("phoneNumber.html", title="Проверка номера телефона", phone="8-{1}{2}{3}-{4}{5}{6}-{7}{8}-{9}{10}".format(*phoneNumbers))
    else:
        return render_template("phoneNumber.html", title="Проверка номера телефона")
