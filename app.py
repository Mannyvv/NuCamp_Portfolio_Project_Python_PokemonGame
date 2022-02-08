from asyncore import loop
from time import sleep
from Pokemon_Battle_pkg.Battle import Battle
from Pokemon_Battle_pkg.Pokemon import Initiate_Pokemon_Data, Initiate_Pokemon, Choose_Pokemon, Pokemon
from Pokemon_Battle_pkg.Visuals import homescreen, Intro, show_homescreen, congrats



show_homescreen()
All_Titles, All_Pokemon_Info = Initiate_Pokemon_Data()
Initiated_Pokemon = Initiate_Pokemon(All_Titles, All_Pokemon_Info)
##homescreen()
Intro()
Players_Pokemon_OutBattle, Opponent_Pokemons = Choose_Pokemon(Initiated_Pokemon)
Battle_List = []


Number_of_Battles = len(Opponent_Pokemons)
Players_Pokemon_InBattle = Players_Pokemon_OutBattle
Reset_HP = Players_Pokemon_InBattle.HitPoints
wins = 0


for battle_N in range(Number_of_Battles):

    Fight_Holder = Battle(Players_Pokemon_InBattle, Opponent_Pokemons[battle_N])
    Fight_Holder.Pokemon_Battle()
    Fight_Holder.Battle_Summary(Fight_Holder.UserWins)
    Players_Pokemon_InBattle.HitPoints = Reset_HP
    if Fight_Holder.UserWins != True:
        break
    else:
        wins +=1
    Battle_List.append(Fight_Holder)

if wins == Number_of_Battles:
    congrats()

