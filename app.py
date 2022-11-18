from flask import Flask, render_template, request

app = Flask(__name__)

tasks = [
    {
        'name': 'estudar',
        'finished': False
    },
    {
        'name': 'dormir',
        'finished': True
    },

    {   'name' : 'comer',
        'finished': True

    }
]


@app.route('/')  #toda vez que o flask receber a url com / vai executar a rome. criamos uma rota. mesmo que no final não tenha barra,
#quando não tem nada ele considera#

def home():
    #templates/home.html
    return render_template('home.html', tasks = tasks)

@app.route('/create', methods =['POST'])
def create():
    name = request.form['name']#pega cada input do forms e traz como valor
    task = {'name': name,
            'finished': False
    }
    tasks.append(task)
    return render_template('home.html', tasks = tasks) 

app.run(debug=True) #fica escutando alterações no código, qualquer mudança reinicia o servidor. 