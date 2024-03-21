from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/somar", methods=["POST"])
def somar():
    if request.form.get("n1") == "" or request.form.get("n2") == "":
        return render_template("index.html", resultado = "Tem de preencher todos os campos")


    n1 = int(request.form.get("n1"))
    n2 = int(request.form.get("n2"))
    soma = n1 + n2
    return render_template("index.html", resultado = soma)


app.run(debug=True)