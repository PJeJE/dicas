---
title: "Plenário Virtual"
date: 2026-05-29T12:09:20-03:00
weight: 10
---
## Regras Negociais

1. Horário de início da sessão: o próprio horário de início da sessão ou, caso ele esteja nulo, o horário de início da sala;

2. Horário de fim da sessão: o horário de fechamento da sessão ou, caso ele esteja nulo, o horário final da sala;

3. Só serão mostrados os processos que possuem data de exclusão nula;
   
4. Quando o processo estiver em segredo de justiça, mostra só o relator e a situação de julgamento;

5. Os processos são mostrados ordenados;
    
6. Sessões futuras são as que não possuem data de fechamento da pauta ou não possuem pauta;

7. O campo Informações pode conter:
   
a. Segredo de justiça;

b. Julgamento em conjunto;

c. Nome do bloco de julgamento;

d. Motivo de retirada de pauta. Ex: Pedido de Vista.

9. As situações da sessão são baseadas na data e horário da consulta:
a. Data de consulta é anterior a data de abertura e horário de início da sessão = “Aguardando Julgamento”
b. Data de consulta é igual a data de abertura e horário de início da sessão = “Em julgamento”
c. A sessão é virtual e a data de consulta é posterior a data e horário fim da sessão = “Realizada” ou a sessão é presencial e data de consulta é posterior a data de realização da sessão = “Realizada”. No caso das sessões presenciais, é sempre até às 23h59 do dia da sessão

10. A classe judicial é a própria casse judicial do processo ou, quando possui um recurso interno, é a descrição da classe judicial por extenso (ds_classe_judicial_extenso);

11. A Certidão de Julgamento que será exibida apenas quando o processo estiver Julgado (JG) ou possuir um Pedido de Vista e não estiver julgado (NJ). 

12. O pedido de vista é mostrado apenas quando existir um Pedido de vista e o processo não estiver julgado (NJ);

13. O pedido de destaque é mostrado apenas quando o processo é retirado de pauta e existir um adiamento por Pauta Presencial (PP);

14. O órgão julgado vencedor é mostrado apenas quando o processo está Julgado (JG)

15. O motivo de retirada de pauta é mostrado apenas quando o processo não foi retirado de julgamento;

16. A ementa (id_tipo = 77) e o relatório (id_tipo = 73) só são mostrados quando:
a. Estão ativos;
b. Não são sigilosos;
b. O julgamento está finalizado ou possui uma data de realização da sessão;
c. A situação do julgamento do processo é JG (Julgado);
d. Estão liberados;
e. Possui uma data de abertura da sessão;
f. Não estão em segredos de justiça.

17. É considerado sempre a última ementa e o último relatório;

18. Mostra quem está impedido ou omisso:
a. O impedido é apenas uma marcação in_impedimento_suspeicao true ou false
b. O omisso é quem faz parte da composição da sessão, não está impedido e não possui voto OU é o relator, possui voto que não esteja liberado e não esteja impedido

19. Só são mostrados os votos:
a. De quem está presente ou é o relator
b. Onde a situação de julgamento é AJ (Aguardando Julgamento) (17/02/2025) ou EJ (Em Julgamento) ou JG (Julgado) ou tem um pedido de vista e a situação é NJ (Não julgado)
c. Onde o julgamento está finalizado ou tenha uma data de realização da sessão
d. Onde tem uma data de abertura da sessão
e. Quando o processo não estiver em segredo de justiça
f. Que estão liberados, exceto se o voto for do relator.

20. O documento do voto é mostrado apenas quando:
a. Estiver ativo
b. Não for sigiloso
c. Possuir assinatura (data de juntada). Caso o parâmetro “pje:sessao:plenarioVirtual:documentoAssinado” do PJe estiver como false, não é necessário o documento possuir assinatura. Se estiver como true ou vazio, precisa estar assinado para mostrar (17/02/2025)

21. Será mostrado sempre o último voto do votante

22. A relatoria será do primeiro julgamento do processo, não do julgamento atual (novo relator)

23. Documentos que serão mostrados a depender de quem for o vencedor, relator ou vogal:
a. Relator vencedor:
i. Ementa do relator – Sim
ii. Relatório do relator – Sim
iii. Voto do relator – Sim

b. Vogal vencedor:
i. Ementa do relator - Não, pois ela é descartada quando tem a ementa do vogal vencedor. Para assinar o acórdão, tem que excluir a ementa (rascunho) do relator
ii. Relatório do relator – Sim
iii. Voto do relator – Sim
iv. Ementa do vogal – Sim
v. Relatório do vogal - Não existe, o vogal só cria o voto e a ementa dele
vi. Voto do vogal – Sim

23. Caso o parâmetro “pje:sessao:plenarioVirtual:documentoAssinado” do PJe esteja como false, não é necessário o documento de relatório, ementa ou voto possuir assinatura para ser visualizado, bastando estar como liberados no PJe. Se o parâmetro estiver como true ou vazio, o documento precisa estar assinado para ser visualizado. Ementa e Relatório são mostrados independente da situação do processo.

24. Podem ser mostradas mais de uma sessão presencial no mesmo dia.
