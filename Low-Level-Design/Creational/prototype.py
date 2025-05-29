import copy
from typing import Dict, List


class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

    def __str__(self):
        return f"{self.name} (Damage: {self.damage}, Durability: {self.durability})"


class Character:
    def __init__(self, name, character_class, level=1):
        self.name = name
        self.character_class = character_class
        self.level = level
        self.stats = {
            "health": 100,
            "mana": 50,
            "strength": 10,
            "intelligence": 10,
            "agility": 10,
        }
        self.equipment = {"weapon": None, "armor": None, "accessories": []}
        self.skills = []
        self.inventory = []

    def clone(self):
        """Create a deep copy of this character"""
        return copy.deepcopy(self)

    def level_up(self):
        self.level += 1
        # Increase stats based on class
        if self.character_class == "Warrior":
            self.stats["health"] += 20
            self.stats["strength"] += 3
        elif self.character_class == "Mage":
            self.stats["mana"] += 15
            self.stats["intelligence"] += 3
        elif self.character_class == "Rogue":
            self.stats["agility"] += 3
            self.stats["health"] += 10

    def equip_weapon(self, weapon):
        self.equipment["weapon"] = weapon

    def add_skill(self, skill):
        self.skills.append(skill)

    def __str__(self):
        weapon_str = (
            str(self.equipment["weapon"]) if self.equipment["weapon"] else "None"
        )
        return (
            f"{self.name} - {self.character_class} (Level {self.level})\n"
            f"Stats: {self.stats}\n"
            f"Weapon: {weapon_str}\n"
            f"Skills: {self.skills}"
        )


# Character Templates/Prototypes
class CharacterPrototypes:
    def __init__(self):
        self.prototypes = {}
        self._create_prototypes()

    def _create_prototypes(self):
        # Warrior prototype
        warrior = Character("Template Warrior", "Warrior")
        warrior.stats.update({"health": 150, "strength": 15, "agility": 8})
        warrior.equip_weapon(Weapon("Iron Sword", 25, 100))
        warrior.add_skill("Slash")
        warrior.add_skill("Block")
        self.prototypes["warrior"] = warrior

        # Mage prototype
        mage = Character("Template Mage", "Mage")
        mage.stats.update({"health": 80, "mana": 120, "intelligence": 18})
        mage.equip_weapon(Weapon("Magic Staff", 15, 80))
        mage.add_skill("Fireball")
        mage.add_skill("Heal")
        self.prototypes["mage"] = mage

        # Rogue prototype
        rogue = Character("Template Rogue", "Rogue")
        rogue.stats.update({"health": 100, "agility": 18, "strength": 12})
        rogue.equip_weapon(Weapon("Steel Dagger", 20, 90))
        rogue.add_skill("Stealth")
        rogue.add_skill("Backstab")
        self.prototypes["rogue"] = rogue

    def create_character(self, character_type, name):
        if character_type.lower() not in self.prototypes:
            raise ValueError(f"Unknown character type: {character_type}")

        # Clone the prototype and customize
        character = self.prototypes[character_type.lower()].clone()
        character.name = name
        return character


# Usage
prototype_manager = CharacterPrototypes()

# Create characters from prototypes
player1 = prototype_manager.create_character("warrior", "Aragorn")
player2 = prototype_manager.create_character("mage", "Gandalf")
player3 = prototype_manager.create_character("warrior", "Boromir")

# Modify characters independently
player1.level_up()
player1.level_up()
player2.add_skill("Lightning Bolt")
player3.equip_weapon(Weapon("Legendary Sword", 50, 200))

print("Player 1:")
print(player1)
print("\nPlayer 2:")
print(player2)
print("\nPlayer 3:")
print(player3)
