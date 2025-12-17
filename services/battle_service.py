from auto_battle.models.character import Character
from auto_battle.services.damage_calculator import DamageCalculator


class BattleService:
    def __init__(self, calculator: DamageCalculator):
        self.calculator = calculator
    def attack(self, attacker: Character, defender: Character):
        if not attacker.is_alive():return
        if not defender.is_alive():return
        if not attacker.weapon.is_usable: return
        damage = self.calculator.calculate(attacker, defender)
        defender.take_damage(damage)
        print(f'{attacker.name} нанес урон в {round(damage, 2)} HP {defender.name}, с помощью {attacker.weapon.name!r}')
        print(f"У {attacker.name}-->{round(attacker.health, 2)}HP, а у {defender.name}-->{round(defender.health, 2)}")


