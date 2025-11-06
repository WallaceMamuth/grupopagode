# Como Publicar no GitHub

## Passo 1: Criar Repositório no GitHub

1. Acesse: https://github.com/new
2. Nome: `grupopagode`
3. Descrição: "Site do Grupo Pagode com Flask e Tailwind CSS"
4. Público ou Privado (sua escolha)
5. **NÃO marque** "Initialize with README"
6. Clique em "Create repository"

## Passo 2: Publicar o Código

Execute no terminal:

```bash
git push -u origin main
```

Se pedir credenciais:
- Username: `WallaceMamuth`
- Password: Use um **Personal Access Token** (não sua senha)

## Como Criar Personal Access Token

1. Acesse: https://github.com/settings/tokens
2. Clique em "Generate new token (classic)"
3. Nome: `grupopagode-token`
4. Selecione escopo: `repo` (tudo dentro de repo)
5. Clique em "Generate token"
6. **COPIE O TOKEN** (você só verá uma vez!)
7. Use este token como senha quando o Git pedir

## Pronto!

Seu projeto estará online em: https://github.com/WallaceMamuth/grupopagode

