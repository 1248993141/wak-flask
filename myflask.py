from flask import Flask , render_template,request
app=Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("pwd")
    if username =="alex" and password =="123":
        return "成功"
    else:
        return render_template("login.html", msg="登录失败")


if __name__ == '__main__':
    app.run()