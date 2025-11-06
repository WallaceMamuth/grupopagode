"""
Script para gerar versão estática do site para GitHub Pages
"""
from jinja2 import Environment, FileSystemLoader
import os
import shutil

# Configurar Jinja2
env = Environment(loader=FileSystemLoader('templates'))

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

def url_for(endpoint, filename=None):
    """Simula url_for do Flask para GitHub Pages"""
    if endpoint == 'static' and filename:
        return f'./static/{filename}'
    routes = {
        'index': './index.html',
        'shows': './shows.html',
        'musicas': './musicas.html',
        'sobre': './sobre.html',
        'contato': './contato.html'
    }
    return routes.get(endpoint, './index.html')

def render_static_template(template_name, output_path, context, active_page=None):
    """Renderiza template e ajusta caminhos para GitHub Pages"""
    template = env.get_template(template_name)
    
    # Adicionar url_for ao contexto
    context['url_for'] = url_for
    context['request'] = {'endpoint': active_page} if active_page else {}
    
    html = template.render(**context)
    
    # Ajustar condicionais de menu ativo
    if active_page:
        html = html.replace(f"request.endpoint == '{active_page}'", "True")
    # Remover outras condições
    for page in ['index', 'shows', 'musicas', 'sobre', 'contato']:
        if page != active_page:
            html = html.replace(f"request.endpoint == '{page}'", "False")
    
    # Ajustar action do formulário
    html = html.replace('action="{{ url_for(\'contato\') }}"', 'action="#"')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

# Diretório de saída
output_dir = 'docs'

# Limpar diretório
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

print("🔄 Gerando site estático para GitHub Pages...\n")

# Renderizar páginas
render_static_template('index.html', os.path.join(output_dir, 'index.html'), 
                      {'shows': SHOWS[:3], 'musicas': MUSICAS[:3], 'integrantes': INTEGRANTES}, 
                      active_page='index')
print("✓ index.html")

render_static_template('shows.html', os.path.join(output_dir, 'shows.html'),
                      {'shows': SHOWS}, active_page='shows')
print("✓ shows.html")

render_static_template('musicas.html', os.path.join(output_dir, 'musicas.html'),
                      {'musicas': MUSICAS}, active_page='musicas')
print("✓ musicas.html")

render_static_template('sobre.html', os.path.join(output_dir, 'sobre.html'),
                      {'integrantes': INTEGRANTES}, active_page='sobre')
print("✓ sobre.html")

render_static_template('contato.html', os.path.join(output_dir, 'contato.html'),
                      {'sucesso': False}, active_page='contato')
print("✓ contato.html")

# Copiar arquivos estáticos
if os.path.exists('static'):
    shutil.copytree('static', os.path.join(output_dir, 'static'), dirs_exist_ok=True)
    print("✓ Arquivos estáticos copiados")

print(f"\n✅ Build concluído! Arquivos em: {output_dir}/")
print("\n📝 Próximos passos:")
print("   1. git add docs/")
print("   2. git commit -m 'Deploy para GitHub Pages'")
print("   3. git push")
