from tabelas import senssionlocal, Usuario, Notas



db = senssionlocal()

def criar_novo_usuario_e_nota(novo_usuario: Usuario, nova_nota: Notas):
   


    

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    print(f"Usuário '{novo_usuario.nome}' criado com ID: {novo_usuario.id}")

  
    
    note = Notas(
        id_usuario= novo_usuario.id, 
        titulo= nova_nota.titulo,
        conteudo= nova_nota.conteudo
        )
    db.add(note)
    db.commit()
    print(f"Nota '{nova_nota.titulo}' criada para {novo_usuario.nome}.")

def ler_dados():
    user =  db.query(Usuario).all()

    if user:
        
        for notas in user.notas:
            print(f" -Título: {notas.titulo} (ID: {Notas.id} ")
        return user
    else:
        print("Usuario(a) não esncontrado.")

def atualizar_nota(id_nota: int, titulo: str, conteudo: str):
    nota_para_editar = db.query(Notas).filter(Notas.id == id_nota).first()

    if nota_para_editar:
       
       
        nota_para_editar.titulo = titulo
        nota_para_editar.conteudo = conteudo
       
        db.commit()
        
    else:
        print("Nota com ID %d não encontrada." % id_nota)


def deletar_usuario(id_usuario: int):
    usuario_deletado = db.query(Usuario).filter(Usuario.id == id_usuario).first()

    if usuario_deletado:

        db.delete(usuario_deletado)
        db.commit()
        print(f"Usuario:  '{usuario_deletado.nome}' removido com sucesso!")
    
    else:
        print("Usuario com ID %d não encontrato." % id_usuario)


