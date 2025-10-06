from tabelas import senssionlocal, Usuario, Notas, joinedload

db = senssionlocal()

def criar_novo_usuario_e_nota(novo_usuario: Usuario, nova_nota: Notas):
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    print(f"Usuário '{novo_usuario.nome}' criado com ID: {novo_usuario.id}")

    note = Notas(
        id_usuario=novo_usuario.id,
        titulo=nova_nota.titulo,
        conteudo=nova_nota.conteudo
    )
    db.add(note)
    db.commit()


def atualizar_nota(id_nota: int, titulo: str, conteudo: str):
    nota_para_editar = db.query(Notas).filter(Notas.id == id_nota).first()

    if nota_para_editar:
        nota_para_editar.titulo = titulo
        nota_para_editar.conteudo = conteudo
        db.commit()
        print(f"Nota ID {id_nota} atualizada com sucesso.")
    else:
        print(f"Nota com ID {id_nota} não encontrada.")


def ler_dados():
    users = db.query(Usuario).options(joinedload(Usuario.notas)).all()

    resultado = []
    for u in users:
        notas = []
        for n in u.notas:
            notas.append({
                "id": n.id,
                "titulo": n.titulo,
                "conteudo": n.conteudo,
                "criado_em": n.criado_em
            })
        resultado.append({
            "id": u.id,
            "usuario": u.nome,
            "email": u.email,
            "criado_em": u.criado_em,
            "notas": notas
        })
    return resultado


def deletar_usuario(id_usuario: int):
    usuario_deletado = db.query(Usuario).filter(Usuario.id == id_usuario).first()

    if usuario_deletado:
        db.delete(usuario_deletado)
        db.commit()
        print(f"Usuário '{usuario_deletado.nome}' removido com sucesso!")
    else:
        print(f"Usuário com ID {id_usuario} não encontrado.")


def login_de_usuario(usr: Usuario):
    usuario_logado = db.query(Usuario).filter(
        Usuario.email == usr.email,
        Usuario.senha_hash == usr.senha_hash
    ).first()

    if usuario_logado:
        return [{
            "id": usuario_logado.id,
            "usuario": usuario_logado.nome,
            "email": usuario_logado.email,
            "criado_em": usuario_logado.criado_em
        }]
    else:
        print("Usuário não encontrado.")
        return []