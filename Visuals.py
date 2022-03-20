
from time import sleep
from tkinter import *

from PIL import ImageTk, Image
from numpy import row_stack
import os
from Pokemon_Battle_pkg.audio import ah_here_it_is, choosing_pokemon, play_intro,play_homescreen, stop_all_sounds, traveling,waiting_for_pokemon




def Display_PokeData(Pokemon_Object):
    print(f"Name: {Pokemon_Object.Name}")
    print(f"Type: {Pokemon_Object.Type}")
    print("Attacks:")
    print(f"        {Pokemon_Object.Attack_1_Name}")
    print(f"        {Pokemon_Object.Attack_2_Name}")
    print(f"        {Pokemon_Object.Attack_3_Name}")
    print(f"        {Pokemon_Object.Attack_4_Name}")
    print(f"Weakness: {Pokemon_Object.Weakness}")
    print(f"Resistance: {Pokemon_Object.Resistance}\n")

def Intro():

    os.system('clear')
    stop_all_sounds()
    play_intro()
    sleep(.7)
    print("Hello there! Welcome to the world of pokémon!")
    sleep(3)
    print("My name is Oak! People call me the pokémon Prof!")
    sleep(3)
    prof_oak()
    os.system('clear')
    print("This world is inhabited by creatures called pokémon!")
    sleep(3)
    print("For some people, pokémon are pets.")
    sleep(2.7)
    print("Others use them for fights.")
    sleep(3)
    os.system('clear')
    print("Myself...I study pokémon as a profession.")
    sleep(3)
    print(".........")
    sleep(2.7)
    print("Where was I going with this...")
    sleep(3)
    os.system('clear')
    print("Oh yes, Welcome to the world of Pokemon!!!")
    sleep(3)
    print("I can see you are excited to start your new adventure...")
    sleep(3)
    print("You will encounter many different Pokemon creatures on your travels...")
    sleep(3.5)
    os.system('clear')
    print("So be careful...")
    sleep(2.5)
    print("But...before you go!")
    sleep(2.7)
    print("I have something to give you...")
    sleep(2.7)
    os.system('clear')
    ah_here_it_is()
    print("Ah...here it is!")
    sleep(4)
    stop_all_sounds()
    os.system('clear')
    choosing_pokemon()
    sleep(1)
    print("You get to choose a Pokemon companion to tag along on your journey to becoming a Pokemon Master!")
    sleep(3.5)
    print("Please choose carefully...")
    sleep(3)

def homescreen():
    os.system('clear')
    play_homescreen()
    print("Loading Game..")
    os.system('clear')
    sleep(1.5)
    print("Pokemon: NuCamp Editon\n")
    sleep(3)
    print("Inspiration from the World of Pokemon\n")
    input("Press Enter to Begin...")
def congrats():
    os.system('clear')
    print("Wow! You have defeated all the pokemon on your journey!")
    sleep(2.7)
    print("You have grown so much as a Pokemon trainer!")
    sleep(2.7)
    print("Please come back again to see if new Pokemon appear to improve your skills.")
    sleep(3)
    thank_you()



def show_attacks(pokemon_object):
    
    print(f"         {pokemon_object.Name}'s Attacks       ")
    print(f" __________________________________________")
    print(f"            1. {pokemon_object.Attack_1_Name}       ")
    print(f"            2. {pokemon_object.Attack_2_Name}       ")
    print(f"            3. {pokemon_object.Attack_3_Name}       ")
    print(f"            4. {pokemon_object.Attack_4_Name}       ")
    print(f"___________________________________________")

def journey_time():
    os.system('clear')
    stop_all_sounds()
    traveling()
    print("Time to get moving!")
    sleep(2.7)
    print("Remember, there are many pokemon creatures with different powers and abilities out there.")
    sleep(3.2)
    print("Learn and grow with your pokemon to overcome any obstacle.")
    sleep(2.7)
    os.system('clear')
    print("Always be ready for anything!")
    sleep(3)
    os.system('clear')
    stop_all_sounds()
    
def show_bush():
    root = Tk()
    
    root.title("Pokemon Game")
    
    root.iconbitmap('Pokemon_Battle_pkg\\Images\\icon2.ico')
    o_image = Image.open("Pokemon_Battle_pkg\\Images\\behind bush.jpg")
    resized_img = o_image.resize((640,480))
    my_img = ImageTk.PhotoImage(resized_img)
    my_label = Label(image=my_img)
    my_label.pack()

    start_button = Button(root, text="Press to go and take a look.",command=root.destroy,  pady=20, padx=50)
    start_button.pack()
    root.mainloop()
    return 

