# 🚀 Como Publicar no GitHub Pages

## ✅ Passo 1: Configurar GitHub Pages

1. Acesse seu repositório: https://github.com/WallaceMamuth/grupopagode
2. Clique em **Settings** (Configurações)
3. No menu lateral, clique em **Pages**
4. Em **Source**, selecione:
   - Branch: `main`
   - Folder: `/docs`
5. Clique em **Save**

## ✅ Passo 2: Aguardar Deploy

- Aguarde alguns minutos (1-5 minutos) para o GitHub processar
- Você verá uma mensagem: "Your site is live at https://wallacemamuth.github.io/grupopagode/"

## 🔄 Para Atualizar o Site

Sempre que fizer mudanças, execute:

```bash
# 1. Gerar novos arquivos estáticos
python build.py

# 2. Adicionar e commitar
git add docs/
git commit -m "Atualizar site"

# 3. Enviar para GitHub
git push origin main
```

O site será atualizado automaticamente em alguns minutos!

## 📝 URL do Site

Após configurar, seu site estará disponível em:

**https://wallacemamuth.github.io/grupopagode/**

## 🎨 Personalizar

Para mudar o nome do repositório e consequentemente a URL:

1. Vá em Settings > General
2. Renomeie o repositório
3. A URL será: `https://wallacemamuth.github.io/NOVO-NOME/`

## ⚠️ Importante

- O arquivo `.nojekyll` na pasta `docs/` é necessário para o GitHub Pages funcionar corretamente
- Sempre execute `python build.py` antes de fazer commit após mudanças nos templates
- As imagens e arquivos estáticos devem estar em `docs/static/`

