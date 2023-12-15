from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def Hello_word():  # put application's code here
    return render_template("Header.html")

@app.route('/cadastro')
def cadastro():
    return render_template("Cadastro.html")

@app.route('/curso')
def curso():
    return render_template("Curso.html")

@app.route('/escrita')
def escrita():
    return render_template("Escrita.html")
@app.route('/localizacao')
def localizacao():
    return render_template("Localizacao.html")

@app.route('/portifolio')
def portifolio():
    return render_template("Portifolio.html")

@app.route('/contato')
def contato():
    return render_template("Contato.html")


if __name__ == '__main__':
    app.run()
