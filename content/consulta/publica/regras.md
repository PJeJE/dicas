---
title: "Regras da Consulta Pública Unificada"
date: 2023-01-20T10:29:52-03:00
weight: 1
hidden: false
---

**RN001-** Serão retornados os **DADOS BÁSICOS** de todos os processos, com exceção daqueles em segredo de justiça, caso em que será apresentada a mensagem “Nenhum processo encontrado”. 

**RN002 -** Serão retornadas as **PARTES**:

1 - que não sejam sigilosas (caso a parte seja sigilosa, não retornam ela nem seus advogados); 

2 - cuja situação seja Ativa (A), Baixada (B) ou Suspensa (S), sendo as duas últimas apresentadas taxadas;
    
IMPORTANTE: nomes de partes menores de idade serão abreviados.

**RN003 -** Serão retornados todos os **MOVIMENTOS** que tenham visibilidade externa e que não sejam sigilosos.

**RN004 -** Serão exibidos os **DOCUMENTOS** assinados, desde que: ativos na base de dados, que não sejam sigilosos e que cuja sua visibilidade esteja marcada como pública.
        
Exceção: 

• Se a classe estiver marcada como pública (na configuração da classe), todos os documentos serão retornados na Consulta Pública (sem a restrição final da RN004).
