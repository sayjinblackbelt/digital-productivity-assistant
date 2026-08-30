"""
Digital Productivity Assistant - MVP CLI

Structured conversational prototype for spreadsheet productivity support.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def load_json(relative_path):
    with open(BASE_DIR / relative_path, "r", encoding="utf-8") as file:
        return json.load(file)


def choose_option(prompt, options):
    print(f"\n{prompt}")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    while True:
        choice = input("\nEscolha uma opção: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]

        print("Opção inválida. Tente novamente.")


def collect_context(questions):
    answers = {}

    for question in questions:
        answers[question] = input(f"\n{question}\n> ").strip()

    return answers


def show_recommendations(operation, rules, responses):
    recommendations = rules["flows"][operation]["recommendations"]

    print("\nPossíveis soluções:")

    for recommendation in recommendations:
        print(f"- {recommendation}")

    available = responses.get(operation, {})

    if available:
        print("\nModelos disponíveis:")

        for formula, details in available.items():
            print(f"\n{formula}")
            print(f"Modelo: {details['template']}")
            print(f"Explicação: {details['explanation']}")


def run_formula_flow():
    rules = load_json("decision_engine/decision_rules.json")
    responses = load_json("responses/spreadsheet_responses.json")

    category = "Criar uma fórmula"
    options = list(rules["categories"][category]["options"].keys())

    operation_name = choose_option(
        rules["categories"][category]["question"],
        options
    )

    operation = rules["categories"][category]["options"][operation_name]["next"]

    questions = rules["flows"][operation]["questions"]

    print("\nVamos entender melhor sua necessidade.")
    answers = collect_context(questions)

    print("\nContexto informado:")

    for question, answer in answers.items():
        print(f"- {question}: {answer}")

    show_recommendations(operation, rules, responses)


def main():
    print("=" * 50)
    print("DIGITAL PRODUCTIVITY ASSISTANT")
    print("MVP — Assistente de Produtividade Digital")
    print("=" * 50)

    main_options = [
        "Criar uma fórmula",
        "Corrigir uma fórmula",
        "Organizar uma planilha",
        "Criar ou organizar uma tabela",
        "Interpretar dados",
        "Formatar um documento",
        "Corrigir ou melhorar um texto",
        "Criar uma resposta ou conteúdo"
    ]

    choice = choose_option(
        "Olá! O que você deseja resolver?",
        main_options
    )

    if choice == "Criar uma fórmula":
        run_formula_flow()
    else:
        print("\nEsta categoria está prevista para as próximas versões.")
        print("Obrigado por testar o MVP!")


if __name__ == "__main__":
    main()
