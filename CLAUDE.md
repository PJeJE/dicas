# Projeto PJe Dicas

## Visão Geral

O **PJe Dicas** é um site de documentação criado pela Assessoria do Processo Judicial Eletrônico (ASPJe/TSE) para compartilhar conhecimento sobre o uso e configuração do sistema PJe na Justiça Eleitoral.

- **URL**: https://pjeje.github.io/dicas/
- **Tecnologia**: Hugo com tema hugo-theme-learn
- **Repositório**: https://github.com/PJeJE/dicas
- **Objetivo**: Padronização de rotinas e divulgação de boas práticas

## Estrutura do Projeto

### Tecnologias Utilizadas
- **Hugo**: Gerador de sites estáticos
- **Tema**: hugo-theme-learn (tema azul)
- **CSS Customizado**: `/static/css/dicas.css`
- **Analytics**: Google Analytics (G-FF8QSSKC39)

### Estrutura de Diretórios

```
/
├── config.toml           # Configuração principal do Hugo
├── content/             # Conteúdo da documentação
│   ├── _index.md        # Página inicial
│   ├── acesso/          # Seção sobre acesso ao sistema
│   ├── advogados/       # Dicas para advogados
│   ├── atos/           # Documentação sobre atos processuais
│   ├── automacao/      # Funcionalidades de automação
│   ├── autos/          # Gestão de autos processuais
│   ├── autuacao/       # Processo de autuação
│   ├── classes/        # Classes processuais
│   ├── consulta/       # Consultas no sistema
│   ├── distribuicao/   # Sistema de distribuição
│   ├── prazos/         # Gestão de prazos
│   ├── procuradorias/  # Específico para procuradorias
│   ├── recursos/       # Gestão de recursos
│   ├── remessa/        # Remessas entre instâncias
│   ├── sessaojulg/     # Sessões de julgamento
│   └── sigilo/         # Gestão de sigilo
├── layouts/            # Templates customizados
├── static/             # Arquivos estáticos (CSS, imagens, docs)
└── themes/             # Tema Hugo
```

### Seções Principais de Conteúdo

1. **Acesso**: Configuração de acesso, certificados, tokens
2. **Advogados**: Orientações específicas para advogados
3. **Atos**: Atos processuais e movimentações
4. **Automação**: Funcionalidades automatizadas (certidões automáticas, etiquetas)
5. **Autos**: Gestão de documentos e variáveis
6. **Autuação**: Processo de autuação e cadastro
7. **Consultas**: Consultas internas e públicas
8. **Distribuição**: Sistema de distribuição processual
9. **Prazos**: Configuração e gestão de prazos
10. **Procuradorias**: Ferramentas específicas
11. **Recursos**: Gestão de recursos processuais
12. **Remessas**: Remessas entre órgãos
13. **Sessões de Julgamento**: Pauta e julgamentos
14. **Sigilo**: Controle de acesso e sigilo

## Comandos Úteis

### Desenvolvimento Local
```bash
# Servir o site localmente
hugo server -D

# Gerar site estático
hugo

# Gerar com tema específico
hugo --theme=hugo-theme-learn
```

### Estrutura de Arquivos
- **Conteúdo**: Arquivos `.md` em `/content/`
- **Imagens**: `/static/imagens/`
- **Documentos**: `/static/docs/`
- **Vídeos**: `/static/videos/`
- **CSS Custom**: `/static/css/dicas.css`

## Funcionalidades Especiais

### Shortcodes Customizados
- `{{<table "variaveismodelo">}}`: Tabelas com estilo específico para variáveis (SEMPRE ordenadas alfabeticamente)
- `{{% notice note %}}`: Avisos e notas importantes
- `{{< relref >}}`: Links internos entre páginas

### Variáveis de Template
O sistema utiliza um conjunto extenso de variáveis para geração automática de documentos, organizadas em:

1. **Variáveis de Uso Geral** (75+ variáveis)
2. **Certidão de Ciência** (6 variáveis específicas)
3. **Certidão de Disponibilização no DJe** (10 variáveis específicas)
4. **Certidão de Publicação no Mural** (10 variáveis específicas)
5. **Habilitação nos Autos** (4 variáveis específicas)

**Características das Variáveis:**
- **REGRA CRÍTICA**: Todas as tabelas com shortcode `{{<table "variaveismodelo">}}` DEVEM estar em ordem alfabética por descrição
- Esta ordenação é obrigatória em qualquer página que use o shortcode "variaveismodelo"
- Variáveis DJe e Mural compartilham a mesma estrutura, diferindo apenas no objeto de serviço (`certidaoDisponibilizacaoDJEService` vs `certidaoPublicacaoMuralService`)
- Localização principal: `/content/autos/documentos/variaveis/_index.md`
- Documentação específica em `/content/automacao/certidao/`

### Certidões Automáticas
O sistema oferece funcionalidades para geração automática de certidões:

1. **Certidão de Ciência** (`certidao_ciencia.md`)
   - Certidão automática de ciência das intimações
   - Disponível a partir da versão 2.1.8.1.59
   - Variáveis específicas para dados de expedição e ciência

2. **Certidão de Disponibilização no DJe** (`certidao_disponibilizacao_dje.md`)
   - Certidão automática após disponibilização no DJe
   - Parâmetros: `idModeloCertidaoDisponibilizacao`, `pje:disponibilizacao:dje:geraCertidao`
   - 10 variáveis específicas incluindo dados do processo

