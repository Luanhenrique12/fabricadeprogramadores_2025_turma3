from tabelas import senssionlocal, Usuario, Notas



db = senssionlocal()

def criar_novo_usuario_e_nota():
   


    novo_usuario = Usuario(
        nome="Luan Henrique ",
        email="luan.henrique@gmail.com",
        senha_hash="hash_super_seguro"
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    print(f"Usuário '{novo_usuario.nome}' criado com ID: {novo_usuario.id}")

  
    nova_nota = Notas(
        titulo="Minha Primeira Nota com SQLAlchemy",
        conteudo="É muito mais fácil do que escrever SQL na mão!",
        autor=novo_usuario
    )

    db.add(nova_nota)
    db.commit()
    print(f"Nota '{nova_nota.titulo}' criada para {novo_usuario.nome}.")

def ler_dados(nome):
    user =  db.query(Usuario).filter(Usuario.nome ==nome).first()

    if user:
        print(f"Enconteri o (a):{user.nome} (Email: {user.email})")
        print("Notas do user:")
        for notas in user.notas:
            print(f" -Título: {notas.titulo} (ID: {Notas.id} ")

    else:
        print("Usuario(a) não esncontrado.")

def atualizar_nota(id_nota):
    nota_para_editar = db.query(Notas).filter(Notas.id == id_nota).first()

    if nota_para_editar:
        print(f"Título original: '{nota_para_editar.titulo}'")

       
        nota_para_editar.titulo = "Lista de anotações ATUALIZADA!"

       
        db.commit()
        print(f"Título novo: '{nota_para_editar.titulo}'")
    else:
        print("Nota com ID %d não encontrada." % id_nota)
    

criar_novo_usuario_e_nota()
