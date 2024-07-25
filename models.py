from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recurso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(500), nullable=True)

class Orientacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carreira = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(500), nullable=True)

class Comunicacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.String(1000), nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)