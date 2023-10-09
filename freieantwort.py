class FreieAntwort:
    def __init__(self):
        self.answer = ""

def check_freieantwort():
    while True:
        answer = input("Was ist deine Antwort: ")
        if answer.strip():
            return answer
        else:
            print("Bitte gib eine valide Antwort ein.")

def main():
    print("Hallo Alice. Hier kannst du freie Antworten geben.")
    freie_antwort = FreieAntwort()
    freie_antwort.answer = check_freieantwort()
    print("Deine Antwort: " + freie_antwort.answer)

if __name__ == "__main__":
    main()
