from typing import List
from auto_battle.models.weapon import Weapon
from auto_battle.models.character import Character
from random import randint

class CharacterFactory:
    characters_name = []
    def create_random(self) -> Character:
        character_var = [cls for cls in Character.__subclasses__()]
        who_is = character_var[randint(0, len(character_var) - 1)]
        health = randint(150, 200)
        name = self.create_name()
        weapons_names = [
            "Ржавый меч",
            "Топор дровосека",
            "Лук с тугими тетивами",
            "Магический посох",
            "Кинжал вора",
            "Дубина с гвоздями"
        ]
        weapon_damage = randint(5, 10)
        weapon_durability = randint(5, 10)
        weapon = Weapon(weapons_names[randint(0, len(weapons_names) - 1)], weapon_damage, weapon_durability)
        return who_is(name, health, weapon)

    def create_many(self, count: int) -> List[Character]:
        return [self.create_random() for _ in range(count)]

    @staticmethod
    def create_name() -> str:
        name = ['Torric','Galran','Keldor','Zorian','Baltazar','Dreven','Finnegan','Xylon','Thundermaker','Ignis']
        f_name = ['Silverwood','Ironfist','Stormborn','Sunsheld','Rockguard','Firemane','Moonblade','Starwalker','Wanderer','Ashstrider']
        full_name = name[randint(0, 9)] + " " +  f_name[randint(0, 9)]
        if full_name in CharacterFactory.characters_name:
            while True:
                full_name = name[randint(0, 9)] + f_name[randint(0, 9)]
                if full_name not in CharacterFactory.characters_name: break
        CharacterFactory.characters_name.append(full_name)
        return full_name
