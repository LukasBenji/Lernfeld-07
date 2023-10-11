import random

class FreieAntwort:
    def __init__(self):
        self.answer = ""

def get_random_question():
    questions = [
        ("Wofür steht OOP? ", "objektorientierte programmierung"),
        ("Was ist ein String? ", "zeichenkette"),
        ("Was ist ein Integer", "Ganzahl")
    ]
    return random.choice(questions)


def check_freieantwort():
    while True:
        answer = input("Was ist deine Antwort: ")
        if answer.strip() and not answer.isdigit():
            return answer
        else:
            print("Bitte gib eine valide Antwort ein.")


def main():
    print("Hallo Alice. Hier kannst du freie Antworten geben.")
    question, right_answer = get_random_question()
    print(question)

    freie_antwort = FreieAntwort()
    freie_antwort.answer = check_freieantwort()
    print("Deine Antwort: " + freie_antwort.answer)

    if freie_antwort.answer.lower() == right_answer:
        print("Deine Antwort ist korrekt!")
    else:
        print("Deine Antwort ist nicht korrekt. Die richtige Antwort ist:", right_answer)


if __name__ == "__main__":
    main()
