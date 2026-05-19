---
title: "Partes"
date: 2022-12-01T16:31:43-03:00
weight: 1
---

A situação das partes não ativas no processo pode ser suspensa, inativa e baixada.

Parte suspensa é aquela que, no processo criminal, na fase de execução da pena, está cumprindo normalmente as medidas restritivas as quais foi condenada. Se ela para de cumprir o que foi determinado na sentença, volta a ficar ativa no processo.

Parte inativa (situação da parte marcada como “I”) e parte baixada (situação da parte marcada como “B”) são partes cuja relação processual foi extinta, independentemente do motivo.

{{% notice info %}}
As partes **inativas** "somem" da capa dos autos, já as **baixadas** permanecem na autuação, mas tachadas (riscadas).
{{% /notice %}}

A diferença entre elas é que as partes baixadas ainda podem ser utilizadas como parâmetro nas consultas processuais e são retornadas no detalhamento do processo. O mesmo não ocorre com as partes inativas: quando se utiliza partes inativas como parâmetro na consulta processual, os respectivos processos não serão retornados.

{{% notice info %}}
Ao submeter solicitação de habilitação nos autos que remove advogados da autuação, ou seja, quando há substituição de advogados, o sistema altera a situação do advogado substituído no processo para **BAIXADO**.
{{% /notice %}}

## Endereço das partes

Para cadastrar um endereço vinculado a uma parte, o PJe sempre exige o fornecimento do CEP. Com o número do CEP, o PJe pesquisa em seus registros internos o endereço vinculado e preenche automaticamente os campos associados, deixando-os livres para edição, com exceção dos campos **Estado** e **Cidade**.

O cadastro de CEPs de onde o PJe recupera o endereço está disponível por meio do menu **Configuração - Tabelas Básicas - CEP**. O cadastro já existente foi alimentado inicialmente de uma base dos correios, mas o usuário com permissão pode cadastrar novos CEPs por meio da tela citada.
