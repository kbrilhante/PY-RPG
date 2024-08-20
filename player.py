from rules import classes, races
from prettytable import PrettyTable
from random import randint


class Player:
    def __init__(self, name, player_race, player_class):
        self.name = name
        self.race = player_race
        self.p_class = player_class
        self.attack = 10 + races[player_race]['attack'] + classes[player_class]['attack']
        self.defense = 10 + races[player_race]['defense'] + classes[player_class]['defense']
        self.magic = 10 + races[player_race]['magic'] + classes[player_class]['magic']
        self.speed = races[player_race]['speed'] + classes[player_class]['speed']
        self.xp = 0
        self.level = 1
        self.health_points = randint(1, classes[player_class]['hp']) + classes[player_class]['hp'] + self.defense
        self.mana_points = randint(1, classes[player_class]['mp']) + classes[player_class]['mp'] + self.magic
        self.gold = 100
        self.inventory = {}

    def print_file(self):
        print(f"\nNAME: {self.name}")
        print(f"{self.p_class}")
        print(f"{self.race}\n")
        print(f"LEVEL: {self.level}")
        # print(f"GOLD: {self.gold}")
        print(f"HP: {self.health_points}")
        print(f"MP: {self.mana_points}")
        table = PrettyTable()
        table.title = "Player Attributes"
        table.field_names = ['Attribute', 'Value']
        table.add_rows([
            ['ATK', self.attack],
            ['DEF', self.defense],
            ['MAG', self.magic],
            ['SPD', self.speed],
        ])
        print(table)
