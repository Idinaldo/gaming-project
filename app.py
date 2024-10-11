from flask import *
from entidades import *

app = Flask(__name__)

games = []

@app.route('/')
def index():
    return render_template('index.html', games=games)

@app.route('/criar', methods=['POST']) 
def create():
    current_game = Game()
    current_game.setNome(request.form['nome'])
    current_game.setDev(request.form['desenvolvedora'])
    current_game.setDesc(request.form['descricao'])
    games.append(current_game)
    return redirect('/')

@app.route('/alterar', methods=['POST']) # Rota /alterar
def update():
    old_name = request.form['old_name']
    new_name = request.form['new_name']
    #old_name_desen = request.form['nome antigo da desenvolvedora']
    new_dev = request.form['new_dev']
    new_desc = request.form['new_desc']
    for g in games:
        if g.getNome() == old_name:
            g.setNome(new_name)
            g.setDev(new_dev)
            g.setDesc(new_desc)
    return redirect('/')
    #elif old_name_desen in games:

@app.route('/apagar', methods=['POST']) # Rota /apagar
def delete():
    nome = request.form['nome']
    for g in games:
        if g.getNome() == nome:
            games.remove(g)
            return redirect('/')
    else:
        return "jogo não encontrado"
if __name__ == '__main__':
    app.run(debug=True)