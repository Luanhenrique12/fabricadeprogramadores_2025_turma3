from flask import Flask, request, jsonify,  render_template, json, redirect, url_for
from main import atualizar_nota, login_de_usuario
from main import criar_novo_usuario_e_nota
from main import deletar_usuario, ler_dados
from main import Usuario, Notas
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = request.get_data() 
        usuario_e_nota = json.loads(data)

        user = Usuario(
                        nome=usuario_e_nota["usuario"],
                        email=usuario_e_nota["email"],
                        senha_hash=usuario_e_nota["senha"] )
        note = Notas( 
                        titulo=usuario_e_nota["titulo"],
                        conteudo=usuario_e_nota["nota"])
        
        app.logger.info("Usuario esta criando nota e usuario associado.")
      
        criar_novo_usuario_e_nota(user, note)
        return jsonify({"msg": "Usuario e nota criados com sucesso!"}),201
    
    else:
        return jsonify({'error': 'pagina não encontrada!'}), 404
    
@app.route("/api/users", methods=["GET"])
def api_users():
        try:
            data = ler_dados()
            return jsonify({"sucess": True, "data": data}),200
        except Exception as e:
            return jsonify({"sucess": False, "error": str(e)}),500

@app.route("/home", methods=["GET"])
def home():
        return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_data()
        usuario = json.loads(data)
        user = Usuario(email=usuario["email"], senha_hash=usuario["senha_hash"])
        try:
            usr=login_de_usuario(user)
            app.logger.info("Usuario de email: %s logado!" % usuario["email"])
            return redirect(url_for("home", data=usr))
        except Exception as e:
            app.logger.error("Erro no servidor:", str(e))
            return jsonify({"sucess": False, "error": str(e)}),500
    else:
        return render_template("login.html")

if __name__=="main_":
    app.run()