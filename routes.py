from flask import render_template, request, redirect, url_for
from models import db, Recurso, Orientacao, Comunicacao

def configure_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/recursos')
    def recursos():
        recursos = Recurso.query.all()
        return render_template('recursos.html', recursos=recursos)

    @app.route('/orientacao')
    def orientacao():
        orientacoes = Orientacao.query.all()
        return render_template('orientacao.html', orientacoes=orientacoes)

    @app.route('/comunicacao', methods=['GET', 'POST'])
    def comunicacao():
        if request.method == 'POST':
            mensagem = request.form['mensagem']
            nova_comunicacao = Comunicacao(mensagem=mensagem)
            db.session.add(nova_comunicacao)
            db.session.commit()
            return redirect(url_for('comunicacao'))
        
        comunicacoes = Comunicacao.query.all()
        return render_template('comunicacao.html', comunicacoes=comunicacoes)