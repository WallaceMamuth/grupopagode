#!/bin/bash
# Script para criar repositório no GitHub via API

# Substitua SEU_TOKEN_AQUI pelo seu Personal Access Token do GitHub
TOKEN="SEU_TOKEN_AQUI"
USERNAME="WallaceMamuth"
REPO_NAME="grupopagode"

echo "Criando repositório $REPO_NAME no GitHub..."

curl -X POST \
  -H "Authorization: token $TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d "{
    \"name\": \"$REPO_NAME\",
    \"description\": \"Site do Grupo Pagode com Flask e Tailwind CSS\",
    \"private\": false,
    \"auto_init\": false
  }"

echo -e "\n\nRepositório criado! Agora execute:"
echo "git push -u origin main"

