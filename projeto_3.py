import sqlite3

try:
    con = sqlite3.connect("desafio.db")
    cur = con.cursor()

    cur.execute("DELETE FROM pessoa")
    #cur.execute("CREATE TABLE  pessoa(id, nome, sala)")
    cur.execute("INSERT INTO pessoa VALUES ('1', 'Ana', 'Recepção' ) ")
    cur.execute("INSERT INTO pessoa VALUES ('2', 'Bruno', 'Financeiro' ) ")
    cur.execute("INSERT INTO pessoa VALUES ('3', 'Carla', 'Depósito' ) ")
    
    con.commit()

  
    cur.execute("SELECT * FROM pessoa")
    responsavel = cur.fetchone()
    

    if responsavel: 
        print("Quem está com a chave do Depósito: {responsavel[0]}")

    else:
        print("Nenhum responsável encontrado para o Depósito.")

    con.commit()
except sqlite3.Error as e:
    print("erro:", e)

