# Decision Engine — MVP

## Visão geral

A primeira versão do Digital Productivity Assistant não depende de IA generativa.

Ela utiliza uma sequência estruturada:

```text
Necessidade
    ↓
Categoria
    ↓
Operação
    ↓
Perguntas específicas
    ↓
Contexto
    ↓
Regra
    ↓
Recomendação
    ↓
Resposta
```

## Exemplo: busca de informações

Usuário:

> Quero buscar um telefone pelo nome.

O sistema identifica:

- categoria: planilhas;
- intenção: criar fórmula;
- operação: procurar valor.

Perguntas:

1. Qual ferramenta está utilizando?
2. Onde está o nome?
3. Onde está o telefone?
4. Qual célula contém o valor que será procurado?

Com o contexto completo, o mecanismo pode montar uma resposta.

Exemplo:

```excel
=PROCX(D2;A:A;B:B;"Não encontrado")
```

## Vantagem da abordagem

A lógica estruturada permite:

- respostas previsíveis;
- fácil teste;
- evolução gradual;
- reutilização das regras;
- futura integração com IA.

A IA pode futuramente interpretar mensagens livres, enquanto o Decision Engine continua responsável pela organização das regras e decisões.
