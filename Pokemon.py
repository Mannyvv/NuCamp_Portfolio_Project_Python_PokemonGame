
from cgitb import reset
import os
from time import sleep
from tkinter.tix import Tree
import pandas as pd
import random
from Pokemon_Battle_pkg.Visuals import Display_PokeData, journey_time
from Pokemon_Battle_pkg.audio import obtained_pokemon, stop_all_sounds


def Initiate_Pokemon_Data():


    ExcelFile = 'Pokemon_Data.xlsx'     ## Uploads the Pokemon information bank from "Pokemon_Data.xlsx file."
    PokeData = pd.read_excel(ExcelFile)

    TotalPokemon = PokeData.shape[0]           # Counts the total rows in .xlsx file, which equals the number of Pokemon in info bank.

    PokemonInfoList = []
    for EachPokemon in range(0, TotalPokemon, 1):           # Stores data of each Pokemon in Pokemon_List as an element
        PokemonInfoList.append(PokeData.iloc[EachPokemon])

    Title_Holder = PokemonInfoList[0].index
    TitleNames = {}
    for NumberOfPokemon in Title_Holder:
           TitleNames[NumberOfPokemon] = None                    # Stores the title for the elements in Pokemon_List as keys
    return TitleNames, PokemonInfoList                          # Dictionary and List Type


def Initiate_Pokemon(TitleNames, PokemonInfoList):
    PokemonInfoDic = {}
    KeysList = list(TitleNames)
    key_iter = 0
    Pokemon_Objects_List = []
    for i in range(len(PokemonInfoList)):
        key_iter = 0
        for y in PokemonInfoList[i]:
            PokemonInfoDic[KeysList[key_iter]] = y
            key_iter += 1
        NewPokemon = Pokemon()
        NewPokemon.UploadData(PokemonInfoDic)
        Pokemon_Objects_List.append(NewPokemon)

    return Pokemon_Objects_List


class Pokemon:
    def __init__(self):
        self.Player = False
        self.PokemonNumber = None
        self.Name = None
        self.HitPoints= None
        self.Type = None
        self.Attack_1_Name= None
        self.Attack_2_Name= None
        self.Attack_3_Name= None
        self.Attack_4_Name= None
        self.Attack_1_Damage= None
        self.Attack_2_Damage= None
        self.Attack_3_Damage= None
        self.Attack_4_Damage= None
        self.Weakness= None
        self.Resistance= None
        self.Fact= None

    def UploadData(self, DataIn):
        self.PokemonNumber = DataIn['PokemonNumber']
        self.Name = DataIn['Name']
        self.HitPoints = DataIn['HitPoints']
        self.Type = DataIn['Type']
        self.Attack_1_Name  = DataIn['Attack_1_Name']
        self.Attack_2_Name = DataIn['Attack_2_Name']
        self.Attack_3_Name = DataIn['Attack_3_Name']
        self.Attack_4_Name = DataIn['Attack_4_Name']
        self.Attack_1_Damage = DataIn['Attack_1_Damage']
        self.Attack_2_Damage = DataIn['Attack_2_Damage']
        self.Attack_3_Damage = DataIn['Attack_3_Damage']
        self.Attack_4_Damage = DataIn['Attack_4_Damage']
        self.Weakness = DataIn['Weakness']
        self.Resistance = DataIn['Resistance']
        self.Fact = DataIn['Fact']

    def Reset_HP(self, Reset_Data):
        self.HitPoints = Reset_Data.HitPoints
        


   


def Choose_Pokemon(Pokemon_Choices):
    Reviewing = True
    while Reviewing:
        while True:
            try:
                os.system('clear')
                print(f"These are the {len(Pokemon_Choices)} Pokemon you can choose from...")
    
                for x in range(len(Pokemon_Choices)):
                     print(f"{x+1}. {Pokemon_Choices[x].Name}\n")
                View_Choice = int(input("Which Pokemon do you want to see?  \n"))
                if View_Choice <= len(Pokemon_Choices) and View_Choice > 0:
                    break
            except ValueError:
                continue
        View_Choice -= 1    
        while True:
            
            os.system('clear')
            Display_PokeData(Pokemon_Choices[View_Choice])
            Confirmation = input(f"Do you want to choose {Pokemon_Choices[View_Choice].Name}? (y/n): \n")
            if Confirmation == "y" or Confirmation == "n":
                break
            else: 
                continue


        if Confirmation == "y":
            Final_Choice = View_Choice
            os.system('clear')
            stop_all_sounds()
            sleep(1)
            obtained_pokemon()
            print(f"Great! {Pokemon_Choices[View_Choice].Name} is excited to be your friend!")
            sleep(4)
            journey_time()
            Players_Pokemon = Pokemon_Choices.pop(Final_Choice)
            Players_Pokemon.Player = True
            Pokemon_OPP = Pokemon_Choices
            random.shuffle(Pokemon_OPP)
            Reviewing = False
        else:
            os.system('clear')
            for x in range(len(Pokemon_Choices)):
                print(f"{x+1}. {Pokemon_Choices[x].Name}\n")
                continue
    return Players_Pokemon, Pokemon_OPP            #Returns player choice and sets opponents




    










