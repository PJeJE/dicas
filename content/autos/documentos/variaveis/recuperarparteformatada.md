---
title: "Recuperar parte formatada"
date: 2023-01-20T17:57:39-03:00
weight: 6
hidden: true
---

Utilização: `#{processoJudicialAction.recuperarParteFormatada(true, true, 'A', 'P', 'T')}` 

Essa variável permite que se recupere os nomes das partes do processo e seus tipos (recorrente,recorrido...) juntamente com seus advogados alinhados. Pode-se recuperar os advogados com o número da OAB ou não. Pode-se recuperar em formato de tabela (alinhado) ou não (alinhamento pode ter alguma variação, mas não causará problemas na publicação do Diário antigo) Pode-se recuperar todos os polos ou especificar polos específicos. Além disso, a variável retorna o nome social, caso tenha sido cadastrado. Caso a parte seja sigilosa, retorna "Em segredo de justiça" em lugar do nome da parte.

Ao utilizar a expressão acima em modelos de documentos, o documento resultante será contruído exibindo, no lugar da expressão, as partes do processo junto com representantes advogados em linhas separadas e com colunas alinhadas, de forma que sejam exibidos os nomes dos tipos de parte respectivos junto com os nomes das partes. Para o caso de advogados, a alinhamento é feito de forma que o advogado fique vinculado à parte que ele representa.

Utilizando diferentes parâmetros entre os parênteses, pode-se alterar o que será retornado.

- 1º item dentro dos parênteses informa que a resposta virá dentro de uma tabela (true) ou fora (false);
- 2º item informa se, quando houver advogados, deve ser exibida a oab (true) ou não (false);
- 3º item "A" informa que devem ser retornadas as partes do polo ativo;
- 4º item "P" informa que devem ser retornadas as partes do polo passivo;
- 5º item "T" informa que devem ser retornadas os terceiros cadastrados no processo.

O usuário pode configurar a variável no modelo de documento de diversas formas:

processoJudicialAction.recuperarParte(true, false,'A')

**{{<marcar texto="OU">}}**

processoJudicialAction.recuperarParte(true, true,'A', 'P')

**{{<marcar texto="OU">}}**

processoJudicialAction.recuperarParte(false, true,'T')


Portanto, podem ser recuperadas as partes do polo ativo, passivo ou terceiros separadas ou em conjunto. As diversas opções da variável flexibilizam como e o que recuperar ao elaborar um novo documento.

