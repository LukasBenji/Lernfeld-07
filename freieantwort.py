import random


class Frage:

    def __init__(self, frage, antwort):
        self.frage = frage
        self.antwort = antwort


class FreiesAntwortSpiel:

    def __init__(self):
        self.frage_liste = []
        self.selection = Selection()

    def add_question(self, frage, antwort):
        self.frage_liste.append(Frage(frage, antwort))

    def get_random_question(self):
        return random.choice(self.frage_liste)

    def spielen(self):
        print("Hallo Alice. Hier kannst du freie Antworten geben.")
        fragen = self.get_random_question()
        print(fragen.frage)
        antwort = input("Was ist deine Antwort: ")

        antwort = self.check_freieantwort(antwort)
        print("Deine Antwort: " + antwort)

        if antwort.lower() == fragen.antwort:
            print("Antwort ist korrekt!")
        else:
            print("Falsche Antwort. Die richtige Antwort ist:", fragen.antwort)

    def check_freieantwort(self, antwort):
        if antwort.strip() and not antwort.isdigit():
            return antwort
        else:
            return "Bitte gib eine valide Antwort ein."


class Selection:

    def __init__(self):
        self.__option_hover = -1
        self.__option_max = 1
        self.__option_selected = -1

    def get_option_by_hovering(self):
        return self.__option_hover

    def increase_hover(self):
        if self.__option_hover < self.__option_max - 1:
            self.__option_hover += 1

    def decrease_hover(self):
        if self.__option_hover > 0:
            self.__option_hover -= 1

    def get_option_max(self):
        return self.__option_max

    def set_option_max(self, new_max):
        self.__option_max = new_max

    def get_option_selected(self):
        return self.__option_selected

    def set_hover_as_selected(self):
        self.__option_selected = self.__option_hover

    def reset_selection(self):
        self.__option_hover = -1
        self.__option_selected = -1


if __name__ == "__main__":
    spiel = FreiesAntwortSpiel()
    spiel.add_question("Wofür steht OOP? ", "objektorientierte programmierung")
    spiel.add_question("Was ist ein String? ", "zeichenkette")
    spiel.add_question("Was ist ein Integer? ", "Ganzahl")
    spiel.spielen()
