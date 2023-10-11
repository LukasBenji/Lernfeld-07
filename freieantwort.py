import random

class Frage:
    def __init__(self, frage, antwort):
        self.frage = frage
        self.antwort = antwort

class FreiesAntwortSpiel:
    def __init__(self):
        self.frage_liste = []
        self.frage_liste.append(Frage("Wofür steht OOP? ", "objektorientierte programmierung"))
        self.frage_liste.append(Frage("Was ist ein String? ", "zeichenkette"))
        self.frage_liste.append(Frage("Was ist ein Integer? ", "Ganzahl"))

    def get_random_question(self):
        return random.choice(self.frage_liste)

    def check_freieantwort(self, antwort):
        if antwort.strip() and not antwort.isdigit():
            return antwort
        else:
            return "Bitte gib eine valide Antwort ein."

    def spielen(self):
        print("Hallo Alice. Hier kannst du freie Antworten geben.")
        frage_obj = self.get_random_question()
        print(frage_obj.frage)
        antwort = input("Was ist deine Antwort: ")
        antwort = self.check_freieantwort(antwort)
        print("Deine Antwort: " + antwort)

        if antwort.lower() == frage_obj.antwort:
            print("Deine Antwort ist korrekt!")
        else:
            print("Deine Antwort ist nicht korrekt. Die richtige Antwort ist:", frage_obj.antwort)

if __name__ == "__main__":
    spiel = FreiesAntwortSpiel()
    spiel.spielen()
