# ⚠️ IMPORTANTE: Configuração do GitHub Pages

## 🔧 Configuração Necessária

Para o site funcionar corretamente, você DEVE configurar o GitHub Pages para usar a pasta `docs/`:

1. Acesse: https://github.com/WallaceMamuth/grupopagode/settings/pages
2. Em **Source**, selecione:
   - **Branch**: `main`
   - **Folder**: `/docs` ← **IMPORTANTE: Deve ser `/docs`**
3. Clique em **Save**

## ❌ Problema Comum

Se o site está mostrando o conteúdo antigo ("Massively"), é porque:
- O GitHub Pages não está configurado para usar `/docs`
- Ou está usando a raiz (`/`) ao invés de `/docs`

## ✅ Solução

**SEMPRE use a pasta `/docs` como source no GitHub Pages!**

O arquivo `index.html` na raiz é o template antigo e NÃO deve ser usado.

## 📝 URL do Site

Após configurar corretamente:
- **URL**: https://wallacemamuth.github.io/grupopagode/
- Deve mostrar: "Grupo Pagode" (não "Massively")

