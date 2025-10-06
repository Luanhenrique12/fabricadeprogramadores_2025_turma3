#from sqlalchemy import create_engine
#
#engine= create_engine('sqlite:///:memory:')
#connection= engine.connect()
#print("Hello, SQLALchemy!")
#connection.close()

import datetime
from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload
from dotenv import load_dotenv, dotenv_values
import os
load_dotenv()

variaveis_de_ambiente = dotenv_values()

DATABASE_URL = variaveis_de_ambiente['DATABASE_URL']
#DATABASE_URL = os.environ.get('DATABASE_URL')


engine = create_engine(DATABASE_URL)

senssionlocal = sessionmaker(autocommit=False , autoflush=False, bind=engine)

Base= declarative_base()

usuario_endereco_associacao=Table(
    "usuario_endereco_associacao",
    Base.metadata,
    Column("usuario_id", Integer, ForeignKey("usuarios.id"), primary_key=True),
    Column("endereco_id", Integer, ForeignKey("enderecos.id"), primary_key=True)
)


class Usuario(Base):
    __tablename__ = "usuarios"  

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=False)
    senha_hash = Column(String(255), nullable=False)
    criado_em = Column(DateTime(timezone=True), default=datetime.datetime.now)

    notas = relationship("Notas", back_populates="autor")
    usuario_endereco = relationship("Endereco",
        secondary=usuario_endereco_associacao,
        back_populates="moradores"
    )
class Notas(Base):
    __tablename__ = "notas" 

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    titulo = Column(String(255), nullable=False)
    conteudo= Column(Text)
    criado_em= Column(DateTime(timezone=True),default = datetime.datetime.now)
    modificado_em = Column(DateTime(timezone=True), default=datetime.datetime.now)
   
    autor = relationship("Usuario", back_populates="notas")



class Endereco(Base):
    __tablename__ = "enderecos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rua= Column(String(500), nullable=False)
    numero= Column(Integer)
    cep= Column(String)

    moradores = relationship(
        "Usuario",
        secondary=usuario_endereco_associacao,
        back_populates="usuario_endereco"
       
   )

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso (se não existiam).")