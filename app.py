# Instalando Flask

from flask import Flask, render_template, request, url_for, jsonify

from flask_mysqldb import MySQL



app = Flask(__name__)
#Bootstrap(app)



# conexão com o banco de dados
app.config['MYSQL_Host'] = '127.0.0.1' # 127.0.0.1
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'contato'

mysql = MySQL(app)


@app.route("/")
def home():
    return render_template("Index.html")

@app.route("/quemsomos/")
def quems_somos():
    return render_template("quemsomos.html")

'''
@app.route("/contato/")
def contatos():
    return render_template("contato.html")

'''


@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    if request.method == "POST":
        nome =  request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO formulario(nome, email, assunto, descricao) VALUES (%s,%s, %s, %s)", (nome,email, assunto, descricao)) #faltando usuario
       
        mysql.connection.commit()
        
        cur.close()

        return 'sucesso'
    return render_template('contato.html')


# rota usuários para listar todos os usuário no banco de dados.
@app.route('/users/')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM formulario")

    if users > 0:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails=userDetails)


