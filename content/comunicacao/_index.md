+++
title = "Comunicação de Atos Processuais"
date = 2022-11-21T14:58:50-03:00
weight = 7
chapter = true
pre = "<b>7. </b>"
+++

### Seção 7

# Comunicação de Atos Processuais

{{% children  %}}

## 1. Publicações no DJe

O próprio DJe trata os autos sigilosos, omitindo os dados sensíveis do processo e das partes.

Isso é feito com base no sigilo do processo: em sendo ele sigiloso, o DJe omitirá os dados na publicação.

{{% notice warning %}}
Na tarefa **Preparar ato de comunicação,** no 2º passo, existe a opção **sigiloso** ao lado do nome da parte, mas ela não tem efeito na publicação do DJe. Ou seja, se o processo não for sigiloso, os dados da parte aparecerão mesmo que esta opção esteja selecionada. A finalidade da opção Sigiloso na tarefa Preparar ato de comunicação é fazer com que o documento que será criado/selecionado em Instrumento de comunicação (após clicar no lápis) seja sigiloso. No entanto, a recomendação é NÃO utilizar essa marcação. Ela não se comporta como o esperado e depende de correção.
{{% /notice %}}

## 2. Diário Eleitoral

Existe uma diferença entre as configurações do DJE para publicações de matérias eleitorais e a marcação “período especial” no DJE (disponível quando o ato de comunicação é feito no meio DJE.

No DJe existem duas configurações possíveis:

IMG_DIARIO_1

**a) Ativar Funcionalidade Diário Eleitoral,** que permite que a marcação feita no PJe (período especial) seja válida para o DJe. Essa opção (destacada em azul na imagem acima), faz com que existam dois diários: um eleitoral, que circula direto (sábados, domingos e feriados) e outro comum (só circula nos dias úteis).

Neste caso, no momento da criação do ato no PJe, é preciso usar a opção “período especial” do PJe para separar o que vai para o diário eleitoral:

IMG_DIARIO_2

Estando ativo o parâmetro e o usuário marcando período especial no PJe, o diário circula no dia seguinte, seja ele feriado, final de semana ou dia útil.

{{% notice warning %}}
Se o parâmetro Ativar Funcionalidade Diário Eleitoral for false e houver marcação no PJe de período especial, essas matérias não serão publicadas!
{{% /notice %}}

**b) Datas de Início e Término do Período Eleitoral,** que, quando marcadas, faz com que todas os diários ordinários sejam publicados no dia seguinte, independentemente de ser final de semana ou feriado. Essa opção (destacada em vermelho na primeira imagem do presente tópico), faz com que tudo o que for publicado siga a regra de circular e publicar em dias uteis e não uteis (ou seja, afeta processos não eleitorais).

{{% notice tip %}}
Estando ativos os dois parâmetros, se o usuário marcar no PJe a opção período especial, vai separar em diários diferentes e, se não marcar, vai ficar tudo junto, mas sempre em dias corridos.
{{% /notice %}}



