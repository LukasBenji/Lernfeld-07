class FreieAntwort:

    def __init__(self):
        self.answer = ""

def check_freieantwort():
    while True:
        answer = input("What is your answer: ")
        if answer:
            break
        elif not answer.isalnum():
            print("Bitte geben Sie eine valide Eingabe ein.")
        else:
            print("Bitte geben Sie etwas ein.")

def main():
    check_freieantwort()

if __name__ == "__main__":
    main()
