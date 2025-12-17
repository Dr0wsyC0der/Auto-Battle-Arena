from abc import ABC, abstractmethod
from auto_battle.models.weapon import Weapon


class Character(ABC):
    def __init__(self, name, health, weapon: Weapon):
        self._name = name
        self._health = health
        self._weapon = weapon
    @abstractmethod
    def base_damage(self):
        pass
    @abstractmethod
    def defence_modifier(self):
        pass
    def is_alive(self):
        return self._health > 0
    def take_damage(self, amount):
        self._health -= amount
    @property
    def name(self):
        return self._name
    @property
    def health(self):
        return self._health
    @property
    def weapon(self):
        return self._weapon

class Magician(Character):
    def __init__(self, name, health, weapon: Weapon):
        super().__init__(name, health, weapon)
        self.class_name = 'Magician'
    def base_damage(self) -> int:
        return 55
    def defence_modifier(self) -> int:
        return 20
class Knight(Character):
    def __init__(self, name, health, weapon: Weapon):
        super().__init__(name, health, weapon)
        self.class_name = 'Knight'
    def base_damage(self)-> int:
        return 35
    def defence_modifier(self)-> int:
        return 15
class Hunter(Character):
    def __init__(self, name, health, weapon: Weapon):
        super().__init__(name, health, weapon)
        self.class_name = 'Hunter'
    def base_damage(self) -> int:
        return 25
    def defence_modifier(self) -> int:
        return 10
class Monster(Character):
    def __init__(self, name, health, weapon: Weapon):
        super().__init__(name, health, weapon)
        self.class_name = 'Monster'
    def base_damage(self) -> int:
        return 50
    def defence_modifier(self) -> int:
        return 0