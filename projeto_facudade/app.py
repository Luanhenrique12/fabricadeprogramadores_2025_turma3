from flask import Flask, request, jsonify, render_template, json
from main import ler_dados, atualizar_nota, criar_novo_usuario_e_nota, deletar_usuario
from tabelas import Usuario, Notas

app = Flask(__name__)

# --- Página inicial (cadastro) ---
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    elif request.method == "POST":
        try:
            data = request.get_data()
            usuario_e_nota = json.loads(data)

            user = Usuario(
                nome=usuario_e_nota["usuario"],
                email=usuario_e_nota["email"],
                senha_hash=usuario_e_nota["senha"]
            )

            note = Notas(
                titulo=usuario_e_nota["titulo"],
                conteudo=usuario_e_nota["nota"]
            )

            criar_novo_usuario_e_nota(user, note)

            return jsonify({"success": True, "message": "Usuário e nota criados com sucesso!"}), 201
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 400
    
    else:
        return jsonify({"error": "Página não encontrada!"}), 404


# --- Página de listagem (HTML) ---
@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")


# --- API para retornar usuários e notas ---
@app.route("/api/users", methods=["GET"])
def api_users():
    try:
        data = ler_dados()
        return jsonify({"success": True, "data": data}), 200 
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)