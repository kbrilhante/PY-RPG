experience = [
    0,
    300,
    900,
    2700,
    6500,
    14000,
    23000,
    34000,
    48000,
    64000,
    85000,
    100000,
    120000,
    140000,
    165000,
    195000,
    225000,
    265000,
    305000,
    355000
]
races = {
    "Dragonborn": {
        'attack': 0,
        'defense': 1,
        'magic': 2,
        'speed': 30,
    },
    "Dwarf": {
        'attack': 1,
        'defense': 2,
        'magic': 1,
        'speed': 25,
    },
    "Elf": {
        'attack': 2,
        'defense': 0,
        'magic': 1,
        'speed': 30,
    },
    "Gnome": {
        'attack': 1,
        'defense': 1,
        'magic': 2,
        'speed': 25,
    },
    "Half-Elf": {
        'attack': 1,
        'defense': 0,
        'magic': 2,
        'speed': 30,
    },
    "Halfling": {
        'attack': 2,
        'defense': 2,
        'magic': 0,
        'speed': 25,
    },
    "Half-Orc": {
        'attack': 2,
        'defense': 1,
        'magic': 0,
        'speed': 30,
    },
    "Human": {
        'attack': 1,
        'defense': 1,
        'magic': 1,
        'speed': 30,
    },
    "Thiefling": {
        'attack': 0,
        'defense': 0,
        'magic': 3,
        'speed': 30,
    },
}

