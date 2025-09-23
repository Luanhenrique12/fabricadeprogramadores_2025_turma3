from flask import Flask, request, jsonify, render_template, json
from main import ler_dados, atualizar_nota, criar_novo_usuario_e_nota, deletar_usuario
from tabelas import Usuario, Notas
app=Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = request.get_data()
        usuario_e_nota = json.loads(data)
        print(usuario_e_nota)
        user = Usuario(usuario_e_nota["usuario"], 'email', 'senha')
        note = Notas(usuario_e_nota["nota"])
        criar_novo_usuario_e_nota(user, note)
        return jsonify({"msg": "Usuário e nota criados com sucesso!"})
    
if __name__=="__main__":
    app.run()