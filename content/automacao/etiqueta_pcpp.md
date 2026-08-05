---
title: "Anonimização"
date: 2025-08-05T14:16:02-03:00
linkTitle: "Anonimização"
weight: 3
---

 
A anonimização de dados no PJe tem como objetivo proteger informações não divulgáveis em documentos públicos, assegurando o cumprimento da legislação de proteção de dados e do sigilo processual.

O projeto opera em duas frentes principais: **Anonimização Automática** e **Anonimização Manual**.

---

## 1. Anonimização Automática

A anonimização automática utiliza Inteligência Artificial para ocultar dados pessoais em documentos da classe Registro de Candidatura, tais como:

- Certidões criminais;
- Certidões de desincompatibilização;
- Comprovantes de escolaridade.

A ferramenta anonimiza os dados apenas na Consulta Pública do PJe, sem afetar a visualização dos documentos para usuários internos e externos na árvore processual.

### 1.1 Premissas

- O documento é sinalizado na árvore do processo como anonimizado automaticamente;
- A ferramenta permite a retificação (inclusão ou remoção de anonimizações), sempre a partir do arquivo original. Por segurança, não é possível recuperar informações anonimizadas a partir do arquivo já anonimizado;
- As retificações realizadas refletem apenas na Consulta Pública Unificada do PJe.
  
---

## 2. Anonimização Manual

A anonimização manual (**Anonimizador Manual**) é a funcionalidade do PJe que permite ocultar (tarjar) informações sensíveis em documentos já juntados aos autos, mediante decisão judicial. Ela complementa a anonimização automática: a partir da versão original do documento, é possível substituir uma anonimização automática já existente, ou anonimizar documentos que ainda não foram processados automaticamente.

### 2.1 Premissas
- O tarjamento manual tem reflexos para usuários internos e externos e também na Consulta Pública Unificada do PJe;
- O documento original não é anonimizado. A secretaria, conforme decisão judicial, desentranha o documento original ou o torna sigiloso;
- O documento tarjado é juntado no PJe com certidão — para isso, o sistema abre a tela de editor de textos para elaboração da certidão e assinatura;
- A anonimização manual não permite retificação. Para ajustes, o usuário baixa o documento original e realiza nova juntada após o devido tratamento;
- Existe a possibilidade de anonimização manual com reflexos exclusivos na Consulta Pública Unificada;
- O documento é sinalizado na árvore do processo como anonimizado manualmente.

### 2.2 Acesso

A partir das tarefas de análise, o processo pode ser encaminhado para a tarefa "Anonimizar Documentos", que inicia o fluxo de anonimização manual.

- Analisar Determinação;
- Analisar Determinação — Urgentes;
- Analisar Processo;
- Analisar Processo — Urgentes.


### 2.3 Fluxo de Uso

**Passo 1 — Busca e seleção de documentos**

A tela inicial permite filtrar os documentos do processo e realizar a busca. O resultado exibe uma tabela com os documentos encontrados, somente nos formatos **PDF, PNG e JPG**.

O número máximo de documentos selecionáveis de uma vez é limitado (padrão: **5**), para evitar tráfego excessivo de dados e processamento pesado no navegador.

**Passo 2 — Gerenciamento da Anonimização**

Dentro da Anonimização Manual, o botão **"Gerenciar Anonimização"** abre um modal com o componente de tarjamento, permitindo:

- Desenhar, desfazer e refazer tarjas nos documentos selecionados;
- Navegar entre páginas de um mesmo documento;
- Redimensionar o tamanho de exibição do documento para facilitar o tarjamento;
- Navegar entre os diferentes documentos selecionados.

O botão **"Finalizar"** só é habilitado depois que todos os documentos selecionados tiverem sido tarjados ao menos uma vez. Após finalizar, não é mais possível desenhar novas tarjas.

**Passo 3 — Destino da anonimização**

Ao clicar em **"Finalizar Anonimização"**, o usuário escolhe entre duas opções:

| Opção | Efeito |
|---|---|
| **Processar para Consulta Pública** | A anonimização vale só para a visualização na Consulta Pública. |
| **Processar para Consulta Pública e PJe** | Gera um novo documento no PJe (com as mesmas características do original, exceto usuário/data de criação), que depende de assinatura de certidão para ser juntado aos autos. |

**Passo 4 — Elaboração da certidão**

Quando a opção escolhida envolve reflexo no PJe, uma segunda tarefa abre o editor de texto com uma minuta de certidão pré-preenchida com os documentos anonimizados. Ao assinar:

- **Anonimização só para Consulta Pública**: o processo é marcado como finalizado; o documento anonimizado passa a ser apresentado na Consulta Pública, seguindo normalmente as demais regras de sigilo já existentes;
- **Anonimização para Consulta Pública e PJe**: o novo documento é assinado com assinatura de sistema e juntado automaticamente, como anexo do documento principal (se houver) ou como anexo da própria certidão (se for documento avulso). A certidão é juntada ao processo e seu movimento de juntada é lançado.

> Se mais de um documento for selecionado, a tela de anonimização é exibida um documento por vez, com botão "próximo"; ao final do último documento, aparecem as opções do Passo 3.

### 2.4 Cancelamento da Anonimização

Em qualquer etapa do fluxo, o usuário pode cancelar o procedimento pelo botão **"Encaminhar para"**.

### 2.5 Visualização nos Autos

Documentos anonimizados, manual ou automaticamente, são exibidos na tela de autos com o mesmo ícone indicativo de anonimização na Consulta Pública Unificada.

### 2.6 Status do Documento

Ao pesquisar documentos para anonimização, o sistema indica a situação atual de cada um:

| Status | Descrição |
|---|---|
| 1 | Documento público |
| 2 | Documento público anonimizado manualmente |
| 3 | Documento público anonimizado de forma automática |
| 4 | Documento não público |
| 5 | Documento não público anonimizado manualmente |
| 6 | Documento não público anonimizado de forma automática |
| 7 | Documento sigiloso |
| 8 | Documento sigiloso anonimizado manualmente |
| 9 | Documento sigiloso anonimizado de forma automática |

---

## 3. Parâmetros de Configuração

| Parâmetro | Descrição |
|---|---|
| `pje:anonimizacao:idModeloCertidaoAnonimizacao` | Identificador do modelo de documento usado para gerar a minuta da certidão de anonimização. |

---

## 4. Glossário

| Termo | Definição |
|---|---|
| Documento Público | Documento disponibilizado na Consulta Pública do PJe. |
| Documento não Público | Documento acessível aos usuários logados no PJe, mas não disponibilizado na Consulta Pública Unificada. |
| Documento Sigiloso | Documento acessível somente a alguns usuários do PJe, conforme configurações de sigilo já existentes. |

> **Observação:** os documentos sigilosos devem ser apresentados na listagem de documentos, pois a ideia não é descartar a possibilidade de anonimizar um documento sigiloso. Isso ocorre porque um documento pode ser sigiloso justamente por conter dados que não podem

