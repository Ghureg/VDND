import csv
import numpy as np
import tkinter as tk
import SpellShop

NAME = 0
TYPE = 1
LEVEL = 2
COST = 3
CONCOST = 4
RANGE = 5
DISCRIPTION = 6



def main():
    SpellsEnv = SpellShop.Shop()
    
    def GetStore():
        NewStoreInput = []
        if lightstore.get() == 1:
            NewStoreInput.extend(SpellsEnv.LightSpells)
        if earthstore.get() == 1:
            NewStoreInput.extend(SpellsEnv.EarthSpells)
        if icestore.get() == 1:
            NewStoreInput.extend(SpellsEnv.IceSpells)
        if darkstore.get() == 1:
            NewStoreInput.extend(SpellsEnv.DarkSpells)
        if arcanestore.get() == 1:
            NewStoreInput.extend(SpellsEnv.ArcaneSpells)
        if firestore.get() == 1:
            NewStoreInput.extend(SpellsEnv.FireSpells)
        if basicabilitystore.get() == 1:
            NewStoreInput.extend(SpellsEnv.BasicAbilitySpells)
        NewStore = SpellsEnv.CreateStore(NewStoreInput)
        SpellsEnv.output(NewStore)
        master.destroy()

    def GetRandom():
        NewStoreInput = []
        if lightstore.get() == 1:
            NewStoreInput.extend(SpellsEnv.LightSpells)
        if earthstore.get() == 1:
            NewStoreInput.extend(SpellsEnv.EarthSpells)
        if icestore.get() == 1:
            NewStoreInput.extend(SpellsEnv.IceSpells)
        if darkstore.get() == 1:
            NewStoreInput.extend(SpellsEnv.DarkSpells)
        if arcanestore.get() == 1:
            NewStoreInput.extend(SpellsEnv.ArcaneSpells)
        if firestore.get() == 1:
            NewStoreInput.extend(SpellsEnv.FireSpells)
        if basicabilitystore.get() == 1:
            NewStoreInput.extend(SpellsEnv.BasicAbilitySpells)
        NewSpell = SpellsEnv.GetRandomSpell(NewStoreInput, 1)
        SpellsEnv.output(NewSpell)
        master.destroy()

    master = tk.Tk()
    master.rowconfigure([0,1,2,3,4,5], weight=1)
    master.columnconfigure([0, 1, 2, 3], weight=1)
    master.configure(bg='#1a041c')
    master.title("Magic Shop")

    la = tk.Label(master, text="Magic Store",bg='#1a041c', fg='#ebe6ed').grid(row=0,column=2)
    lightstore = tk.IntVar()
    earthstore = tk.IntVar()
    icestore = tk.IntVar()
    darkstore = tk.IntVar()
    arcanestore = tk.IntVar()
    firestore = tk.IntVar()
    basicabilitystore = tk.IntVar()

    lightcheck = tk.Checkbutton(master, text="Light", variable=lightstore, onvalue=1, offvalue=0,bg='#1a041c', fg='#ebe6ed',selectcolor='#1a041c').grid(row=2,column=0)
    earthcheck = tk.Checkbutton(master, text="Earth", variable=earthstore, onvalue=1, offvalue=0,bg='#1a041c', fg='#ebe6ed',selectcolor='#1a041c').grid(row=3,column=0)
    icecheck = tk.Checkbutton(master, text="Ice", variable=icestore, onvalue=1, offvalue=0,bg='#1a041c', fg='#ebe6ed',selectcolor='#1a041c').grid(row=4,column=0)
    darkcheck = tk.Checkbutton(master, text="Dark", variable=darkstore, onvalue=1, offvalue=0,bg='#1a041c', fg='#ebe6ed',selectcolor='#1a041c').grid(row=2,column=3)
    arcanecheck = tk.Checkbutton(master, text="Arcane", variable=arcanestore, onvalue=1, offvalue=0,bg='#1a041c', fg='#ebe6ed',selectcolor='#1a041c').grid(row=3,column=3)
    firecheck = tk.Checkbutton(master, text="Fire", variable=firestore, onvalue=1, offvalue=0,bg='#1a041c', fg='#ebe6ed',selectcolor='#1a041c').grid(row=4,column=3)
    
    basicability = tk.Checkbutton(master, text="Basic Ability", variable=basicabilitystore, onvalue=1, offvalue=0,bg='#1a041c', fg='#ebe6ed',selectcolor='#1a041c').grid(row=1,column=2)
    
    
    
    SubmitButtonStore = tk.Button(master, text='Create Store', command=GetStore,bg='#1a041c', fg='#ebe6ed').grid(row=5,column=1, pady=4)
    SubmitButtonSpell = tk.Button(master, text='Get Random', command=GetRandom,bg='#1a041c', fg='#ebe6ed').grid(row=5,column=2, pady=4)
    master.mainloop()

    

if __name__=='__main__':
    main()