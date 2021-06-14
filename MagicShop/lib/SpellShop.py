import csv
import numpy as np
class Shop():
    def __init__(self):
        self.NAME = 0
        self.TYPE = 1
        self.LEVEL = 2
        self.COST = 3
        self.CONCOST = 4
        self.RANGE = 5
        self.DISCRIPTION = 6
        self.SpellList = []
        with open("./lib/assets/MasterMagicList.tsv",encoding="utf8") as Unfiltered:
            Source = csv.reader(Unfiltered, delimiter="\t", quotechar='"')
            for spell in Source:
                self.SpellList.append(spell)
        self.LightSpells = self.GetSpells(self.SpellList,"light")
        self.EarthSpells = self.GetSpells(self.SpellList,"earth")
        self.IceSpells = self.GetSpells(self.SpellList,"ice")
        self.DarkSpells = self.GetSpells(self.SpellList,"dark")
        self.ArcaneSpells = self.GetSpells(self.SpellList,"arcane")
        self.FireSpells = self.GetSpells(self.SpellList,"fire")
        self.BasicAbilitySpells = self.GetSpells(self.SpellList,"basicability")

    def GetSpells(self,SpellList,t):
        if t == "light": ty = 'L'
        if t == "earth": ty = 'E'
        if t == "ice": ty = 'I'
        if t == "dark": ty = 'D'
        if t == "fire": ty = 'F'
        if t == "arcane": ty = 'A'
        if t == "basicability": ty = 'BA'
        ListofClassSpells = []
        for spell in self.SpellList:
            if spell[self.TYPE] == ty:
                ListofClassSpells.append(spell)
        return ListofClassSpells

    def GetRandomSpell(self,ListofSpells,number):
        indexes = (np.random.choice(range(0,len(ListofSpells)), number, False))
        returnedSpells = []
        for i in indexes:
            returnedSpells.append(ListofSpells[i])
        return returnedSpells
    def CreateStore(self,ListofSpells):
        NumberofOther = 5
        NumberofBasic = 6
        NumberofAdanced = 2
        NumberofLegendary = 0
        OtherSpells = []
        BasicSpells = []
        AdvancedSpells = []
        LegendarySpells = []
        for spell in ListofSpells:
            if int(spell[self.LEVEL]) == 1:
                BasicSpells.append(spell)
            elif int(spell[self.LEVEL]) == 2:
                AdvancedSpells.append(spell)
            elif int(spell[self.LEVEL]) == 3:
                LegendarySpells.append(spell)
            else:
                OtherSpells.append(spell)
        SpellShop = []
        if NumberofBasic != 0 and len(BasicSpells) != 0:
            BasicSpellShopIndexes = np.random.choice(range(0,len(BasicSpells)), NumberofBasic)
            for s in BasicSpellShopIndexes:
                SpellShop.append(BasicSpells[s])
        if NumberofBasic != 0 and len(AdvancedSpells) != 0:
            AdvancedSpellShopIndexes = np.random.choice(range(0,len(AdvancedSpells)), NumberofAdanced)
            for s in AdvancedSpellShopIndexes:
                SpellShop.append(AdvancedSpells[s])
        if NumberofBasic != 0 and len(LegendarySpells) != 0:
            LegendarySpellShopIndexes = np.random.choice(range(0,len(LegendarySpells)), NumberofLegendary)
            for s in LegendarySpellShopIndexes:
                SpellShop.append(LegendarySpells[s])
        if NumberofOther != 0 and len(OtherSpells) !=0:
            OtherSpellsShopIndexes = np.random.choice(range(0,len(OtherSpells)), NumberofOther)
            for s in OtherSpellsShopIndexes:
                SpellShop.append(OtherSpells[s])

        return SpellShop

    def output(self, Spells):
        outputfile = open("./lib/Spells.txt", "w")
        for s in Spells:
            outputfile.write("""{}\nCost: {}\nContinued Cost: {}\nCast Time: {}\nRange: {}\nDiscription: \n{}\n\n\n""".format(s[self.NAME], s[self.COST], s[self.CONCOST],s[5],s[6],s[7]))
        outputfile.close()

