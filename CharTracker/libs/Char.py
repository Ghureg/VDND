import SpellShop
class Character():
    def __init__(self):
        self.PlayerName = "Player Name"
        self.CharName = "Character Name"
        self.race = "DWARF"
        self.maxhealth = 20
        self.health = 20
        self.gold = 100
        # 1 = Anytime
        # 2 = Movement
        # 3 = Basic Attack
        # 4 = Spell
        self.actions = [3,4,2,1,1]
        self.spells = []
    def ChangePlayerName(self, NewName):
        self.PlayerName = NewName
    def ChangeCharacterName(self, NewName):
        self.CharacterName = NewName
    def ChangeHealth(self, amount):
        self.health = self.health + amount
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        if self.health <= 0:
            self.health = 0
    def ChangeAction(self, space, newvalue):
        self.action[space] = newvalue
    def ChangeGold(self, amount):
        self.gold = self.gold + amount
    def AddSpell(self, SpellName):
        Spells = SpellShop.Shop()
        for i in range(0,len(Spells.SpellList)):
            if Spells.SpellList[i][0] == SpellName:
                self.spells.append(Spells.SpellList[i])
                return None
    def RemoveSpell(self, SpellName):
        for i in range(0,len(self.spells)):
            if self.spells[i][0] == SpellName:
                del self.spells[i]
                return None
    
