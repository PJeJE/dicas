+++
title = "Documentos Processuais"
date = 2022-11-23T17:49:43-03:00
weight = 1
chapter = true
+++

### Autos Digitais

# Documentos Processuais

A aba **Documentos** exibe uma lista contendo todos os documentos vinculados ao processo.

A lista é exibida respeitando algumas restrições:
- Os documentos vinculados a expedientes construídos a partir de documentos existentes não serão exibidos, visto que são apenas cópias de documentos já produzidos
- Caso a data de juntada não exista ou não existam assinadores para o documento, ele só será exibido 
 - se o usuário de inclusão for o usuário atual ou
 - se o usuário de inclusão for um assistente de advogado e a localização do assistente for a localização atual ou
 - se o usuário de inclusão for um assistente de procuradoria e a localização do assistente for a localização atual ou
 - se a localização de inclusão do documento seja a localização atual
- Caso a data de juntada exista e existam assinadores para o documento, ele será exibido, exceto de acordo com as seguintes situações:
 - se o documento é sigiloso ou o documento principal a ele vinculado é sigiloso
   - o usuário deve estar cadastrado como visualizador do documento ou deve estar vinculado à procuradoria cadastrada como visualizadora ou
   - se o usuário estiver vinculado ao papel visualizasigiloso ou manipulasigiloso, deve estar vinculado ao órgão julgador ou órgão julgador colegiado do processo, conforme for a vinculação do usuário atual a uma localização ou
   - se o usuário de inclusão for o usuário atual ou
   - se o usuário de inclusão for um assistente de advogado e a localização do assistente for a localização atual ou
   - se o usuário de inclusão for um assistente de procuradoria e a localização do assistente for a localização atual ou 

Os documentos são exibidos na ordem descrecente da data de juntada


A seguir, algumas informações relacionadas a documentos do processo.

{{% children  %}}
