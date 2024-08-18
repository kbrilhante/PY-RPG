from rules import *
from player import Player

print(list(races))
print(classes)


def get_choice(question, data):
    for i, choice in enumerate(data):
        question += f"\n{i + 1} - {choice.title()}"
    question += "\n> "
    while True:
        try:
            opt = int(input(question))
            if 1 <= opt <= len(data):
                return data[opt - 1]
            print(f"Pick a number between 1 and {len(data)}")
        except ValueError:
            print("Invalid option. Your choice needs to be a number")


def char_builder():
    name = input("What is your name?\n> ").strip().title()
    race = get_choice("What is your race?", list(races))
    p_class = get_choice("What is your class?", list(classes))
    p = Player(name, race, p_class)
    p.print_file()
    return p


# noinspection SpellCheckingInspection
player = char_builder()
