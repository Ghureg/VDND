from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
import Char


if __name__=='__main__':
    # ---- On_Click Functions ---- #


    # ---- Character Tab Creation ---- #
    def add_Char_On_Click(event = None):
        #More asset loading
        
        LebelFont = font.Font(family="Times",size=15)
        ButtonFont = font.Font(family="Times",size=7,weight="bold")
        OtherFont = font.Font(family="Times",size=40,weight="bold")

        #Create Character Frame
        CharFrame = Frame(PlayerFrame, bg=Tab_Color,bd=2)
        CharFrame.pack(side = TOP, pady = 10)


        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        # Creating Top Row Frame
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#




        TopFrame = Frame(CharFrame, bg=Tab_Color,bd=2)
        TopFrame.pack(side = TOP)

        # Create Character
        Character = Char.Character()
        # Character Name
        CharName = StringVar()
        Character_Name = Label(TopFrame, textvariable=CharName, bg=Tab_Color, fg=Text_Color, font = LebelFont)
        CharName.set(Character.CharName)
        Character_Name.pack(side = LEFT, padx=5)
        #Character  Stamina
        StamFrame = Frame(TopFrame, bg=Tab_Color,bd=2)
        StamFrame.pack(side = LEFT, padx = 5)
        
        # Frame for Minus Buttons
        Subtract_Stam_Frame = Frame(StamFrame, bg=Tab_Color,bd=2)
        Subtract_Stam_Frame.pack(side = LEFT, padx = 5)

        #Stamina Bar
        Stamina_Bar_base = ImageTk.PhotoImage(Image.open(image_stamina_null))
        Stamina_Bar= Label(StamFrame, bg=Tab_Color, image = Stamina_Bar_base)
        Stamina_Bar.pack(side=LEFT)

        def Char_Change_Health_minus_one(event = None, amount = -1):
            Character.ChangeHealth(amount)
            print(Character.PlayerName + " || " + Character.CharName + " Stamina:" + str(Character.health))
            update_Stam_Bar()
        def Char_Change_Health_minus_five(event = None, amount = -5):
            Character.ChangeHealth(amount)
            print(Character.PlayerName + " || " + Character.CharName + " Stamina:" + str(Character.health))
            update_Stam_Bar()
        def Char_Change_Health_minus_ten(event = None, amount = -10):
            Character.ChangeHealth(amount)
            print(Character.PlayerName + " || " + Character.CharName + " Stamina:" + str(Character.health))
            update_Stam_Bar()

        def Char_Change_Health_plus_one(event = None, amount = 1):
            Character.ChangeHealth(amount)
            print(Character.PlayerName + " || " + Character.CharName + " Stamina:" + str(Character.health))
            update_Stam_Bar()
        def Char_Change_Health_plus_five(event = None, amount = 5):
            Character.ChangeHealth(amount)
            print(Character.PlayerName + " || " + Character.CharName + " Stamina:" + str(Character.health))
            update_Stam_Bar()
        def Char_Change_Health_plus_ten(event = None, amount = 10):
            Character.ChangeHealth(amount)
            print(Character.PlayerName + " || " + Character.CharName + " Stamina:" + str(Character.health))
            update_Stam_Bar()

        def update_Stam_Bar():
            bar = image_stamina_null
            percent = Character.health/Character.maxhealth
            if percent == 0:
                bar = image_stamina_null
            elif 0 < percent <= 0.1:
                bar = image_stamina_10
            elif 0.1 < percent <= 0.2:
                bar = image_stamina_20
            elif 0.2 < percent <= 0.3:
                bar = image_stamina_30
            elif 0.3 < percent <= 0.4:
                bar = image_stamina_40
            elif 0.4 < percent <= 0.5:
                bar = image_stamina_50
            elif 0.5 < percent <= 0.6:
                bar = image_stamina_60
            elif 0.6 < percent <= 0.7:
                bar = image_stamina_70
            elif 0.7 < percent <= 0.8:
                bar = image_stamina_80
            elif 0.8 < percent <= 0.9:
                bar = image_stamina_90
            else: 
                bar = image_stamina_100
            updated_image = ImageTk.PhotoImage(Image.open(bar).resize((300,30), Image.NEAREST))
            Stamina_Bar.configure(image=updated_image)
            Stamina_Bar.image = updated_image
        update_Stam_Bar()
        

        #Stamina Minus Buttons
        Stam_Minus_One_Var = StringVar()
        Stam_Minus_One_Label = Label(Subtract_Stam_Frame, textvariable=Stam_Minus_One_Var, bg=Tab_Color, fg=Text_Color, font = ButtonFont)
        Stam_Minus_One_Var.set("- 1")
        Stam_Minus_One_Label.pack(side = TOP, padx=5)
        Stam_Minus_One_Label.bind('<Button-1>', Char_Change_Health_minus_one)

        Stam_Minus_Five_Var = StringVar()
        Stam_Minus_Five_Label = Label(Subtract_Stam_Frame, textvariable=Stam_Minus_Five_Var, bg=Tab_Color, fg=Text_Color, font = ButtonFont)
        Stam_Minus_Five_Var.set("- 5")
        Stam_Minus_Five_Label.pack(side = TOP, padx=5)
        Stam_Minus_Five_Label.bind('<Button-1>', Char_Change_Health_minus_five)

        Stam_Minus_Ten_Var = StringVar()
        Stam_Minus_Ten_Label = Label(Subtract_Stam_Frame, textvariable=Stam_Minus_Ten_Var, bg=Tab_Color, fg=Text_Color, font = ButtonFont)
        Stam_Minus_Ten_Var.set("-10")
        Stam_Minus_Ten_Label.pack(side = TOP, padx=5)
        Stam_Minus_Ten_Label.bind('<Button-1>', Char_Change_Health_minus_ten)


        #Stamina Add Buttons
        Add_Stam_Frame = Frame(StamFrame, bg=Tab_Color,bd=2)
        Add_Stam_Frame.pack(side = LEFT, padx = 5)

        Stam_Add_One_Var = StringVar()
        Stam_Add_One_Label = Label(Add_Stam_Frame, textvariable=Stam_Add_One_Var, bg=Tab_Color, fg=Text_Color, font = ButtonFont)
        Stam_Add_One_Var.set("+ 1")
        Stam_Add_One_Label.pack(side = TOP, padx=5)
        Stam_Add_One_Label.bind('<Button-1>', Char_Change_Health_plus_one)

        Stam_Add_Five_Var = StringVar()
        Stam_Add_Five_Label = Label(Add_Stam_Frame, textvariable=Stam_Add_Five_Var, bg=Tab_Color, fg=Text_Color, font = ButtonFont)
        Stam_Add_Five_Var.set("+ 5")
        Stam_Add_Five_Label.pack(side = TOP, padx=5)
        Stam_Add_Five_Label.bind('<Button-1>', Char_Change_Health_plus_five)

        Stam_Add_Ten_Var = StringVar()
        Stam_Add_Ten_Label = Label(Add_Stam_Frame, textvariable=Stam_Add_Ten_Var, bg=Tab_Color, fg=Text_Color, font = ButtonFont)
        Stam_Add_Ten_Var.set("+10")
        Stam_Add_Ten_Label.pack(side = TOP, padx=5)
        Stam_Add_Ten_Label.bind('<Button-1>', Char_Change_Health_plus_ten)


        # Delete Character
        def delete_Char(event = None):
            CharFrame.pack_forget()
            print("Deleated Character: " + Character.PlayerName + " || " + Character.CharName)
        removePlayerFrame = Frame(TopFrame, bg=Tab_Color)
        removePlayerFrame.pack(side = RIGHT)
        removePlayer_Symbole = StringVar()
        removePlayer_Button= Label(removePlayerFrame, textvariable=removePlayer_Symbole, bg=Tab_Color, fg=Text_Color, font = OtherFont)
        removePlayer_Symbole.set("-")
        removePlayer_Button.pack(side=RIGHT)
        removePlayer_Button.bind('<Button-1>', delete_Char)


        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        # Second Row Frame
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        SecondFrame = Frame(CharFrame, bg=Tab_Color,bd=2)
        SecondFrame.pack(side = TOP)



        #Race Icon
        
        Race_Icon_Base = ImageTk.PhotoImage(Image.open(image_stamina_null))
        Race_Icon= Label(SecondFrame, bg=Tab_Color, image = Race_Icon_Base)

        def update_Race_Icon():
            icon = image_race_Dwarf
            value = Character.race
            if value == "ELF":
                icon = image_race_Elf
            elif value == "GNOME":
                icon = image_race_Gnome
            elif value == "CROWN":
                icon = image_race_Crown
            elif value == "BEAST":
                icon = image_race_Fang
            elif value == "MANDOZIAN":
                icon = image_race_Human
            elif value == "CATHARINES":
                icon = image_race_Lizard
            elif value == "ENORKANS":
                icon = image_race_Locus
            elif value == "XENOKIAN":
                icon = image_race_Octopus
            elif value == "VESTIAN":
                icon = image_race_Robot
            elif value == "SWORD":
                icon = image_race_Sward
            elif value == "HERGSOIGISE":
                icon = image_race_Turtle
            

            else:
                icon = image_race_Dwarf
            updated_image = ImageTk.PhotoImage(Image.open(icon).resize((80,80), Image.NEAREST))
            Race_Icon.configure(image=updated_image)
            Race_Icon.image = updated_image
        def change_race_icon(event = None):
            Character.ChangeRace()
            print(Character.PlayerName + " || " + Character.CharName + " Changed Race to: " + str(Character.race))
            update_Race_Icon()

        
        Race_Icon.pack(side=LEFT)
        Race_Icon.bind('<Button-1>', change_race_icon)
        
        update_Race_Icon()


        #Actions

        def Actions(action = 0):
            ActionFrame = Frame(SecondFrame, bg=Tab_Color,bd=2)
            ActionFrame.pack(side = LEFT, padx = 5)
            
            Action_Icon_Base = ImageTk.PhotoImage(Image.open(image_action_null))
            Action_Icon= Label(ActionFrame, bg=Tab_Color, image = Action_Icon_Base)
            def update_action():
                icon = image_action_null
                if action == 1:
                    icon = image_action_anytime
                elif action == 2:
                    icon = image_action_movement
                elif action == 3:
                    icon = image_action_attack
                elif action == 4:
                    icon = image_action_spell
                else:
                    icon = image_action_null
                updated_image = ImageTk.PhotoImage(Image.open(icon).resize((20,20), Image.NEAREST))
                Race_Icon.configure(image=updated_image)
                Race_Icon.image = updated_image
            # def trigger_action(event = None):
            #     action = action *-1
            #     update_action()
            Action_Icon.pack(side=LEFT)
            # Action_Icon.bind('<Button-1>', trigger_action)
        for i in Character.actions:
            Actions(action = i)
            


                

        print("Created New Character Tab")

        


    # ---- Asset Loading ----#
    Window_Color = "#3d3731"
    Text_Color = "#c9981c"
    Tab_Color = "#2e241b"

    image_plus = "./assets/img/+.png"
    image_minus = "./assets/img/-.png"

    image_action_null = "./assets/img/Null.png"
    image_action_anytime = "./assets/img/Anytime.png"
    image_action_attack = "./assets/img/Attack.png"
    image_action_movement = "./assets/img/movement.png"    
    image_action_spell = "./assets/img/spell.png"

    image_stamina_null = "./assets/img/stamina_0.png"  
    image_stamina_10 = "./assets/img/stamina_10.png" 
    image_stamina_20 = "./assets/img/stamina_20.png" 
    image_stamina_30 = "./assets/img/stamina_30.png" 
    image_stamina_40 = "./assets/img/stamina_40.png" 
    image_stamina_50 = "./assets/img/stamina_50.png" 
    image_stamina_60 = "./assets/img/stamina_60.png" 
    image_stamina_70 = "./assets/img/stamina_70.png" 
    image_stamina_80 = "./assets/img/stamina_80.png" 
    image_stamina_90 = "./assets/img/stamina_90.png"  
    image_stamina_100 = "./assets/img/stamina_100.png"

    image_race_Dwarf = "./assets/img/Dwarf.png"
    image_race_Elf = "./assets/img/Elf.png"
    image_race_Gnome = "./assets/img/Gnome.png"
    image_race_Crown = "./assets/img/Crown.png"
    image_race_Fang = "./assets/img/Fang.png"
    image_race_Human = "./assets/img/Human.png"
    image_race_Lizard = "./assets/img/Lizard.png"
    image_race_Locus = "./assets/img/Locus.png"
    image_race_Octopus = "./assets/img/Octopus.png"
    image_race_Robot = "./assets/img/Robot.png"
    image_race_Sward = "./assets/img/Sword.png"
    image_race_Turtle = "./assets/img/Tutle.png"
    
    
    # ---- Window Build ---- #

    master=Tk()
    master.configure(bg=Window_Color)
    master.title("Charcter Tracker")

    #Create main Frames
    PlayerFrame = Frame(master, bg=Window_Color)
    PlayerFrame.pack(side = TOP)
    NPCFrame = Frame(master)
    NPCFrame.pack(side = LEFT)

    #Add Player Button Creation
    AddPlayerFrame = Frame(master, bg=Window_Color)
    AddPlayerFrame.pack(side = LEFT)
    AddPlayer_Symbole = ImageTk.PhotoImage(Image.open(image_plus).resize((32,32), Image.NEAREST))
    AddPlayer_Button= Label(AddPlayerFrame, bg=Window_Color, image = AddPlayer_Symbole)
    AddPlayer_Button.pack(side=BOTTOM)
    AddPlayer_Button.bind('<Button-1>', add_Char_On_Click)
    
    # ---- Start Window ---- #
    master.mainloop()





    


