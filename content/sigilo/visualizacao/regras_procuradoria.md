---
title: "Regra das procuradorias"
date: 2023-01-16T10:49:43-03:00
weight: 2
---
Ao cadastrar uma procuradoria como visualizadora do processo sigiloso, os participantes dessa procuradoria estarão aptos a visualizarem o processo, salvo se detiverem o papel pje:papel:administrarProcuradorias.

Esse papel existe para que procuradorias possam atribuir a servidores a função administrativa de cadastrar novos procuradores e novos assistentes de procuradoria, com a restrição de não visualizarem processos. Dessa forma, o papel de procurador ou de procurador gestor não pode conter em sua hierarquia o papel de administrador de procuradoria, sob pena de não visualizarem os processos sigilosos aos quais a procuradoria tem acesso.

A visualização dos procuradores depende do correto cadatramento da porcuradoria como visualizador do processo. Observe a imagem abaixo:

IMG_VISUALIZACAO_PROCURADORIAS

No destaque em amarelo (número 1) o cadastramento está correto e todos os usuários da procuradoria, respeitadas as regras de visualização dentro das caixas, terão acesso aos autos. 

Já no exemplo em azul (número 2), está incorreto. Apenas quando o símbolo de procuradoria aparece ao lado do nome é que os usuários vão ver o processo.

Caso precise ajustar os visualizadores, clique em **Opções** e escolha a opção **Liberar Vizualização para todas as partes.** Dessa forma as procuradorias serão cadastradas de maneira correta. Após isso, se for necessário, exclua visualizadores que não deveriam ter sido incluídos. 
