from flask import Flask, request, jsonify, render_template, json
from main import atualizar_nota, login_de_usuario, criar_novo_usuario_e_nota, deletar_usuario, ler_dados
from main import Usuario, Notas

app = Flask(__name__)

# -------------------------------
# Rota principal (cadastro)
# -------------------------------
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        try:
            data = request.get_json()

            user = Usuario(
                nome=data.get("usuario"),
                email=data.get("email"),
                senha_hash=data.get("senha")
            )
            note = Notas(
                titulo=data.get("titulo"),
                conteudo=data.get("nota")
            )

            criar_novo_usuario_e_nota(user, note)

            return jsonify({"success": True, "redirect": "/login"}), 201

        except Exception as e:
            print("Erro ao registrar usuário:", e)
            return jsonify({"success": False, "error": "Erro ao se registrar."}), 500


# -------------------------------
# API - lista de usuários
# -------------------------------
@app.route("/api/users", methods=["GET"])
def api_users():
    try:
        data = ler_dados()
        return jsonify({"success": True, "data": data}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# -------------------------------
# Área do aluno
# -------------------------------
@app.route("/home", methods=["GET"])
def home():
    return render_template("area_aluno.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            data = request.get_json()
            user = Usuario(email=data.get("email"), senha_hash=data.get("senha"))

            usr = login_de_usuario(user)

            if usr:
                return jsonify({"success": True, "redirect": "/home"}), 200
            else:
                return jsonify({"success": False, "error": "Usuário ou senha inválidos."}), 401

        except Exception as e:
            print("Erro no login:", e)
            return jsonify({"success": False, "error": "Erro no servidor."}), 500
    else:
        return render_template("login.html")



@app.route("/remover/usuario/<id>", methods=['GET', 'POST'])
def remover_usuarios(id):
    if request.method == "POST":
        try:
            deletar_usuario(id_usuario=id)
            app.logger.info(f"Usuário de ID {id} foi removido com sucesso!")
            return jsonify({"success": True, "message": f"Usuário {id} removido com sucesso."}), 200

        except Exception as e:
            app.logger.error(f"Erro na remoção do usuário {id}: {e}")
            return jsonify({"success": False, "error": str(e)}), 500

    else:
        return render_template('remover.html')



if __name__ == "__main__":
    app.run(debug=True)