from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date

app = Flask(__name__)
app.secret_key = "presente_mae_2026"

SENHA = "GoldenSurprise!19"
DATA_REVELACAO = date(2026, 11, 19)

def verificar_data():
    hoje = date.today()
    return hoje >= DATA_REVELACAO

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/presente")
def presente():
    return render_template("presente.html")

@app.route("/verificar")
def verificar():
    if verificar_data():
        return redirect(url_for("senha"))
    return redirect(url_for("contagem"))

@app.route("/contagem")
def contagem():
    if verificar_data():
        return redirect(url_for("senha"))
    return render_template("contagem.html")

@app.route("/senha", methods=["GET", "POST"])
def senha():

    if not verificar_data():
        return redirect(url_for("contagem"))

    erro = None

    if request.method == "POST":

        senha_digitada = request.form.get("senha", "")

        if senha_digitada == SENHA:
            session["liberado"] = True
            return redirect(url_for("revelacao"))

        erro = "Senha incorreta. Tente novamente!"

    return render_template("senha.html", erro=erro)

@app.route("/revelacao")
def revelacao():
    if not verificar_data():
        return redirect(url_for("contagem"))

    if not session.get("liberado"):
        return redirect(url_for("senha"))

    return render_template("revelacao.html")

if __name__ == "__main__":
    app.run(debug=True)
