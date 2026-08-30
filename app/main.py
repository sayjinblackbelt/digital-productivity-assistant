"""Digital Productivity Assistant - MVP CLI"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def load_json(path):
    with open(BASE_DIR / path, "r", encoding="utf-8") as file:
        return json.load(file)

def choose_option(prompt, options):
    print("\n" + prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        choice = input("\nEscolha uma opção: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Opção inválida. Tente novamente.")

def ask(prompt, default=""):
    return input("\n" + prompt + "\n> ").strip() or default

def run_text_improvement():
    goal = choose_option("O que você deseja fazer?", ["Corrigir ortografia e gramática", "Melhorar clareza e organização", "Tornar o texto mais profissional", "Resumir ou simplificar um texto"])
    text_input = ask("Cole ou escreva o texto que deseja analisar")
    print("\nANÁLISE E MELHORIA DE TEXTO")
    print("=" * 50)
    if not text_input.strip():
        print("Nenhum texto foi informado.")
        return
    print(f"Objetivo selecionado: {goal}")
    print("Texto recebido com sucesso.")
    if goal == "Corrigir ortografia e gramática":
        print("Orientação: revise ortografia, concordância, pontuação e repetição de palavras.")
    elif goal == "Melhorar clareza e organização":
        print("Orientação: prefira frases diretas, organize as ideias em sequência e elimine informações redundantes.")
    elif goal == "Tornar o texto mais profissional":
        print("Orientação: utilize linguagem objetiva, evite informalidade excessiva e destaque informações importantes.")
    else:
        print("Orientação: mantenha as ideias centrais e reduza detalhes que não contribuem para o objetivo principal.")
    print("\nObservação: a reescrita automática completa será integrada em uma próxima camada do assistente.")

def run_document_formatting():
    goal = choose_option("O que você deseja fazer?", ["Formatar um documento existente", "Criar uma estrutura de documento", "Melhorar a apresentação de um documento"])
    tool = ask("Qual ferramenta você está utilizando?", "Word")
    print("\nFORMATAÇÃO DE DOCUMENTOS")
    print("=" * 50)
    print(f"Ferramenta: {tool}")
    if goal == "Formatar um documento existente":
        print("Checklist: título destacado, estilos consistentes, fonte legível, espaçamento uniforme, alinhamento adequado e revisão de quebras de página.")
    elif goal == "Criar uma estrutura de documento":
        subject = ask("Qual é o assunto ou objetivo do documento?")
        print(f"\nEstrutura sugerida para: {subject}")
        print("1. Título")
        print("2. Introdução ou objetivo")
        print("3. Conteúdo principal")
        print("4. Conclusão ou próximos passos")
    else:
        print("Priorize hierarquia visual, títulos consistentes, espaços em branco e listas quando facilitarem a leitura.")
    print("\nDica: use estilos de título para facilitar a organização e a criação de sumários.")

def run_table_assistant():
    goal = choose_option("O que você deseja fazer?", ["Criar uma nova tabela", "Organizar uma tabela existente", "Preparar dados para análise", "Escolher uma estrutura de tabela"])
    tool = ask("Qual ferramenta você está utilizando?", "Excel")
    print("\nASSISTENTE DE TABELAS")
    print("=" * 50)
    print(f"Ferramenta: {tool}")
    if goal == "Criar uma nova tabela":
        subject = ask("Qual é o assunto principal da tabela? Ex.: controle de alunos")
        fields = ask("Quais informações precisam ser registradas? Separe por vírgula. Ex.: Nome, Turma, Presença")
        print("\nEstrutura sugerida:")
        print(f"Assunto: {subject}")
        for i, field in enumerate(fields.split(","), 1):
            if field.strip(): print(f"{i}. {field.strip()}")
        print("Use uma linha para cabeçalhos e uma linha por registro.")
    elif goal == "Organizar uma tabela existente":
        print("Checklist: cabeçalhos claros, uma informação por coluna, sem células mescladas, sem linhas vazias e formatos padronizados.")
    elif goal == "Preparar dados para análise":
        print("Revise duplicados, padronize formatos, corrija valores inconsistentes e mantenha uma variável por coluna.")
    else:
        print("Modelo básico: uma linha de cabeçalho e uma linha por registro.")
    print("\nDica: planeje primeiro quais perguntas a tabela deverá responder.")

def run_spreadsheet_organization():
    problem = choose_option("Qual problema você deseja resolver?", ["Dados duplicados", "Organizar colunas e cabeçalhos", "Padronizar datas", "Padronizar números", "Separar dados misturados", "Melhorar a estrutura geral"])
    tool = ask("Qual ferramenta você está utilizando?", "Excel")
    print("\nORIENTAÇÃO PRÁTICA")
    print("=" * 50)
    print(f"Ferramenta: {tool}")
    guidance = {
        "Dados duplicados": "Faça uma cópia dos dados, identifique a coluna única e use a remoção de duplicatas. Exemplo: =CONT.SE(A:A;A2)>1",
        "Organizar colunas e cabeçalhos": "Use uma única linha de cabeçalho, nomes claros e uma informação por coluna. Evite células mescladas na base.",
        "Padronizar datas": "Verifique se as datas são valores de data e escolha um formato único, como dd/mm/aaaa.",
        "Padronizar números": "Verifique números armazenados como texto e padronize moeda, porcentagem e casas decimais.",
        "Separar dados misturados": "Identifique o separador e use Texto para Colunas ou funções de divisão.",
        "Melhorar a estrutura geral": "Checklist: cabeçalho único, uma informação por coluna, sem linhas vazias, formatos consistentes e duplicados revisados."
    }
    print(guidance[problem])
    print("\nFaça uma cópia antes de alterações estruturais.")

def run_data_interpretation():
    raw = ask("Informe valores separados por ponto e vírgula. Ex.: 10;15;20")
    values = []
    for item in raw.split(";"):
        try:
            values.append(float(item.strip().replace(",", ".")))
        except ValueError:
            pass
    if not values:
        print("Nenhum valor numérico válido foi informado.")
        return
    choice = choose_option("O que você deseja descobrir?", ["Maior valor", "Menor valor", "Média", "Comparar primeiro e último valor", "Resumo geral"])
    maximum, minimum = max(values), min(values)
    average = sum(values) / len(values)
    print("\nRESULTADO DA ANÁLISE")
    print("=" * 50)
    if choice == "Maior valor":
        print(f"Maior valor: {maximum:g}")
    elif choice == "Menor valor":
        print(f"Menor valor: {minimum:g}")
    elif choice == "Média":
        print(f"Média: {average:.2f}")
    elif choice == "Comparar primeiro e último valor":
        first, last = values[0], values[-1]
        change = last - first
        print(f"Valor inicial: {first:g}")
        print(f"Valor final: {last:g}")
        print(f"Variação absoluta: {change:+g}")
        if first != 0:
            print(f"Variação percentual: {change / first * 100:+.2f}%")
        print("Interpretação: aumento." if change > 0 else "Interpretação: redução." if change < 0 else "Interpretação: sem variação.")
    else:
        print(f"Quantidade: {len(values)}")
        print(f"Menor: {minimum:g}")
        print(f"Maior: {maximum:g}")
        print(f"Média: {average:.2f}")
        print("Interpretação: indicadores básicos; o significado depende do contexto.")

def run_formula_correction():
    tool = ask("Qual ferramenta você está utilizando? Ex.: Excel")
    formula = ask("Qual fórmula está apresentando problema?")
    error = ask("Qual erro aparece? Ex.: #N/D, #VALOR!, #REF!")
    expected = ask("Qual resultado você esperava obter?")
    suggestions = {"#N/D": "O valor procurado pode não existir ou os dados podem ter formatos diferentes.", "#VALOR!": "Verifique argumentos e tipos de dados.", "#REF!": "A fórmula pode apontar para uma referência removida.", "#DIV/0!": "A fórmula está tentando dividir por zero ou por uma célula vazia."}
    print("\nDIAGNÓSTICO INICIAL")
    print("=" * 50)
    print(f"Ferramenta: {tool}")
    print(f"Erro: {error}")
    print(f"Resultado esperado: {expected}")
    print(suggestions.get(error.upper().replace(" ", ""), "Verifique fórmula, intervalos e dados."))
    print("Fórmula informada:", formula)

def run_formula_flow():
    rules = load_json("decision_engine/decision_rules.json")
    responses = load_json("responses/spreadsheet_responses.json")
    category = "Criar uma fórmula"
    options = list(rules["categories"][category]["options"].keys())
    operation_name = choose_option(rules["categories"][category]["question"], options)
    operation = rules["categories"][category]["options"][operation_name]["next"]
    for question in rules["flows"][operation]["questions"]:
        ask(question)
    available = responses.get(operation, {})
    formula = choose_option("Qual solução você deseja gerar?", list(available.keys()))
    if operation == "lookup":
        value = ask("Célula do valor procurado. Ex.: D2", "D2")
        if formula == "PROCV":
            table_range = ask("Intervalo completo da tabela. Ex.: A:B", "A:B")
            column_index = ask("Número da coluna de retorno. Ex.: 2", "2")
            result = f"=PROCV({value};{table_range};{column_index};FALSO)"
        else:
            search_range = ask("Intervalo de busca. Ex.: A:A", "A:A")
            return_range = ask("Intervalo de retorno. Ex.: B:B", "B:B")
            result = f'=PROCX({value};{search_range};{return_range};"Não encontrado")'
    elif operation == "sum":
        if formula == "SOMA":
            result = f'=SOMA({ask("Intervalo a ser somado. Ex.: B2:B100", "B2:B100")})'
        elif formula == "SOMASES":
            sum_range = ask("Intervalo da soma. Ex.: C:C", "C:C")
            criteria_range1 = ask("Primeiro intervalo de critério. Ex.: A:A", "A:A")
            criteria1 = ask("Primeiro critério. Ex.: Vendas", "Vendas")
            criteria_range2 = ask("Segundo intervalo de critério. Ex.: B:B", "B:B")
            criteria2 = ask("Segundo critério. Ex.: Janeiro", "Janeiro")
            result = f'=SOMASES({sum_range};{criteria_range1};"{criteria1}";{criteria_range2};"{criteria2}")'
        else:
            result = f'=SOMASE({ask("Intervalo do critério", "A:A")};"{ask("Critério", "Vendas")}";{ask("Intervalo da soma", "B:B")})'
    elif operation == "count":
        if formula == "CONT.VALORES":
            result = f'=CONT.VALORES({ask("Intervalo a ser contado. Ex.: A2:A100", "A2:A100")})'
        elif formula == "CONT.SES":
            criteria_range1 = ask("Primeiro intervalo de critério. Ex.: A:A", "A:A")
            criteria1 = ask("Primeiro critério. Ex.: Presente", "Presente")
            criteria_range2 = ask("Segundo intervalo de critério. Ex.: B:B", "B:B")
            criteria2 = ask("Segundo critério. Ex.: Manhã", "Manhã")
            result = f'=CONT.SES({criteria_range1};"{criteria1}";{criteria_range2};"{criteria2}")'
        else:
            result = f'=CONT.SE({ask("Intervalo", "A:A")};"{ask("Critério", "Presente")}")'
    elif operation == "condition":
        if formula == "SES":
            condition1 = ask("Primeira condição. Ex.: A2>=9", "A2>=9")
            result1 = ask("Resultado da primeira condição", "Excelente")
            condition2 = ask("Segunda condição. Ex.: A2>=7", "A2>=7")
            result2 = ask("Resultado da segunda condição", "Aprovado")
            default_result = ask("Resultado padrão", "Reprovado")
            result = f'=SES({condition1};"{result1}";{condition2};"{result2}";VERDADEIRO;"{default_result}")'
        elif formula == "E":
            condition1 = ask("Primeira condição. Ex.: A2>=7", "A2>=7")
            condition2 = ask("Segunda condição. Ex.: B2>=75", "B2>=75")
            result = f'=E({condition1};{condition2})'
        elif formula == "OU":
            condition1 = ask("Primeira condição. Ex.: A2>=7", "A2>=7")
            condition2 = ask("Segunda condição. Ex.: B2>=75", "B2>=75")
            result = f'=OU({condition1};{condition2})'
        else:
            result = f'=SE({ask("Condição", "A2>=7")};"{ask("Resultado verdadeiro", "Aprovado")}";"{ask("Resultado falso", "Reprovado")}")'
    else:
        result = ""
    print("\nFÓRMULA PERSONALIZADA")
    print("=" * 50)
    print(result)
    print(available[formula]["explanation"])

def main():
    print("=" * 50)
    print("DIGITAL PRODUCTIVITY ASSISTANT")
    print("MVP — Assistente de Produtividade Digital")
    print("=" * 50)
    options = ["Criar uma fórmula", "Corrigir uma fórmula", "Organizar uma planilha", "Criar ou organizar uma tabela", "Interpretar dados", "Formatar um documento", "Corrigir ou melhorar um texto", "Criar uma resposta ou conteúdo"]
    choice = choose_option("Olá! O que você deseja resolver?", options)
    if choice == "Criar uma fórmula":
        run_formula_flow()
    elif choice == "Corrigir uma fórmula":
        run_formula_correction()
    elif choice == "Organizar uma planilha":
        run_spreadsheet_organization()
    elif choice == "Criar ou organizar uma tabela":
        run_table_assistant()
    elif choice == "Interpretar dados":
        run_data_interpretation()
    elif choice == "Formatar um documento":
        run_document_formatting()
    elif choice == "Corrigir ou melhorar um texto":
        run_text_improvement()
    else:
        print("\nEsta categoria está prevista para as próximas versões.")

if __name__ == "__main__":
    main()
