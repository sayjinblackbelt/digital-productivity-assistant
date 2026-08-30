# 🚀 Digital Productivity Assistant

🇧🇷 Português | [🇺🇸 English](README.en.md) | [🇪🇸 Español](README.es.md)

> Assistente conversacional para produtividade digital, ajudando usuários com documentos, planilhas, fórmulas, correções, tabelas, respostas prontas e interpretação de dados.

## 📌 Sobre o projeto

O **Digital Productivity Assistant** é um projeto em desenvolvimento criado para ajudar pessoas a resolver demandas específicas relacionadas ao uso de ferramentas de produtividade digital.

A proposta surgiu a partir de situações recorrentes em que pessoas solicitavam ajuda para resolver problemas no computador, desde dúvidas sobre documentos e planilhas até demandas técnicas mais específicas. Esse padrão de necessidades também levou à realização de **consultorias online personalizadas**.

Ao observar que muitas dúvidas se repetiam, surgiu a ideia de criar uma ferramenta simples e autônoma que pudesse identificar a necessidade do usuário por meio de perguntas, solicitar contexto adicional e entregar uma solução prática.

O projeto também poderá servir como base para versões educacionais simplificadas e para apoio em consultorias personalizadas.

## 🎯 Objetivo

Ajudar o usuário a resolver um problema específico sem exigir que ele conheça profundamente toda a ferramenta utilizada.

O assistente busca:

- identificar a necessidade;
- compreender o contexto;
- fazer perguntas complementares;
- fornecer fórmulas e exemplos;
- corrigir ou explicar soluções;
- organizar informações;
- gerar tabelas;
- produzir respostas prontas;
- interpretar dados;
- orientar passo a passo.

## 💬 Como funciona

```text
USUÁRIO
   ↓
Pergunta ou necessidade inicial
   ↓
Identificação da categoria
   ↓
Perguntas complementares
   ↓
Coleta de contexto
   ↓
Contexto suficiente?
   │
   ├── NÃO → nova pergunta
   │
   └── SIM
         ↓
    SOLUÇÃO PRÁTICA
         │
         ├── Fórmula
         ├── Correção
         ├── Tabela
         ├── Resposta pronta
         ├── Passo a passo
         └── Interpretação de dados
```

## 🧩 MVP inicial

A primeira versão parte de um fluxo estruturado de perguntas.

Exemplo:

### 1. Qual ferramenta você está utilizando?

- Excel
- Google Sheets
- LibreOffice Calc
- Word
- Google Docs
- LibreOffice Writer

### 2. Qual é sua necessidade?

- Criar uma fórmula
- Corrigir uma fórmula
- Organizar dados
- Criar uma tabela
- Formatar um documento
- Corrigir ou melhorar um texto
- Interpretar dados
- Criar uma resposta pronta

A partir da escolha, o assistente faz perguntas específicas para compreender o problema.

## 📊 Assistente de planilhas

Possíveis demandas:

- PROCV;
- PROCX;
- PROCH;
- SE;
- SOMASE;
- SOMASES;
- CONT.SE;
- CONT.SES;
- filtros;
- organização de tabelas;
- limpeza de dados;
- cálculos;
- indicadores;
- gráficos;
- interpretação de resultados.

### Exemplo

**Usuário:**

> Quero buscar o nome de uma pessoa em outra tabela.

**Assistente:**

> Qual coluna contém o valor de busca e qual informação você deseja retornar?

Depois de obter o contexto, o sistema pode fornecer uma fórmula adequada e explicar seu funcionamento.

## 📝 Assistente de documentos

Possíveis demandas:

- formatação;
- estilos;
- títulos;
- parágrafos;
- espaçamento;
- tabelas;
- organização do conteúdo;
- revisão estrutural;
- melhoria de textos;
- modelos e respostas prontas.

O objetivo não é apenas explicar onde clicar, mas ajudar o usuário a chegar a uma solução aplicável.

## 📈 Interpretação de dados

O assistente poderá ajudar a:

- identificar tendências;
- comparar períodos;
- encontrar valores relevantes;
- calcular evolução;
- sugerir indicadores;
- resumir resultados;
- transformar dados em interpretações compreensíveis.

## 🧠 Princípio de design

> **As pessoas frequentemente não precisam aprender toda a ferramenta naquele momento. Elas precisam resolver um problema específico.**

Por isso, o projeto prioriza:

- simplicidade;
- perguntas objetivas;
- contexto antes da resposta;
- soluções aplicáveis;
- explicações claras;
- evolução progressiva.

## 🏗️ Evolução planejada

```text
V1
Perguntas estruturadas
        ↓
V2
Árvore de decisão
        ↓
V3
Base de conhecimento
        ↓
V4
Interpretação de linguagem natural
        ↓
V5
Assistente conversacional especializado
```

