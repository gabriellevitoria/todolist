from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  #toda vez que o flask receber a url com / vai executar a rome. criamos uma rota. mesmo que no final não tenha barra,
#quando não tem nada ele considera#

def home():
    #templates/home.html
    return render_template('home.html')

@app.route('/bye')
def bye():
    return'Bye'

app.run(debug=True) #fica escutando alterações no código, qualquer mudança reinicia o servidor. 