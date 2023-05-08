---
title: "Alterar data da sessão"
date: 2023-05-08T20:00:45-03:00
weight: 5
menuTitle: "Alterar data"
---

A data da sessão pode ser alterada antes da realização, de acordo com as seguintes regras:

+ A data da sessão ou data inicial da sessão, para o caso de sessões contínuas, só pode ocorrer antes da sessão ter sido iniciada;
+ A data final da sessão, para o caso de sessões contínuas, só pode ocorrer antes do término da sessão;
+ Caso a pauta da sessão não tenha sido fechada ainda, a alteração pode ocorrer livremente, respeitando as regras de disponibilidade de salas que já existem no cadastro inicial da sessão;
+ Caso a pauta já tenha sido fechada, a alteração só será permitida para quem detiver o papel pje:sessao:permiteAlterarData. Para esse caso, se a alteração for na data de início ou no horário de início da sessão, o sistema deve gerar nova movimentação de "Incluído em pauta", já que a movimentação tem como complemento a data da sessão e precisa estar atualizada com a data real. Da mesma forma, as intimações automáticas deverão ser também disparadas, da mesma forma realizada no fechamento da pauta;
+ Para sessões contínuas, não há necessidade de verificar disponibilidade de sala para a alteração;
+ Para sessões presenciais, a verificação de disponibilidade será feita apenas para o dia da sessão na sala escolhida. O horário, a exemplo do que é feito na criação da sessão, não será validado.
