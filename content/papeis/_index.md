+++
title = "Papéis e recursos"
date = 2024-09-03T14:07:27-03:00
weight = 12
chapter = true
pre = "<b>12. </b>"
+++

### Seção 12

O controle de acesso no PJe utiliza o cadastro de pessoas, suas localizações e dois outros conceitos: o de papéis e o de recursos. Por recursos, entenda-se as funcionalidades acessíveis dentro do PJe. São, basicamente, itens de menu. Essas funcionalidades podem ser agrupadas em papéis criados pelo próprio usuário, como um conjunto de funcionalidades. Os papéis, por sua vez, podem conter outros papéis, criando uma hierarquia de papéis. 

A partir desses elementos, o PJe limita a visão de funcionalidades disponibilizadas ao usuário, reduzindo ou ampliando os menus e as opções disponíveis nos menus. Também limita a visualização de objetos, restringindo o acesso a essas edições. A criação de papéis e sua associação a usuários é livre ao administrador, mas esse tipo de modificação deve ser cuidadosamente planejada a fim de evitar desvios de segurança e integridade das informações. De igual modo, a criação de papéis deve ser acompanhada por uma revisão das definição das raias nos fluxos de negócio, ou seja, a definição das tarefas às quais o usuário pode acessar.

{{% notice note %}}
A redefinição de papéis sem a correspondente revisão das raias pode levar à impressão de que os processos pendentes de tarefas “desapareceram”, já que o usuário que utilizar o novo papel não verá processos pendentes na sua caixa de tarefas. 
{{% /notice %}}

É importante avaliar a estrutura de papéis de sua aplicação para assegurar que os papéis principais do sistema não herdem funcionalidades uns dos outros. Em outras palavras, por exemplo, servidores não podem ficar "abaixo" de magistrados na hierarquia de papéis, nem tampouco isso pode acontecer com advogados etc. Na estrutura de papéis, deve-se ficar com uma árvore parecida com a seguinte: 

    Administrador (raiz)
        Magistrado
        Servidor
            Assessor
            Assessor de plenário
        Advogado
        Assistente de advogado
        Assistente de procuradoria
        Perito
        Procurador MP
            pje:procurador 
        Procurador
            pje:procurador 
        Oficial de justiça distribuidor
            Oficial de justiça 

Outro caso concreto de situações que não devem ocorrer é, por exemplo:
 - o papel assessor-chefe é detentor do papel que permite a ele visualizar processos sigilosos
 - o papel assessor também é detentor do papel que permite a ele visualizar processos sigilosos
 - o papel assessor-chefe é detentor do papel assessor

Essa situação faz com que, ao salvar novos papeis vinculados ao papel assessor-chefe ou ao papel assessor ou ainda a alguma papel acima na sua hierarquia, o sistema tente fazer referências a todos os papéis da hierarquia e entre em uma referência cíclica, impedindo a finalizadação do cadastro.

Independente de cadastros equivocados, a alteração de papéis é sempre uma atividade demorada para o sistema. Em algumas vezes, pode acontecer de o sistema desistir de finalizar devido ao tempo máximo de espera para uma operação ter sido atingido. Não é desejável aumentar esse tempo então, caso isso ocorra, abra um chamado para que a TI realize a vinculação desejada direto no banco de dados.

{{% notice note %}}
Ao vincular um novo papel a um perfil já existente, a alteração só terá efeito após o usuário sair e entrar novamente da aplicação. Se você é Administrador e vinculou um novo papel ao perfil Administrador, acione o botão "Sair" do PJe para que consiga fazer sua identificação (login) novamente e, aí sim, verificar os efeitos do novo papel adicionado.
{{% /notice %}}

**Instruções para cadastro de papeis e suas vinculações:**

**Instruções para cadastro de recursos e suas vinculações:**

**Papéis existentes:**

O identificador do modelo de documento selecionado será gravado em um parâmetro do sistema denominado 
- **pje:sistema**:
  - Papel utilizado para vincular ações que sejam realizadas de forma automática



