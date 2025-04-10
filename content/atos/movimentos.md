---
title: "Movimentações processuais"
date: 2025-04-01T14:49:00-03:00
weight: 6
---


As movimentações processuais, ao lado dos assuntos e das classes, são, hoje, a única linguagem realmente unificada no Poder Judiciário Brasileiro. Embora o sistema faça referência a esses movimentos como “eventos”, designação historicamente utilizada pela Justiça Federal, o uso das movimentações nacionais deve ser feito intensamente no sistema para assegurar a coleta de informações estatísticas relevantes. 

Instruções relevantes sobre movimentações processuais podem ser encontradas no [link](https://docs.pje.jus.br/manuais-de-uso/Manual%20de%20referencia%20PJe%201.0#movimenta%C3%A7%C3%B5es)

## Inclusão de movimentos na justiça eleitoral

No PJe da Justiça Eleitoral, as movimentações são incluídas nos processos por diversos meios. 

Dependendo do ponto do PJe, o conjunto de tipos de movimento a serem lançados são diferentes. Pode-se verificar os tipos de movimento existentes pelo link do [SGT](https://www.cnj.jus.br/sgt/consulta_publica_movimentos.php). 

Por exemplo, nas tarefas onde o usuário seleciona o movimento a ser lançado que são apresentada após assinatura de documentos de ato proferido ou de condução de audiências  
(**Lançar movimentos de Julgamento Colegiado**, **Lançar movimentos de julgamento colegiado**, **Lançar movimento**, **Lançar movimento - Corregedoria**, **Lançar Movimentação Processual** ou **Lançar Movimentação**), os movimentos possíveis são os relacionados à árvore de **Magistrado**. 

Já movimentos lançados no decorrer da tramitação processual são, via de regra, da árvore de **Serventuário**. É o caso de movimentos que são lançados após remessa de processos entre instâncias. 

Os movimentos lançados pelo próprio PJe após execução de alguma atividades também são, via de regra, da árvore de **Serventuário**, como por exemplo, o movimento lançado ao final da realização da sessão de julgamento ou o movimento lançado após distribuição/redistribuição de processos.

Há também casos onde as integrações são responsáveis pelo lançamento de movimentos, como, por exemplo, o movimento que sinaliza a totalização dos votos em uma eleição, que é lançado pela integração com o o sistema de registro de candidaturas.

Temos na Justiça Eleitoral uma outra possibilidade de lançamento de movimentos que é pela funcionalidade **Ajustar movimentação**, cujas instruções de utilização podem ser encontradas [aqui](/docs/manual_ajustar_movimentacao.pdf).

## Configuração de movimentos, aplicabilidade e complementos

A configuração de movimentos é um ponto extremamente relevante para o correto funcionamento do PJe. O conjunto de movimentos habilitados na Justiça Eleitoral são periodicamente revistos por um grupo de discussão que envolve o TSE e representantes dos regionais. 

Há instruções relevantes sobre as configurações de movimentações processuais no [link](https://docs.pje.jus.br/manuais-de-uso/Manual%20de%20referencia%20PJe%201.0#movimenta%C3%A7%C3%B5es)

Gostaríamos e ressaltar alguns pontos importantes a respeito da configuração de complementos.

Na configuração da aplicabilidade do movimento, são configuradas as possibilidades de inserção de complementos dos movimentos. Isso significa que, ainda que o usuário tenha selecionado algum complemento de movimento, se a aplicabilidade não tiver corretamente configurada para conter o complemento, ele não será exibido na descrição do movimento lançado. Da mesma forma, caso seja inserido um complemento na configuração da aplicabilidade e o complemento não seja informado pelo usuário ou pela própria aplicação, o movimento é lançado sem o complemento e exibindo um texto sem sentido para o usuário. Por exemplo, se for configurado o complemento **tipo_da_decisao_anterior** no movimento de código SGT 945 e o usuário não tiver como informar esse complemento, o sistema lançará o movimento da seguinte forma:

Revogada decisão anterior #{tipo_da_decisao_anterior} datada de 12/05/2024

Para que o usuário consiga visualizar o complemento para selecionar, a aba complemento do referido movimento deve ser preenchida com o complemento respectivo. 

Ainda sobre complementos, especialmente sobre complementos do tipo **dinâmico** (que remetem ao tipo **identificador** do SGT), a configuração, via de regra, dependerá de um desenvolvedor com acesso ao código do PJe para identificar qual expressão recuperará o dado dinâmico que o movimento precisará. Tomando como exemplo o mesmo movimento de código SGT 945 citado no parágrafo acima, o complemento **tipo_da_decisao_anterior** precisa ser apresentado para ser selecionado ao usuário que lança o movimento contendo uma lista de atos para que o usuário selecione qual tipo de decisão será revogada. Quem faz a configuração da expressão que recupera os tipos de decisão é o usuário administrador, mas ele não tem como saber qual expressão é capaz de recuperar esses valores dentro do PJe. Após retorno do desenvolvedor com a respectiva expressão, aí sim, o usuário administrador, de posse da expressão, pode fazer a efetiva configuração na campo adequado na configuração de complemento. Para esse complemento específico, recomendamos a expressão **#{tipoProcessoDocumentoManager.getTipoDocumentoAtoMagistradoList()}**, que recupera os tipos de documentos que são assinados por magistrados no PJe.
