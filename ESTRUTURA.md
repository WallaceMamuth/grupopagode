# 📁 Estrutura do Projeto

## ✅ O que cada pasta faz:

### `/templates/` - Templates Flask
- Templates Jinja2 para o Flask
- Usados quando você roda `python app.py` localmente
- **NÃO** são usados no GitHub Pages

### `/static/` - Arquivos estáticos do Flask
- Imagens e assets para o Flask
- Usados quando você roda localmente
- **NÃO** são usados no GitHub Pages

### `/docs/` - Site estático para GitHub Pages
- HTMLs gerados pelo `build.py`
- **ESTES** são os arquivos que o GitHub Pages usa
- Gerados automaticamente a partir dos templates
- Contém cópia das imagens em `docs/static/images/`

### `/assets/` - Assets do template original
- CSS, JS, fonts do template original
- Não são mais usados (o site usa Tailwind CSS via CDN)
- Podem ser removidos se quiser

### `/images/` - Imagens antigas
- Imagens do template original
- Não são mais usadas (estão em `/static/images/` e `/docs/static/images/`)
- Podem ser removidos se quiser

## 🔄 Fluxo de trabalho:

1. **Desenvolver localmente:**
   ```bash
   python app.py  # Usa templates/ e static/
   ```

2. **Gerar site estático:**
   ```bash
   python build.py  # Gera docs/ a partir de templates/
   ```

3. **Publicar:**
   ```bash
   git add docs/
   git commit -m "Atualizar site"
   git push
   ```

## 🎯 Resumo:

- **Para desenvolvimento:** Use `templates/` e `static/`
- **Para GitHub Pages:** Use `docs/` (gerado automaticamente)

