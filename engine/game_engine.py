from auto_battle.models.character import Character
from random import randint
from auto_battle.services.battle_service import BattleService
from auto_battle.services.damage_calculator import DamageCalculator
from auto_battle.factory.character_factory import CharacterFactory
import time

class GameEngine:
    def __init__(self, characters: list[Character], service: BattleService):
        self.characters = characters
        self.service = service

    def run(self):
        while len(self._alive_characters()) > 1:
            attacker, defender = self._choose_pair()
            self._fight(attacker, defender)

        winner = self._alive_characters()[0]
        print(f"\n🏆 Игра окончена! Победитель: {winner.name}")

    def _fight(self, attacker: Character, defender: Character):
        print("\n⚔️ Бой начинается!")
        print(f"{attacker.class_name}---{attacker.name} VS {defender.class_name}---{defender.name}")
        time.sleep(1)

        turn = 1
        while attacker.is_alive() and defender.is_alive():
            print(f"Ход {turn}:")
            self.service.attack(attacker, defender)
            time.sleep(1)
            if not defender.is_alive():
                print(f"Победитель раунда {attacker.name}, и у него осталось {round(attacker.health, 2)}HP, a {defender.name} пал в бою!")
                break
            attacker, defender = defender, attacker
            turn += 1
        print("⚔️ Бой завершён\n")
        time.sleep(2)

    def _alive_characters(self) -> list[Character]:
        return [character for character in self.characters if character.is_alive()]
    def _choose_pair(self) -> tuple[Character, Character]:
        characters = self._alive_characters()
        if len(characters) >= 2:
            attacker = characters[randint(0, len(characters) - 1)]
            defender = characters[randint(0, len(characters) - 1)]
            while True:
                if defender != attacker: break
                defender = characters[randint(0, len(characters) - 1)]
            return attacker, defender
    @classmethod
    def create_default_game(cls):
        print("Вас приветствует игра БОИ")
        count = int(input("Введите количество персонажей: "))
        factory = CharacterFactory()
        characters = factory.create_many(count)
        print('_'*40)
        print("Наши сегодняшние бойцы:")
        for character in characters:
            print(f"{character.class_name} {character.name} с оружием {character.weapon.name!r}")
        print('_' * 40)
        time.sleep(2)
        calculator = DamageCalculator()
        service = BattleService(calculator)
        return cls(characters, service)
