from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão com SQLite estabelecida.")

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

## ADICIONA USUARIO BD
# novo_usuario = Usuario(nome='Matheus', idade=28)
# session.add(novo_usuario)
# session.commit()
# print("Usuário inserido com sucesso.")

## REALIZA CONSULTA (SELECT) DO BD FILTRANDO PELA COLUNA NOME
usuario = session.query(Usuario).filter_by(nome='Matheus').first()
print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")