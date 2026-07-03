class Character:
    def __init__(self, hp, name):
        self.name = name
        self.hp = hp

    def displayInfo(self):
        print(f"HP: {self.hp, self.name}")


class player(Character):
    def __init__(self, hp, name):
        Character.__init__(self, hp, name)
    
class enemy(Character):
    def __init__(self, hp, name):
        Character.__init__(self, hp, name)
    
    def damaged(self, damage):
        print(f"[self.name] lost [damage] HP")
        self.hp -= damage

