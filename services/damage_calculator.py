from auto_battle.models.character import Character
from random import uniform

class DamageCalculator:
    def calculate(self, attacker: Character, defender: Character) -> int|float:
        return max(attacker.base_damage()*self.random_modifier() - defender.defence_modifier(), 0)
    @staticmethod
    def random_modifier() -> int|float:
        return uniform(0.8, 1.2)

