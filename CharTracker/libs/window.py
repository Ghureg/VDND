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

        #Create Character Frame
        CharFrame = Frame(PlayerFrame, bg=Tab_Color,bd=2)
        CharFrame.pack(side = TOP, pady = 10)

        # Create Character
        Character = Char.Character()
        # Character Name
        CharName = StringVar()
        Character_Name = Label(CharFrame, textvariable=CharName, bg=Tab_Color, fg=Text_Color, font = LebelFont)
        CharName.set(Character.CharName)
        Character_Name.pack(side = LEFT, padx=5)
        #Character  Stamina
        StamFrame = Frame(CharFrame, bg=Tab_Color,bd=2)
        StamFrame.pack(side = LEFT, padx = 5)


        #Stamina Minus Buttons
        Subtract_Stam_Frame = Frame(StamFrame, bg=Tab_Color,bd=2)
        Subtract_Stam_Frame.pack(side = LEFT, padx = 5)

        #Stamina Bar
        Stamina_Bar_base = ImageTk.PhotoImage(Image.open(image_stamina_null))
        Stamina_Bar= Label(StamFrame, bg=Tab_Color, image = Stamina_Bar_base)
        Stamina_Bar.pack(side=LEFT)

        def Char_Change_Health_minus_one(event = None, amount = -1):
            Character.ChangeHealth(amount)
            print(Character.health)
            update_Stam_Bar()
        def Char_Change_Health_minus_five(event = None, amount = -5):
            Character.ChangeHealth(amount)
            print(Character.health)
            update_Stam_Bar()
        def Char_Change_Health_minus_ten(event = None, amount = -10):
            Character.ChangeHealth(amount)
            print(Character.health)
            update_Stam_Bar()

        def Char_Change_Health_plus_one(event = None, amount = 1):
            Character.ChangeHealth(amount)
            print(Character.health)
            update_Stam_Bar()
        def Char_Change_Health_plus_five(event = None, amount = 5):
            Character.ChangeHealth(amount)
            print(Character.health)
            update_Stam_Bar()
        def Char_Change_Health_plus_ten(event = None, amount = 10):
            Character.ChangeHealth(amount)
            print(Character.health)
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
            updated_image = ImageTk.PhotoImage(Image.open(bar).resize((150,15), Image.NEAREST))
            Stamina_Bar.configure(image=updated_image)
            Stamina_Bar.image = updated_image
        update_Stam_Bar()
        
        

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





    


