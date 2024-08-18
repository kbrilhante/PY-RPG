from rules import classes, races
from prettytable import PrettyTable
from random import randint


class Player:
    def __init__(self, name, player_race, player_class):
        self.name = name
        self.race = player_race
        self.p_class = player_class
        self.attack = 10 + races[player_race]['attack']
        self.defense = 10 + races[player_race]['defense']
        self.magic = 10 + races[player_race]['magic']
        self.speed = races[player_race]['speed']
        self.health_points = randint(1, classes[player_class]['hp']) + classes[player_class]['hp'] + self.defense
        self.mana_points = randint(1, classes[player_class]['mp']) + classes[player_class]['mp'] + self.magic
        self.gold = randint(1, 20) * 10
        self.inventory = {}

    def print_file(self):
        print(f"\nNAME: {self.name}")
        print(f"{self.p_class}")
        print(f"{self.race}\n")
        # print(f"GOLD: {self.gold}")
        print(f"HP: {self.health_points}")
        print(f"MP: {self.mana_points}")
        table = PrettyTable()
        table.field_names = ['Attribute', 'Value']
        table.add_rows([
            ['ATK', self.attack],
            ['DEF', self.defense],
            ['MAG', self.magic],
            ['SPD', self.speed],
        ])
        print(table)