def prof_oak():
    root = Tk()
    
    root.title("Pokemon Game")
    
    root.iconbitmap('Pokemon_Battle_pkg\\Images\\icon2.ico')
    o_image = Image.open("Pokemon_Battle_pkg\\Images\\professor_oak.png")
    resized_img = o_image.resize((640,480))
    my_img = ImageTk.PhotoImage(resized_img)
    my_label = Label(image=my_img)
    my_label.pack()

    start_button = Button(root, text="Press to talk to Professor Oak.",command=root.destroy,  pady=20, padx=50)
    start_button.pack()
    root.mainloop()
    return 

def thank_you():
        root = Tk()

        root.title("Pokemon Game")

        root.iconbitmap('Pokemon_Battle_pkg\\Images\\icon2.ico')
        o_image = Image.open("Pokemon_Battle_pkg\\Images\\thankyou.png")
        resized_img = o_image.resize((640,480))
        my_img = ImageTk.PhotoImage(resized_img)
        my_label = Label(image=my_img)
        my_label.pack()

        start_button = Button(root, text="Goodbye!!!",command=root.destroy,  pady=20, padx=50)
        start_button.pack()
        root.mainloop()
        return 

def show_homescreen():
    root = Tk()
    
    root.title("Pokemon Game")
    play_homescreen()
    
    root.iconbitmap('Pokemon_Battle_pkg\\Images\\icon2.ico')
    o_image = Image.open("Pokemon_Battle_pkg\\Images\\Start_Screen.png")
    resized_img = o_image.resize((640,480))
    my_img = ImageTk.PhotoImage(resized_img)
    my_label = Label(image=my_img)
    my_label.pack()

    start_button = Button(root, text="Click Here To Start",command=root.destroy,  pady=20, padx=50)
    start_button.pack()
    root.mainloop()
    return 

def show_pokemon_image(pokemon_name):
    root = Tk()
    if pokemon_name == "Venusaur":
       
        
        root.title("Venusaur")
        root.iconbitmap('Pokemon_Battle_pkg\\Images\\icon2.ico')
        o_image = Image.open("Pokemon_Battle_pkg\\Images\\venusaur.jpg")
        resized_img = o_image.resize((640,480))
        my_img = ImageTk.PhotoImage(resized_img)
        my_label = Label(image=my_img)
        my_label.pack()

        start_button = Button(root, text="Click here to find out what it is!",command=root.destroy,  pady=20, padx=50)
        start_button.pack()
        root.mainloop()
        return
    elif pokemon_name == "Blastoise":
        
        
        root.title(pokemon_name)
        root.iconbitmap('Pokemon_Battle_pkg\\Images\\icon2.ico')
        o_image = Image.open("Pokemon_Battle_pkg\\Images\\Blastoise.png")
        resized_img = o_image.resize((640,480))
        my_img = ImageTk.PhotoImage(resized_img)
        my_label = Label(image=my_img)
        my_label.pack()

        start_button = Button(root, text="Click here to find out what it is!",command=root.destroy,  pady=20, padx=50)
        start_button.pack()
        root.mainloop()
        return
    elif pokemon_name == "Pikachu":
        
       
        root.title(pokemon_name)
        root.iconbitmap('Pokemon_Battle_pkg\\Images\\icon2.ico')
        o_image = Image.open("Pokemon_Battle_pkg\\Images\\Pikachu.png")
        resized_img = o_image.resize((640,480))
        my_img = ImageTk.PhotoImage(resized_img)
        my_label = Label(image=my_img)
        my_label.pack()

        start_button = Button(root, text="Click here to find out what it is!",command=root.destroy,  pady=20, padx=50)
        start_button.pack()
        root.mainloop()
        return
    elif pokemon_name == "Charizard":
        
        root.title(pokemon_name)
        root.iconbitmap('Pokemon_Battle_pkg\\Images\\icon2.ico')
        o_image = Image.open("Pokemon_Battle_pkg\\Images\\Charizard.png")
        resized_img = o_image.resize((640,480))
        my_img = ImageTk.PhotoImage(resized_img)
        my_label = Label(image=my_img)
        my_label.pack()

        start_button = Button(root, text="Click here to find out what it is!",command=root.destroy,  pady=20, padx=50)
        start_button.pack()
        root.mainloop()
        return
    else:
       
        root.title(pokemon_name)
        root.iconbitmap('Pokemon_Battle_pkg\\Images\\icon2.ico')
        o_image = Image.open("Pokemon_Battle_pkg\\Images\\Mew.png")
        resized_img = o_image.resize((640,480))
        my_img = ImageTk.PhotoImage(resized_img)
        my_label = Label(image=my_img)
        my_label.pack()

        start_button = Button(root, text="Click here to find out what it is!",command=root.destroy,  pady=20, padx=50)
        start_button.pack()
        root.mainloop()
        return
     