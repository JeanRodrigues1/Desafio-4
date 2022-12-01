from flask import Flask, request, Blueprint, render_template, url_for
from .database import inserir_dados, buscarinfo

routes = Blueprint('routes',__name__)


@routes.route("/")
def i():
    return render_template("home.html")

@routes.route("/home")
def home():
    return render_template("home.html")
    
@routes.route("/info")
def info():
    info = buscarinfo()
    if len(info) > 0:
        return render_template("info.html", info = buscarinfo())
    else: 
        return render_template("info.html")

@routes.route("/contato",methods = ["POST","GET"])
def contato():
    if request.method == "POST":
        email = request.form.get("email")
        assunto = request.form.get("assunto")
        descricao = request.form.get("desc")
        inserir_dados(email, assunto, descricao)
        return render_template("contato.html")
    return render_template("contato.html")

@routes.route("/quemSomos")
def who():
    return render_template("quemSomos.html")