3. **Certidão de Publicação no Mural** (`certidao_mural.md`)
   - Certidão automática após publicação no Mural
   - Parâmetros: `idModeloCertidaoPublicacaoMural`, `pje:publicacao:mural:geraCertidaoPublicacao`
   - 10 variáveis específicas (mesma estrutura do DJe)

4. **Habilitação nos Autos** (`habilitacao_autos.md`)
   - Certidão automática para habilitação de advogados
   - 4 variáveis específicas para dados de habilitação

## Configurações Importantes

### config.toml
- **baseURL**: `https://pjeje.github.io/dicas/`
- **Tema**: `hugo-theme-learn` (variante azul)
- **Idioma**: Português brasileiro
- **Editor**: Links para GitHub para edição colaborativa

### Participação Colaborativa
O projeto aceita contribuições através de formulário Google Forms para sugestões e melhorias.

## Regras Críticas do Projeto

### Ordenação de Tabelas de Variáveis
**REGRA FUNDAMENTAL**: Qualquer tabela que use o shortcode `{{<table "variaveismodelo">}}` DEVE estar ordenada alfabeticamente pela coluna "Descrição".

**Aplicação:**
- Vale para TODAS as páginas do projeto
- Não há exceções para nenhuma seção ou funcionalidade
- Deve ser verificada antes de qualquer commit
- Inclui tanto a página principal de variáveis quanto páginas específicas de certidões

### Formatação de Parâmetros
**PADRÃO OBRIGATÓRIO**: Todos os parâmetros devem seguir o formato específico estabelecido no projeto.

**Estrutura para parâmetros:**
```markdown
- **Parâmetro `nomeDoParametro`**:
  - O valor desse parâmetro deve ser `valor` para habilitar/configurar...
```

**Regras específicas:**
- Nome do parâmetro sempre entre crases: `` `nomeDoParametro` ``
- Valores de parâmetros sempre entre crases: `` `S` `` e `` `N` `` ou `` `true` `` e `` `false` ``
- Usar "habilitar" e "desabilitar" para parâmetros booleanos
- Para parâmetros ID: "corresponde ao ID do modelo de documento"
- Sempre incluir aviso sobre parâmetros ativos e configurados

### Formatação de Shortcodes Notice
**PADRÕES ESTABELECIDOS**: Usar shortcodes notice para avisos importantes.

**Tipos de notice:**
- `{{% notice note %}}` - Informações gerais e orientações
- `{{% notice warning %}}` - Avisos críticos sobre configuração
- `{{% notice info %}}` - Informações complementares

**Localização padrão:**
- Avisos sobre parâmetros: após a lista de parâmetros
- Avisos sobre modelos: após as tabelas de variáveis
- Orientações gerais: no final das seções

### Formatação de Variáveis
**ESTRUTURA OBRIGATÓRIA**: Todas as variáveis devem estar formatadas consistentemente.

**Regras para variáveis:**
- Sempre usar `#{}` para delimitar expressões
- Manter consistência nos nomes de objetos de serviço
- Tabelas sempre com colunas "Descrição" e "Variável"
- Descrições claras e específicas sobre o que cada variável retorna

**Páginas que devem seguir esta regra:**
- `/content/autos/documentos/variaveis/_index.md` (página principal) ✅
- `/content/automacao/certidao/certidao_ciencia.md` ✅
- `/content/automacao/certidao/certidao_disponibilizacao_dje.md` ✅
- `/content/automacao/certidao/certidao_mural.md` ✅
- `/content/automacao/certidao/habilitacao_autos.md` ✅
- Qualquer nova página que contenha variáveis de modelo

**Status atual**: Todas as páginas listadas foram verificadas e estão em conformidade com a regra de ordenação alfabética (última verificação: 2025-01-10).

## Manutenção

### Atualizações de Conteúdo
- Editar arquivos `.md` em `/content/`
- Adicionar imagens em `/static/imagens/`
- Documentos PDF em `/static/docs/`

### Boas Práticas para Variáveis
- **Ordenação OBRIGATÓRIA**: Todas as tabelas `{{<table "variaveismodelo">}}` devem estar em ordem alfabética por descrição
- **Aplicação Universal**: Esta regra se aplica a QUALQUER página que use o shortcode "variaveismodelo"
- **Verificação**: Sempre verificar ordenação antes de salvar alterações
- **Sincronização**: Manter sincronizadas as variáveis entre DJe e Mural
- **Documentação**: Atualizar tanto os arquivos específicos quanto o índice principal
- **Consistência**: Usar nomenclatura consistente para objetos de serviço
- **Validação**: Testar variáveis antes de incluir na documentação

### Padrões de Texto Estabelecidos
**FRASES PADRÃO**: Usar terminologia consistente em todo o projeto.

**Texto introdutório para variáveis:**
```markdown
No modelo de documento podem ser utilizadas as seguintes variáveis para recuperação de informações:
```

**Aviso padrão sobre parâmetros:**
```markdown
{{% notice note %}}
Para a correta utilização da funcionalidade, todos os parâmetros devem estar **ativos** e devidamente configurados.
{{% /notice %}}
```

**Aviso padrão sobre ID de modelo:**
```markdown
{{% notice warning %}}
O ID do modelo de documento informado no parâmetro `nomeParametro` deve fazer referência a um modelo de documento válido e ativo. Caso contrário, a certidão automática não será juntada ao processo.
{{% /notice %}}
```

### Publicação
O site é gerado automaticamente e publicado no GitHub Pages quando há commits no repositório principal.

## Contato e Suporte

**Responsável**: Assessoria do Processo Judicial Eletrônico (ASPJe/TSE)

Para contribuições e sugestões, utilizar o formulário de participação disponível no próprio site.