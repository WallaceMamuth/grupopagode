from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Dados do grupo
SHOWS = [
    {
        'data': '15 de Fevereiro, 2024',
        'local': 'Bar do Zé',
        'cidade': 'São Paulo, SP',
        'horario': '22:00'
    },
    {
        'data': '20 de Fevereiro, 2024',
        'local': 'Casa de Shows Samba',
        'cidade': 'Rio de Janeiro, RJ',
        'horario': '21:00'
    },
    {
        'data': '25 de Fevereiro, 2024',
        'local': 'Festa na Praça',
        'cidade': 'Belo Horizonte, MG',
        'horario': '20:00'
    }
]

MUSICAS = [
    {
        'titulo': 'Pagode da Madrugada',
        'video_id': 'dQw4w9WgXcQ',
        'thumbnail': 'https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg'
    },
    {
        'titulo': 'Samba no Pé',
        'video_id': 'dQw4w9WgXcQ',
        'thumbnail': 'https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg'
    },
    {
        'titulo': 'Noite de Gala',
        'video_id': 'dQw4w9WgXcQ',
        'thumbnail': 'https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg'
    }
]

INTEGRANTES = [
    {'nome': 'João Silva', 'funcao': 'Vocal'},
    {'nome': 'Maria Santos', 'funcao': 'Pandeiro'},
    {'nome': 'Pedro Oliveira', 'funcao': 'Cavaquinho'},
    {'nome': 'Ana Costa', 'funcao': 'Tan-tan'}
]

@app.route('/')
def index():
    return render_template('index.html', 
                         shows=SHOWS[:3], 
                         musicas=MUSICAS[:3],
                         integrantes=INTEGRANTES)

@app.route('/shows')
def shows():
    return render_template('shows.html', shows=SHOWS)

@app.route('/musicas')
def musicas():
    return render_template('musicas.html', musicas=MUSICAS)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', integrantes=INTEGRANTES)

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form.get('name')
        email = request.form.get('email')
        mensagem = request.form.get('message')
        print(f"Mensagem de {nome} ({email}): {mensagem}")
        return render_template('contato.html', sucesso=True)
    return render_template('contato.html')

if __name__ == '__main__':
    print(f"Servidor rodando em: {os.getcwd()}")
    print("Acesse: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)

