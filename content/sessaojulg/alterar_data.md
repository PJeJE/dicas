---
title: "Alterar data da sessão"
date: 2023-05-08T20:00:45-03:00
weight: 5
menuTitle: "Alterar data"
---

## Introdução
A data da sessão pode ser alterada antes da realização, de acordo com as seguintes regras:

+ A alteração da data da sessão ou data inicial da sessão, para o caso de sessões contínuas, só pode ocorrer antes da sessão ter sido iniciada;
+ A alteração da data final da sessão, para o caso de sessões contínuas, só pode ocorrer antes do término da sessão;
+ Caso a pauta da sessão ainda esteja _aberta_, a alteração pode ocorrer livremente, respeitando as regras de disponibilidade de salas que já existem no cadastro inicial da sessão;
+ {{<marcar texto="Caso a pauta já tenha sido fechada, a alteração só será permitida para quem detiver o papel “pje:sessao:permiteAlterarData”">}}. Para esse caso, se a alteração for na data de início ou no horário de início da sessão, o sistema gera nova movimentação de "Incluído em pauta", já que a movimentação tem como complemento a data da sessão e precisa estar atualizada com a data real. Da mesma forma, as intimações automáticas serão também disparadas, semelhante ao que ocorre no fechamento da pauta;
+ Para sessões contínuas, não existe verificação de disponibilidade de sala para a alteração;
+ Para sessões presenciais, a verificação de disponibilidade é feita apenas para o dia da sessão na sala escolhida. O horário, a exemplo do que é feito na criação da sessão, não é validado.

### Configuração do papel 

Se a pauta já estiver fechada, apenas o usuário que possuir o papel "pje:sessao:permiteAlterarData" poderá realizar alterações na data. Para configurar este acesso, siga estes passos:

1. Verifique se o papel existe no cadastro de papéis. Se não existir, crie-o:
![Tela de cadastro de papel](/imagens/parametro_alterar_data.png)
2. Na aba "Herdeiros" (Seta 2), encontre o perfil que deseja conceder acesso para alterar a data de sessão com pauta fechada e adicione-o à lista da direita (Seta 3).

Após a configuração, o usuário com a permissão poderá retornar ao cadastro da sessão de julgamento e alterar a data.
