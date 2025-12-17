from dataclasses import dataclass
@dataclass
class Weapon:
    name: str
    damage: int
    durability: int
    def use(self) -> int:
        if self.is_broken(): return 0
        self.durability -= 1
        return self.damage
    def is_broken(self) -> bool:
        return self.durability <= 0
    @property
    def is_usable(self) -> bool:
        return self.durability > 0