classes = {
    "Barbarian": {
        'hp': 14,
        'mp': 6,
        'attack': 4,
        'defense': 0,
        'magic': 0,
        'speed': 0,
    },
    "Druid": {
        'hp': 8,
        'mp': 12,
        'attack': 0,
        'defense': 2,
        'magic': 2,
        'speed': 0,
    },
    "Fighter": {
        'hp': 12,
        'mp': 8,
        'attack': 1,
        'defense': 3,
        'magic': 0,
        'speed': 0,
    },
    "Rogue": {
        'hp': 10,
        'mp': 8,
        'attack': 2,
        'defense': 1,
        'magic': 0,
        'speed': 10,
    },
    "Wizard": {
        'hp': 6,
        'mp': 14,
        'attack': 0,
        'defense': 0,
        'magic': 4,
        'speed': 0,
    },

}
monsters = {
    # damage inflicted = hit + hit_dice + skill
    # damage defended = armor + defense
    "Baboon": {
        'level': 0,
        'xp': 10,
        'armor': 12,
        # 1d6
        'hp_amt': 1,
        'hp_dice': 6,
        'hp_modifier': 0,
        'speed': 30,
        'attack': 11,
        'defense': 11,
        'magic': 8,
        'gold': 6,
        'actions': {
            'bite': {
                'type': 'melee',
                'weapon_modifier': 1,
                'hit_amt': 1,
                'hit_dice': 4,
                'hit_modifier': -1,
            },
        },
        'spells': {},
    },
    "Badger": {
        'level': 0,
        'xp': 10,
        'armor': 10,
        'hp_amt': 1,
        'hp_dice': 4,
        'hp_modifier': 1,
        'speed': 20,
        'attack': 8,
        'defense': 12,
        'magic': 7,
        'gold': 5,
        'actions': {
            'bite': {
                'type': 'melee',
                'weapon_modifier': 2,
                'hit_amt': 0,
                'hit_dice': 0,
                'hit_modifier': 1,
            },
        },
        'spells': {},
    },
    "Bat": {
        'level': 0,
        'xp': 10,
        'armor': 12,
        'hp_amt': 1,
        'hp_dice': 4,
        'hp_modifier': -1,
        'speed': 30,
        'attack': 9,
        'defense': 8,
        'magic': 7,
        'gold': 5,
        'actions': {
            'bite': {
                'type': 'melee',
                'weapon_modifier': 0,
                'hit_amt': 0,
                'hit_dice': 0,
                'hit_modifier': 1,
            },
        },
        'spells': {},
    },
    "Hyena": {
        'level': 0,
        'xp': 10,
        'armor': 11,
        'hp_amt': 1,
        'hp_dice': 8,
        'hp_modifier': 1,
        'speed': 50,
        'attack': 12,
        'defense': 12,
        'magic': 7,
        'gold': 7,
        'actions': {
            'bite': {
                'type': 'melee',
                'weapon_modifier': 2,
                'hit_amt': 1,
                'hit_dice': 6,
                'hit_modifier': 0,
            },
        },
        'spells': {},
    },
    "Rat": {
        'level': 0,
        'xp': 10,
        'armor': 10,
        'hp_amt': 1,
        'hp_dice': 4,
        'hp_modifier': -1,
        'speed': 20,
        'attack': 7,
        'defense': 9,
        'magic': 7,
        'gold': 5,
        'actions': {
            'bite': {
                'type': 'melee',
                'weapon_modifier': 0,
                'hit_amt': 0,
                'hit_dice': 0,
                'hit_modifier': 1,
            },
        },
        'spells': {},
    },
    "Giant Rat": {
        'level': 1/8,
        'xp': 25,
        'armor': 12,
        'hp_amt': 2,
        'hp_dice': 6,
        'hp_modifier': 0,
        'speed': 30,
        'attack': 11,
        'defense': 11,
        'magic': 6,
        'gold': 20,
        'actions': {
            'bite': {
                'type': 'melee',
                'weapon_modifier': 4,
                'hit_amt': 1,
                'hit_dice': 4,
                'hit_modifier': 2,
            },
        },
        'spells': {},
    },
    "Kobold": {
        'level': 1/8,
        'xp': 25,
        'armor': 12,
        'hp_amt': 2,
        'hp_dice': 6,
        'hp_modifier': -2,
        'speed': 30,
        'attack': 11,
        'defense': 9,
        'magic': 8,
        'gold': 20,
        'actions': {
            'dagger': {
                'type': 'melee',
                'weapon_modifier': 4,
                'hit_amt': 1,
                'hit_dice': 4,
                'hit_modifier': 2,
            },
            'sling': {
                'type': 'range',
                'weapon_modifier': 4,
                'hit_amt': 1,
                'hit_dice': 4,
                'hit_modifier': 2,
            },
        },
        'spells': {},
    },
    "Acolyte": {
        'level': 1/4,
        'xp': 50,
        'armor': 10,
        'hp_amt': 2,
        'hp_dice': 8,
        'hp_modifier': 0,
        'speed': 30,
        'attack': 10,
        'defense': 10,
        'magic': 12,
        'gold': 50,
        'actions': {
            'club': {
                'type': 'melee',
                'weapon_modifier': 2,
                'hit_amt': 1,
                'hit_dice': 4,
                'hit_modifier': 0,
            },
            'sacred flame': {
                'type': 'spell',
                'weapon_modifier': 0,
                'hit_amt': 1,
                'hit_dice': 8,
                'hit_modifier': 0,
            },
        },
        'spells': {
            'cure wounds': {
                'hp': 4
            }
        },
    },
    "Boar": {
        'level': 1 / 4,
        'xp': 50,
        'armor': 11,
        'hp_amt': 2,
        'hp_dice': 8,
        'hp_modifier': 2,
        'speed': 40,
        'attack': 12,
        'defense': 12,
        'magic': 6,
        'gold': 30,
        'actions': {
            'tusk': {
                'type': 'melee',
                'weapon_modifier': 3,
                'hit_amt': 1,
                'hit_dice': 6,
                'hit_modifier': 1,
            },
        },
        'spells': {},
    },
    "Goblin": {
        'level': 1 / 4,
        'xp': 50,
        'armor': 15,
        'hp_amt': 2,
        'hp_dice': 6,
        'hp_modifier': 0,
        'speed': 30,
        'attack': 11,
        'defense': 10,
        'magic': 9,
        'gold': 40,
        'actions': {
            # type - melee, range or magic
            'scimitar': {
                'type': 'melee',
                'weapon_modifier': 4,
                'hit_amt': 1,
                'hit_dice': 6,
                'hit_modifier': 2,
            },
            'shortbow': {
                'type': 'range',
                'weapon_modifier': 4,
                'hit_amt': 1,
                'hit_dice': 6,
                'hit_modifier': 2,
            },
        },
        'spells': {},
    },
}
