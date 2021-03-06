from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
import Char


if __name__=='__main__':

    # ---- Character Tab Creation ---- #
    def add_Char_On_Click(PlayerFrame):
        # ---- Character Tab Creation ---- #
        
        LebelFont = font.Font(family="Times",size=15)
        ButtonFont = font.Font(family="Times",size=7,weight="bold")
        OtherFont = font.Font(family="Times",size=40,weight="bold")

        # ---- Character Frame---- #
        CharFrame = Frame(PlayerFrame, bg=Tab_Color,bd=2)
        CharFrame.pack(side = TOP, pady = 1, anchor=W)


        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        # Creating Top Row Frame
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



        # ---- Main Frame ---- #
        TopFrame = Frame(CharFrame, bg=Tab_Color,bd=0)
        TopFrame.pack(side = TOP, pady = 0, fill=X)

        # Create Character
        Character = Char.Character()


        # ---- Character Name ---- #
        CharName = StringVar()
        Character_Name = Label(TopFrame, textvariable=CharName, bg=Tab_Color, fg=Text_Color, font = LebelFont)
        CharName.set(Character.CharName)
        Character_Name.pack(side = LEFT, padx=5, anchor=W)


        # ---- Character Tab Creation ---- #
        StamFrame = Frame(TopFrame, bg=Tab_Color,bd=2)
        StamFrame.pack(side = LEFT, padx = 5)
        
        # Frame for Minus Buttons
        Subtract_Stam_Frame = Frame(StamFrame, bg=Tab_Color,bd=2)
        Subtract_Stam_Frame.pack(side = LEFT, padx = 5)

        #Stamina Bar
        Stamina_Bar_base = ImageTk.PhotoImage(Image.open(image_stamina_null))
        Stamina_Bar= Label(StamFrame, bg=Tab_Color, image = Stamina_Bar_base)
        Stamina_Bar.pack(side=LEFT)

        #Functions for changing stamina and image
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
        # Stam_Minus_Ten_Var = StringVar()
        # Stam_Minus_Ten_Label = Label(Subtract_Stam_Frame, textvariable=Stam_Minus_Ten_Var, bg=Tab_Color, fg=Text_Color, font = ButtonFont)
        # Stam_Minus_Ten_Var.set("-10")
        # Stam_Minus_Ten_Label.pack(side = TOP, padx=5)
        # Stam_Minus_Ten_Label.bind('<Button-1>', Char_Change_Health_minus_ten)

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
        # Stam_Add_Ten_Var = StringVar()
        # Stam_Add_Ten_Label = Label(Add_Stam_Frame, textvariable=Stam_Add_Ten_Var, bg=Tab_Color, fg=Text_Color, font = ButtonFont)
        # Stam_Add_Ten_Var.set("+10")
        # Stam_Add_Ten_Label.pack(side = TOP, padx=5)
        # Stam_Add_Ten_Label.bind('<Button-1>', Char_Change_Health_plus_ten)


        # ---- Delete Character button ---- #

        # Image load
        
        photo_Delete = ImageTk.PhotoImage(Image.open(image_Delete).resize((20,20), Image.NEAREST))

        #Character Delete Function
        def delete_Char(event = None):
            CharFrame.pack_forget()
            print("Deleated Character: " + Character.PlayerName + " || " + Character.CharName)

        #Character Delete Button and Label
        removePlayerFrame = Frame(TopFrame, bg=Tab_Color)
        removePlayerFrame.pack(side = RIGHT)
        removePlayer_Button= Label(removePlayerFrame,bg=Tab_Color, image = photo_Delete)
        removePlayer_Button.configure(image=photo_Delete)
        removePlayer_Button.image = photo_Delete
        removePlayer_Button.pack(side=RIGHT, pady=0)
        removePlayer_Button.bind('<Button-1>', delete_Char)



        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        # Second Row Frame
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        


        # ---- Second Frame Row ---- #
        SecondFrame = Frame(CharFrame, bg=Tab_Color,bd=0)
        SecondFrame.pack(side = TOP, anchor=W, pady = 0, fill=X)


        # ---- Race Icon ---- #

        # Setting Label for Icon
        Race_Icon_Base = ImageTk.PhotoImage(Image.open(image_stamina_null))
        Race_Icon= Label(SecondFrame, bg=Tab_Color, image = Race_Icon_Base)

        # Function for updating and selcting Icon
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
                # Defult to Dwarf
                icon = image_race_Dwarf
            updated_image = ImageTk.PhotoImage(Image.open(icon).resize((80,80), Image.NEAREST))
            Race_Icon.configure(image=updated_image)
            Race_Icon.image = updated_image
        # Trigger for updating Icon and to change
        def change_race_icon(event = None):
            Character.ChangeRace()
            print(Character.PlayerName + " || " + Character.CharName + " Changed Race to: " + str(Character.race))
            update_Race_Icon()
        Race_Icon.pack(side=LEFT, padx= 24)
        Race_Icon.bind('<Button-1>', change_race_icon)
        update_Race_Icon()


        # ---- Action Buttons ---- #
        
        # Setting Frame
        ActionSFrame = Frame(SecondFrame, bg=Tab_Color,bd=2)
        ActionSFrame.pack(side = LEFT, anchor= CENTER)

        # Actions Images
        photo_null = ImageTk.PhotoImage(Image.open(image_action_null).resize((40,40), Image.NEAREST))
        photo_anytime = ImageTk.PhotoImage(Image.open(image_action_anytime).resize((40,40), Image.NEAREST))
        photo_movement = ImageTk.PhotoImage(Image.open(image_action_movement).resize((40,40), Image.NEAREST))
        photo_attack = ImageTk.PhotoImage(Image.open(image_action_attack).resize((40,40), Image.NEAREST))
        photo_spell = ImageTk.PhotoImage(Image.open(image_action_spell).resize((40,40), Image.NEAREST))
        photo_Arrow = ImageTk.PhotoImage(Image.open(image_Arrow).resize((20,20), Image.NEAREST))
        photo_Minus = ImageTk.PhotoImage(Image.open(image_minus).resize((5,5), Image.NEAREST))
        
        # Function to create new Actions, based on list from Character data
        def Actions(act):
            ActionFrame = Frame(ActionSFrame, bg=Tab_Color,bd=2)
            ActionFrame.pack(side = LEFT, padx = 5)

            # Function to rotate between action types
            def Rotate_Action(a):
                Character.ChangeAction(a)
                update_action(a)

            # Button for rotateing between action types
            ChangeActionIcon = Label(ActionFrame, bg=Tab_Color, image = photo_Arrow)
            ChangeActionIcon.bind('<Button-1>', lambda event, action=act:Rotate_Action(action))
            ChangeActionIcon.configure(image=photo_Arrow)
            ChangeActionIcon.image = photo_Arrow
            ChangeActionIcon.pack(side=TOP)
            
            # Action Icons and Image Selection
            Action_Icon= Label(ActionFrame, bg=Tab_Color, image = photo_null)
            def update_action(acti):
                action = Character.actions[acti]
                aicon = image_action_null
                if action == 1:
                    aicon = photo_anytime
                elif action == 2:
                    aicon = photo_movement
                elif action == 3:
                    aicon = photo_attack
                elif action == 4:
                    aicon = photo_spell
                else:
                    aicon = photo_null
                Action_Icon.configure(image=aicon)
                Action_Icon.image = aicon
            
            # Function to mark actions as active or nonactive
            def trigger_action(a):
                Character.actions[a] = Character.actions[a]*-1
                print(Character.PlayerName + " || " + Character.CharName + " updated action: " + str(a))
                update_action(a)
            # Trigger icon update
            update_action(act)
            Action_Icon.bind('<Button-1>', lambda event, action=act:trigger_action(action))
            Action_Icon.pack(side=TOP)
            def Remove_Action(event = None):
                ActionFrame.pack_forget()
                print(Character.PlayerName + " || " + Character.CharName + " Removed Action")
            
            RemoveAction_Button= Label(ActionFrame,bg=Tab_Color, image = photo_Minus)
            RemoveAction_Button.configure(image=photo_Minus)
            RemoveAction_Button.image = photo_Minus
            RemoveAction_Button.pack(side=BOTTOM)
            RemoveAction_Button.bind('<Button-1>', Remove_Action)
        for a in range(0, len(Character.actions)):
            Actions(a)

        def add_action(event = None):
            lenth = len(Character.actions)
            Character.actions.append(1)
            print(Character.PlayerName + " || " + Character.CharName + " Added Action")

            Actions(lenth)
        AddAction_Var = StringVar()
        AddAction_Button= Label(ActionSFrame, textvariable=AddAction_Var, bg=Tab_Color, fg=Text_Color, font = LebelFont)
        AddAction_Var.set("+")
        AddAction_Button.pack(side=RIGHT)
        AddAction_Button.bind('<Button-1>', add_action)
            

        # ---- Gold ---- #
        photo_Gold = ImageTk.PhotoImage(Image.open(image_Gold).resize((24,24), Image.NEAREST))

        
        GoldFrame = Frame(SecondFrame, bg=Text_Color,bd=1)
        
        def Increase_Gold(event=None):
            Character.gold = Character.gold+5
            Gold_Var.set(str(Character.gold))
            print(Character.PlayerName + " || " + Character.CharName + " Increased Gold: " + str(Character.gold))
        def Decrease_Gold(event=None):
            Character.gold = Character.gold-5
            if Character.gold < 0:
                Character.gold = 0
            Gold_Var.set(str(Character.gold))
            print(Character.PlayerName + " || " + Character.CharName + " Decreassed Gold: " + str(Character.gold))
        
        GoldFrame.bind('<Button-1>', Decrease_Gold)
        GoldFrame.bind('<Button-2>', Increase_Gold)
        GoldFrame.bind('<Button-3>', Increase_Gold)
        
        GoldFrame.pack(side = RIGHT, padx = (64,5), anchor=E)
        GoldIcon = Label(GoldFrame, bg=Tab_Color, image = photo_Gold)
        GoldIcon.configure(image=photo_Gold)
        GoldIcon.image = photo_Gold
        GoldIcon.pack(side = LEFT)
        Gold_Var = StringVar()
        GoldNum = Label(GoldFrame, bg=Tab_Color, textvariable=Gold_Var, font = LebelFont, fg = Text_Color)
        Gold_Var.set(str(Character.gold))
        GoldNum.pack(side = RIGHT)
        
        GoldIcon.bind('<Button-1>', Decrease_Gold)
        GoldIcon.bind('<Button-2>', Increase_Gold)
        GoldIcon.bind('<Button-3>', Increase_Gold)
        GoldNum.bind('<Button-1>', Decrease_Gold)
        GoldNum.bind('<Button-2>', Increase_Gold)
        GoldNum.bind('<Button-3>', Increase_Gold)
        

        

                
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        # Third Row Frame
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        ThirdFrame = Frame(CharFrame, bg=Tab_Color,bd=0)
        ThirdFrame.pack(side = TOP,fill=X, pady = 0)

        # ---- Player Name ---- #
        PlayerName = StringVar()
        Player_Name = Label(ThirdFrame, textvariable=PlayerName, bg=Tab_Color, fg=Text_Color, font = LebelFont)
        PlayerName.set(Character.PlayerName)
        Player_Name.pack(side = LEFT, padx=5, anchor=W)

        print("Created New Character Tab")
        
        # ---- Full Edit Drop Down ---- #
        Advanced_Label_Frame = Frame(ThirdFrame, bg=Text_Color,bd=1)
        Advanced_Label_Frame.pack(side = RIGHT, anchor=E)
        Advanced_Edit_Text = StringVar()
        Advanced_Edit = Label(Advanced_Label_Frame, textvariable=Advanced_Edit_Text, bg=Tab_Color, fg=Text_Color, font = LebelFont)
        Advanced_Edit_Text.set("Advanced")
        Advanced_Edit.pack(side = RIGHT, anchor=E)



        #Advanced Tab Form
        def Advanced_Tab(event=None):

            AdvancedFrame = Frame(CharFrame, bg=Tab_Color,bd=2)
            AdvancedFrame.pack(side = RIGHT, anchor=SW)

            #PlayerName
            Form_PlayerName_Frame = Frame(AdvancedFrame, bg=Tab_Color,bd=2)
            Form_PlayerName_Frame.pack(side = TOP, anchor=W)
            Form_PlayerName = StringVar()
            From_PlayerName_Label = Label(Form_PlayerName_Frame, textvariable=Form_PlayerName, bg=Tab_Color, fg=Text_Color, font = LebelFont)
            Form_PlayerName.set("Player Name: ")
            From_PlayerName_Label.pack(side = LEFT, padx=5)
            Form_Playername_Entry_Var = StringVar()
            Form_PlayerName_Entry = Entry(Form_PlayerName_Frame, textvariable=Form_Playername_Entry_Var, bg=Tab_Color, fg=Text_Color, font = LebelFont, bd=2)
            Form_Playername_Entry_Var.set(Character.PlayerName)
            Form_PlayerName_Entry.pack(side = LEFT, padx = 5)

            #CharName
            Form_CharName_Frame = Frame(AdvancedFrame, bg=Tab_Color,bd=2)
            Form_CharName_Frame.pack(side = TOP, anchor=W)
            Form_CharName = StringVar()
            From_CharName_Label = Label(Form_CharName_Frame, textvariable=Form_CharName, bg=Tab_Color, fg=Text_Color, font = LebelFont)
            Form_CharName.set("Character Name: ")
            From_CharName_Label.pack(side = LEFT, padx=5)
            Form_CharName_Entry_Var = StringVar()
            Form_CharName_Entry = Entry(Form_CharName_Frame, textvariable=Form_CharName_Entry_Var, bg=Tab_Color, fg=Text_Color, font = LebelFont, bd=2)
            Form_CharName_Entry_Var.set(Character.CharName)
            Form_CharName_Entry.pack(side = LEFT, padx = 5)

            #Race
            Form_race_Frame = Frame(AdvancedFrame, bg=Tab_Color,bd=2)
            Form_race_Frame.pack(side = TOP, anchor=W)
            Form_race = StringVar()
            From_race_Label = Label(Form_race_Frame, textvariable=Form_race, bg=Tab_Color, fg=Text_Color, font = LebelFont)
            Form_race.set("Race: ")
            From_race_Label.pack(side = LEFT, padx=5)
            Form_race_menu_Var = StringVar()
            Form_race_menu = OptionMenu(Form_race_Frame, Form_race_menu_Var, *Character.pos_Race)
            Form_race_menu_Var.set(Character.race)
            Form_race_menu.pack(side=LEFT, padx=5)

            #maxhealth
            Form_maxhealth_Frame = Frame(AdvancedFrame, bg=Tab_Color,bd=2)
            Form_maxhealth_Frame.pack(side = TOP, anchor=W)
            Form_maxhealth = StringVar()
            From_maxhealth_Label = Label(Form_maxhealth_Frame, textvariable=Form_maxhealth, bg=Tab_Color, fg=Text_Color, font = LebelFont)
            Form_maxhealth.set("Max Health: ")
            From_maxhealth_Label.pack(side = LEFT, padx=5)
            Form_maxhealth_Entry_Var = StringVar()
            Form_maxhealth_Entry = Entry(Form_maxhealth_Frame, textvariable=Form_maxhealth_Entry_Var, bg=Tab_Color, fg=Text_Color, font = LebelFont, bd=2)
            Form_maxhealth_Entry_Var.set(Character.maxhealth)
            Form_maxhealth_Entry.pack(side = LEFT, padx = 5)

            #health
            Form_health_Frame = Frame(AdvancedFrame, bg=Tab_Color,bd=2)
            Form_health_Frame.pack(side = TOP, anchor=W)
            Form_health = StringVar()
            From_health_Label = Label(Form_health_Frame, textvariable=Form_health, bg=Tab_Color, fg=Text_Color, font = LebelFont)
            Form_health.set("Health: ")
            From_health_Label.pack(side = LEFT, padx=5)
            Form_health_Entry_Var = StringVar()
            Form_health_Entry = Entry(Form_health_Frame, textvariable=Form_health_Entry_Var, bg=Tab_Color, fg=Text_Color, font = LebelFont, bd=2)
            Form_health_Entry_Var.set(Character.health)
            Form_health_Entry.pack(side = LEFT, padx = 5)

            #gold
            Form_gold_Frame = Frame(AdvancedFrame, bg=Tab_Color,bd=2)
            Form_gold_Frame.pack(side = TOP, anchor=W)
            Form_gold = StringVar()
            From_gold_Label = Label(Form_gold_Frame, textvariable=Form_gold, bg=Tab_Color, fg=Text_Color, font = LebelFont)
            Form_gold.set("Gold/Money: ")
            From_gold_Label.pack(side = LEFT, padx=5)
            Form_gold_Entry_Var = StringVar()
            Form_gold_Entry = Entry(Form_gold_Frame, textvariable=Form_gold_Entry_Var, bg=Tab_Color, fg=Text_Color, font = LebelFont, bd=2)
            Form_gold_Entry_Var.set(Character.gold)
            Form_gold_Entry.pack(side = LEFT, padx = 5)

            #SaveButton
            Form_Save_Frame = Frame(AdvancedFrame, bg=Text_Color,bd=2)
            Form_Save_Frame.pack(side = TOP, anchor=E)
            Form_save = StringVar()
            From_save_Label = Label(Form_Save_Frame, textvariable=Form_save, bg=Tab_Color, fg=Text_Color, font = LebelFont)
            Form_save.set("Save & Close")
            From_save_Label.pack(side = LEFT, padx=5)
            def update_Character(event=None):
                Character.PlayerName = Form_PlayerName_Entry.get()
                Character.CharName = Form_CharName_Entry.get()
                Character.race = Form_race_menu_Var.get()
                Character.maxhealth = int(Form_maxhealth_Entry.get())
                Character.health = int(Form_health_Entry.get())
                Character.gold = int(Form_gold_Entry.get())
                
                CharName.set(Character.CharName)
                update_Stam_Bar()
                update_Race_Icon()
                Increase_Gold()
                Decrease_Gold()
                PlayerName.set(Character.PlayerName)
                print(Character.PlayerName + " || " + Character.CharName + " Updated Info")
                AdvancedFrame.forget()
            Form_Save_Frame.bind('<Button-1>', update_Character)
            From_save_Label.bind('<Button-1>', update_Character)
        Advanced_Edit.bind('<Button-1>', Advanced_Tab)
    
        Advanced_Label_Frame = Frame(ThirdFrame, bg=Text_Color,bd=1)
        Advanced_Label_Frame.pack(side = RIGHT, anchor=E)




            



        


    # ---- Asset Loading ----#
    Window_Color = "#3d3731"
    Text_Color = "#c9981c"
    Tab_Color = "#2e241b"

    image_plus = "./libs/assets/img/+.png"
    image_Delete = "./libs/assets/img/Delete.png"
    image_minus = "./libs/assets/img/-.png"
    image_Arrow = "./libs/assets/img/Arrow.png"
    image_Gold = "./libs/assets/img/Gold.png"


    image_action_null = "./libs/assets/img/Null.png"
    image_action_anytime = "./libs/assets/img/Anytime.png"
    image_action_attack = "./libs/assets/img/Attack.png"
    image_action_movement = "./libs/assets/img/movement.png"    
    image_action_spell = "./libs/assets/img/spell.png"

    image_stamina_null = "./libs/assets/img/stamina_0.png"  
    image_stamina_10 = "./libs/assets/img/stamina_10.png" 
    image_stamina_20 = "./libs/assets/img/stamina_20.png" 
    image_stamina_30 = "./libs/assets/img/stamina_30.png" 
    image_stamina_40 = "./libs/assets/img/stamina_40.png" 
    image_stamina_50 = "./libs/assets/img/stamina_50.png" 
    image_stamina_60 = "./libs/assets/img/stamina_60.png" 
    image_stamina_70 = "./libs/assets/img/stamina_70.png" 
    image_stamina_80 = "./libs/assets/img/stamina_80.png" 
    image_stamina_90 = "./libs/assets/img/stamina_90.png"  
    image_stamina_100 = "./libs/assets/img/stamina_100.png"

    image_race_Dwarf = "./libs/assets/img/Dwarf.png"
    image_race_Elf = "./libs/assets/img/Elf.png"
    image_race_Gnome = "./libs/assets/img/Gnome.png"
    image_race_Crown = "./libs/assets/img/Crown.png"
    image_race_Fang = "./libs/assets/img/Fang.png"
    image_race_Human = "./libs/assets/img/Human.png"
    image_race_Lizard = "./libs/assets/img/Lizard.png"
    image_race_Locus = "./libs/assets/img/Locus.png"
    image_race_Octopus = "./libs/assets/img/Octopus.png"
    image_race_Robot = "./libs/assets/img/Robot.png"
    image_race_Sward = "./libs/assets/img/Sword.png"
    image_race_Turtle = "./libs/assets/img/Tutle.png"
    
    
    # ---- Window Build ---- #

    master=Tk()
    master.configure(bg=Window_Color)
    master.title("Charcter Tracker")
    master.iconbitmap("./libs/favicon.ico")



    
    def create_class(event=None):
        PlayerFrame = Frame(master, bg=Window_Color)
        PlayerFrame.pack(side = LEFT, anchor=N, padx=(0,5))
        #Add Player Button Creation
        AddPlayerFrame = Frame(PlayerFrame, bg=Window_Color)
        AddPlayerFrame.pack(side = BOTTOM, anchor=SE)
        AddPlayer_Button= Label(AddPlayerFrame, bg=Window_Color, image = AddClass_Symbole)
        AddPlayer_Button.pack(side=BOTTOM)
        print("Created New Character Class")
        def add_char_trigger_pass(event=None):
            add_Char_On_Click(PlayerFrame)
        AddPlayer_Button.bind('<Button-1>', add_char_trigger_pass)
    
    AddClassFrame = Frame(master, bg=Window_Color)
    AddClassFrame.pack(side = BOTTOM, anchor=SW)
    AddClass_Symbole = ImageTk.PhotoImage(Image.open(image_plus).resize((32,32), Image.NEAREST))
    AddClass_Button= Label(AddClassFrame, bg=Window_Color, image = AddClass_Symbole)
    AddClass_Button.pack(side=BOTTOM)
    AddClass_Button.bind('<Button-1>', create_class)
    
    # ---- Start Window ---- #
    master.mainloop()





    


