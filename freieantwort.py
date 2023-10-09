class FreieAntwort:
    def __init__(self):
        self.answer = ""

def questions():
    answer1 = input("Wofür steht OOP? ")
    answer2 = input("Was ist ein String? ")
    return answer1, answer2 

def check_freieantwort():
    while True:
        answer = input("Was ist deine Antwort: ")
        if answer.strip() and not answer.isdigit():  # Use parentheses to call isdigit
            return answer
        else:
            print("Bitte gib eine valide Antwort ein.")

def check_answer(answer1, answer2):
    if answer1.lower() == "objektorientierte programmierung" and answer2.lower() == "zeichenkette":
        return True
    else:
        return False

def main():
    print("Hallo Alice. Hier kannst du freie Antworten geben.")
    answer1, answer2 = questions()
    freie_antwort = FreieAntwort()
    freie_antwort.answer = check_freieantwort()
    print("Deine Antwort: " + freie_antwort.answer)

    if check_answer(answer1, answer2):
        print("Deine Antworten sind korrekt!")
    else:
        print("Deine Antworten sind nicht korrekt.")

if __name__ == "__main__":
    main()
