from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []

@app.route("/")
def index():
    return render_template("index.html", tarefas=tarefas)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    tarefa = request.form.get("tarefa")

    if tarefa:
        tarefas.append(tarefa)

    return redirect("/")

@app.route("/remover/<int:id>")
def remover(id):
    if 0 <= id < len(tarefas):
        tarefas.pop(id)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)