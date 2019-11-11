from flask import Flask, render_template, request, redirect, make_response
from models import Comment, db, dobi_bazo

app = Flask(__name__)


@app.route("/")
def index():
    name = request.cookies.get("name")

    objave = dobi_bazo().query(Comment).all()

    print("stevilo objav:", len(objave))

    return render_template("aaa.html", name=name, objave=objave)


@app.route("/objava", methods=["POST"])
def naredi_objavo():
    name = request.cookies.get("name")

    vsebina = request.form.get("vsebina")

    baza = dobi_bazo()

    objava = Comment(avtor=name, vsebina=vsebina)
    baza.add(objava)
    baza.commit()

    return redirect("/")


@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")

    response = make_response(redirect("/"))
    response.set_cookie("name", name)
    return response


if __name__ == '__main__':
    app.run()