## 👥 Possíveis aplicações

### 🎓 Educação

Versões simplificadas podem apoiar educandos no desenvolvimento de competências digitais relacionadas a:

- documentos;
- planilhas;
- fórmulas;
- organização de informações;
- interpretação de dados.

### 💻 Consultorias personalizadas

A ferramenta poderá apoiar atendimentos relacionados a:

- dúvidas recorrentes;
- soluções para documentos;
- planilhas;
- fórmulas;
- organização de dados;
- orientações passo a passo.

### 👤 Uso individual

Usuários podem consultar a ferramenta para resolver necessidades específicas de produtividade digital.

## 🛠️ Arquitetura conceitual

```text
DIGITAL PRODUCTIVITY ASSISTANT
│
├── 💬 Conversation Layer
│
├── 🧠 Decision Engine
│
├── 📚 Knowledge Base
│
├── 📊 Spreadsheet Assistant
│
├── 📝 Document Assistant
│
├── 📈 Data Interpretation
│
└── 🎓 Guided Learning
```

## 🗂️ Estrutura planejada

```text
digital-productivity-assistant/
│
├── README.md
├── README.en.md
├── README.es.md
│
├── docs/
│   ├── PROJECT_ORIGIN.md
│   ├── ARCHITECTURE.md
│   ├── CONVERSATION_FLOW.md
│   └── ROADMAP.md
│
├── knowledge/
│   ├── spreadsheets/
│   └── documents/
│
├── app/
│   ├── questions/
│   ├── decision_engine/
│   └── responses/
│
└── sample_data/
```

## 🚧 Status

**Origem:** demandas recorrentes de suporte e consultorias personalizadas  
**Projeto iniciado:** 2026  
**Status:** 🟡 Em desenvolvimento  
**Fase atual:** MVP CLI funcional e expansão dos módulos de planilhas

## 💻 MVP executável

A primeira implementação funcional utiliza uma interface de linha de comando (CLI).

Execute:

\`\`\`bash
python app/main.py
\`\`\`

Fluxo atual:

\`\`\`text
Escolher necessidade
        ↓
Criar uma fórmula
        ↓
Escolher operação
        ↓
Responder perguntas específicas
        ↓
Consultar regras
        ↓
Exibir recomendações e modelos
\`\`\`

A primeira implementação é propositalmente simples e utiliza arquivos JSON como base de regras e respostas.

## 🗺️ Próximos passos

- [x] Documentar as perguntas iniciais.
- [x] Criar o fluxo inicial de decisão.
- [x] Definir categorias prioritárias.
- [x] Criar a primeira base de respostas.
- [x] Implementar geração inicial de fórmulas.
- [ ] Criar casos de documentos.
- [x] Adicionar interpretação básica de dados.
- [ ] Criar interface inicial.
- [ ] Testar com usuários.
- [ ] Evoluir para diálogo baseado em linguagem natural.

## 🔒 Privacidade

O projeto não deve armazenar ou publicar documentos pessoais, planilhas confidenciais, credenciais, tokens ou chaves de API.

Exemplos públicos devem utilizar dados fictícios ou anonimizados.

## 👨‍💻 Autor

**Filipe G Morais**

Projeto autoral em desenvolvimento, inspirado por demandas reais de suporte tecnológico, educação digital e consultorias personalizadas.


## MVP Status

### Funcional
- Criar fórmulas: PROCX, PROCV, SOMA, SOMASE, SOMASES, CONT.VALORES, CONT.SE, CONT.SES, SE, SES, E e OU.
- Correção inicial de fórmulas.
- Organização de planilhas.
- Criação e organização de tabelas.
- Interpretação básica de dados.
- Formatação de documentos.

### Estrutura inicial
- Melhoria de textos: atualmente fornece orientação; reescrita automática é uma evolução futura.
- Criação de respostas e conteúdo: atualmente fornece estrutura; geração automática é uma evolução futura.

## Próximos passos
1. Testes de cenários reais.
2. Melhorar profundidade dos módulos de texto e conteúdo.
3. Adicionar uma camada de IA.
4. Avaliar interface gráfica.


## 🌐 Versão Web para testes

Foi adicionada uma versão web estática para testes com educandos.

- Interface responsiva para computador e celular.
- 8 categorias principais do MVP.
- Fluxos guiados por perguntas.
- Geração de resultados básicos para fórmulas e interpretação de dados.
- Botão para copiar resultados.
- Canal de feedback via GitHub Issues.

### Como testar localmente

Abra o arquivo `index.html` em um navegador ou publique o repositório usando GitHub Pages.

A versão web é um protótipo de validação educacional e não coleta dados pessoais.

---

## Author

**Filipe G Morais**

GitHub: https://github.com/sayjinblackbelt  
Repository: https://github.com/sayjinblackbelt/digital-productivity-assistant
