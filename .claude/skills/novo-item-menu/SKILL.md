---
name: novo-item-menu
description: Cria um novo item de menu de primeiro nível (capítulo / pasta em content/ com _index.md chapter=true) a partir de um title informado e realinha weight, pre e o número da "### Seção" de todos os capítulos para manter a ordem alfabética dos titles. Use quando o usuário pedir para adicionar/criar uma nova seção, capítulo ou item de menu no site Dicas, ou para reordenar/realinhar os pesos do menu em ordem alfabética.
---

# Criar novo item de menu mantendo a ordem alfabética

No site Dicas (Hugo + hugo-theme-learn), cada pasta em `content/` com
`_index.md` contendo `chapter = true` vira um item do menu lateral. A posição
no menu é dada por `weight`, e o número exibido ao lado do título vem de
`pre = "<b>N. </b>"`. O corpo ainda traz `### Seção N`, que deve casar com o
mesmo número.

Esta skill garante que, ao adicionar um novo capítulo, **todos** os capítulos
fiquem renumerados (`weight`, `pre` e `### Seção`) seguindo a **ordem
alfabética dos titles** (acento-insensível, em português), sem buracos,
de 1 a N.

## Como usar

O trabalho pesado é feito por `reorder.py` (mesma pasta desta skill).

### 1. Coletar os dados do novo item
- **title**: peça ao usuário o título exato (ex.: `"Sessão de Julgamento"`).
- **slug** (nome da pasta): se o usuário não informar, o script deriva um slug
  do title (minúsculas, sem acentos, só letras/números). Os slugs existentes
  costumam ser semânticos e curtos (`acesso`, `automacao`, `peticionamento`),
  então **prefira confirmar o nome da pasta com o usuário** em vez de aceitar o
  default cegamente.

### 2. Pré-visualizar (recomendado)
```bash
python3 .claude/skills/novo-item-menu/reorder.py --create --title "TITULO" --slug SLUG --dry-run
```
Mostra a ordem final e onde o novo item entraria, **sem gravar nada**. Confirme
com o usuário se a posição ficou como esperado.

### 3. Aplicar
```bash
python3 .claude/skills/novo-item-menu/reorder.py --create --title "TITULO" --slug SLUG
```
Isso:
- cria `content/SLUG/_index.md` com o front matter padrão (`chapter = true`,
  `date` = agora, corpo com `# TITULO` e `{{% children %}}`);
- recalcula a ordem alfabética de todos os capítulos;
- reescreve `weight`, `pre` e `### Seção` de cada `_index.md` para o novo número.

### Apenas realinhar (sem criar)
Se o usuário só quer reordenar os pesos existentes em ordem alfabética:
```bash
python3 .claude/skills/novo-item-menu/reorder.py
```

## Depois de rodar
- Mostre ao usuário a tabela final (a saída do script já lista `# | pasta | title`).
- Informe quantos arquivos foram alterados.
- Pergunte se deve rodar `hugo` para validar a build e/ou fazer o commit
  (não commite sem o usuário pedir).

## Observações
- Só mexe em pastas cujo `_index.md` tem `chapter = true`.
- A numeração resultante é sempre contígua (1..N) — corrige eventuais buracos
  de weight e números de `### Seção` defasados que existam.
- Edição cirúrgica: só as linhas `weight`, `pre` e `### Seção` são tocadas; o
  restante do arquivo é preservado.
