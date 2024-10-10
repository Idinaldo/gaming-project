from flask import *

app = Flask(__name__)

games = []

@app.route('/')
def index():
    return render_template('index.html', games=games)

@app.route('/criar', methods=['POST']) 
def create():
    nome = request.form['nome']
    games.append(nome)
    return redirect('/')

@app.route('/alterar', methods=['POST']) # Rota /alterar
def update():
    old_name = request.form['old_name']
    new_name = request.form['new_name']
    if old_name in games:
        index = games.index(old_name)
        games[index] = new_name
    return redirect('/')

@app.route('/apagar', methods=['POST']) # Rota /apagar
def delete():
    nome = request.form['nome']
    if nome in games:
        games.remove(nome)
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)