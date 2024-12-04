---
title: "Regras da Consulta Pública"
date: 2023-01-20T10:29:52-03:00
weight: 1
hidden: false
---

**RN001-** Serão retornados os DADOS BÁSICOS de todos os processos, com exceção dos processos em segredo de justiça, caso em que será apresentada a mensagem “Nenhum processo encontrado”. 

**RN002 -** Serão retornadas as PARTES:

1 - que não sejam sigilosas (caso a parte seja sigilosa, não retorna ela nem seus advogados); 
2 - cuja situação seja Ativa (A), Baixada (B) ou Suspensa (S), sendo as duas últimas apresentadas taxadas;
    
Importante: nomes de partes menores de idade serão abreviados.

**RN003 -** Serão retornados todos os MOVIMENTOS que tenham visibilidade externa e que não sejam sigilosos.

**RN004 -** Serão exibidos os DOCUMENTOS dos processos
1 - assinados, desde que: ativos na base de dados, que não sejam sigilosos e que cuja sua visibilidade esteja marcada como pública;
        
Exceção: para as classes abaixos, todos os documentos serão apresentados (mesmo os não públicos), desde que o documento ou o processo não sejam sigilosos:

• PRESTAÇÃO DE CONTAS ANUAL (Código: 12377);

• PRESTAÇÃO DE CONTAS ELEITORAIS (Código: 12193);

• REGISTRO DE CANDIDATURA (Código: 11532);

• REQUERIMENTO DE REGULARIZAÇÃO DE OMISSÃO DE PRESTAÇÃO DE CONTAS ANUAL (Código: 12631);

• REQUERIMENTO DE REGULARIZAÇÃO DE OMISSÃO DE PRESTAÇÃO DE CONTAS ELEITORAIS (Código: 12633);

• PRESTAÇÃO DE CONTAS (Código: 11531);

• PROPAGANDA PARTIDÁRIA (Código: 11536);
