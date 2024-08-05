# Neuralmed monorepo
## requisitos
- docker

## comandos
- make upload-api-dev (roda upload api apenas)
- make resize-api-dev (roda resize api apenas)
- make dev (roda tudo)

## img-upload-api - API de upload de imagens
- recebe um link da imagem ou a imagem em si
- persiste a imagem no banco de dados
- enfileira um job de redimentsionamento de imagens

## img-resize-api - API de redimensionamento de imagens
- usa uma fila para receber requests
- redimensiona imagens para 384x384