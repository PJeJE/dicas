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

## Publicações no DJe

Um dos meios mais frequentes utilizado nas comunicações de atos processuais é o Diário de Justiça Eletrônico. O DJE da Justiça Eleitoral tem algumas particularidades para atender às necessidades da Justiça Eleitoral. Definições a respeito do DJE podem ser encontradas no [STI conhecimento](https://sticonhecimento.tse.jus.br/copp/seaju/sistemas/novo-dje).

O próprio DJe trata os autos sigilosos, omitindo os dados sensíveis do processo e das partes.

Isso é feito com base no sigilo do processo: em sendo ele sigiloso, o DJe omitirá os dados na publicação.

{{% notice warning %}}
Na tarefa **Preparar ato de comunicação,** no 2º passo, existe a opção **sigiloso** ao lado do nome da parte, mas ela não tem efeito na publicação do DJe. Ou seja, se o processo não for sigiloso, os dados da parte aparecerão mesmo que esta opção esteja selecionada. A finalidade da opção Sigiloso na tarefa Preparar ato de comunicação é fazer com que o documento que será criado/selecionado em Instrumento de comunicação (após clicar no lápis) seja sigiloso. No entanto, a recomendação é NÃO utilizar essa marcação. Ela não se comporta como o esperado e depende de correção.
{{% /notice %}}

{{< video src="/videos/intimacao-em-lote.mp4">}}

### Diário Eleitoral

Existe uma diferença entre as configurações do DJE para publicações de matérias eleitorais e a marcação “período especial” no DJE (disponível quando o ato de comunicação é feito no meio DJE.

No DJe existem duas configurações possíveis:

![diario 1](/imagens/diario_1.png)

**a) Ativar Funcionalidade Diário Eleitoral,** que permite que a marcação feita no PJe (período especial) seja válida para o DJe. Essa opção (destacada em azul na imagem acima), faz com que existam dois diários: um eleitoral, que circula direto (sábados, domingos e feriados) e outro comum (só circula nos dias úteis).

Neste caso, no momento da criação do ato no PJe, é preciso usar a opção “período especial” do PJe para separar o que vai para o diário eleitoral:

![diario 2](/imagens/diario_2.png)

Estando ativo o parâmetro e o usuário marcando período especial no PJe, o diário circula no dia seguinte, seja ele feriado, final de semana ou dia útil.

{{% notice warning %}}
Se o parâmetro Ativar Funcionalidade Diário Eleitoral for false e houver marcação no PJe de período especial, essas matérias não serão publicadas!
{{% /notice %}}

**b) Datas de Início e Término do Período Eleitoral,** que, quando marcadas, faz com que todas os diários ordinários sejam publicados no dia seguinte, independentemente de ser final de semana ou feriado. Essa opção (destacada em vermelho na primeira imagem do presente tópico), faz com que tudo o que for publicado siga a regra de circular e publicar em dias uteis e não uteis (ou seja, afeta processos não eleitorais).

{{% notice tip %}}
Estando ativos os dois parâmetros, se o usuário marcar no PJe a opção período especial, vai separar em diários diferentes e, se não marcar, vai ficar tudo junto, mas sempre em dias corridos.
{{% /notice %}}

### Calendário do PJe e reflexo no DJE

No PJe, os feriados/indisponibilidades que afetam os prazos processuais são cadastrados em ferramenta própria. O DJE aproveita o calendário do PJe. Dessa forma, ocorre uma replicação dos feriados novos cadastros de 30 em 30 minutos. 

Os feriados replicados a cada sincronização são os feriados cujas datas sejam posteriores ao momento da replicação e os feriados recorrentes, ou seja, feriados que se repetem anualmente. 

Um feriado será cadastrado no DJE como nacional, ou seja, afetará todos o envio de matérias no Brasil, caso seja cadastrado no PJe como feriado de abrangência nacional e se tiver sido cadastrado no PJe do TSE. 

Já um feriado será estadual só será replicado se a abrangência do feriado for estadual e a UF vinculada ao feriado for a mesma do PJe. Dessa forma, o estado de São Paulo não conseguirá cadastrar feriados distritais para o DF. 


 

    
            No caso do ambiente 3G (TSE), considerar o estado como Distrito Federal (DF);
        Feriados Órgão julgador (O): somente quando o in_abrangencia = O e o id_estado seja nulll (default); e
        Feriados Municipais (C): somente quando o in_abrangencia = C e o id_estado seja igual ao estado do ambiente PJe.

## Utilização da Central de Mandados

A utilização da central de mandados para fazer comunicação só será possível se o usuário selecionar, ao criar uma comunicação, o meio "Central de Mandados". Caso seja selecionado, o servidor terá que complementar as informações sobre a central de mandados em tarefa posterior que será apresentada ao finalizar a construção do documento a ser utilizado na comunicação. 

Da mesma forma, a tarefa para complementação das informações sobre a central de mandados só será apresentada se o usuário tiver selecionado o meio pertinente. Caso a tarefa seja apresentada e o usuário tenha selecionado o meio erroneamente, recomenda-se seguir o fluxo de complementação das informações da central e, só ao finalizar os procedimentos, fechar o expediente, certificando que a comunicação não precisa ser cumprida, conforme termos comuns da prática cartorária do regional.
