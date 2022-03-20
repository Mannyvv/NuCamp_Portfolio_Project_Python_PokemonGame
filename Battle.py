
import os
import random
from tracemalloc import stop
from xml.dom.minidom import Element
from Pokemon_Battle_pkg.Visuals import show_attacks, show_pokemon_image,show_bush
from time import sleep
from tkinter.tix import Tree
from Pokemon_Battle_pkg.Pokemon import Pokemon
from Pokemon_Battle_pkg.audio import pokemon_heal, stop_all_sounds, victory, waiting_for_pokemon, wild_pokemon,attack_sound, play_lost_battle


def Pokemon_Attack(self,Pokemon1,Pokemon2):  
        if Pokemon1.Player:
            while True:
                try:
                    os.system('clear')
                    show_attacks(Pokemon1)
                    Player_choice = int(input(f"What attack will {Pokemon1.Name} use?(1~4)  "))
                    if Player_choice <=4 and Player_choice >= 1:
                        break
                except ValueError:
                    continue
            if Player_choice == 1:
                self.Attack_Text(Pokemon1.Name, Pokemon1.Attack_1_Name)
                if Pokemon2.Weakness == Pokemon1.Type:
                    actual_damage = int(Pokemon1.Attack_1_Damage*random.triangular(0,.9,1) + 20)
                    Pokemon2.HitPoints -= actual_damage
                else:
                    actual_damage = int(Pokemon1.Attack_1_Damage*random.triangular(0,.9,1))
                    Pokemon2.HitPoints -= actual_damage
                attack_sound(Pokemon1.Name,int(Player_choice))
                self.Attack_Damage(Pokemon1.Name, Pokemon2.Name, actual_damage)
                self.show_hp(Pokemon1.Name, Pokemon2.Name, Pokemon1.HitPoints, Pokemon2.HitPoints)
                return None

            elif Player_choice == 2:
                self.Attack_Text(Pokemon1.Name, Pokemon1.Attack_2_Name)
                if Pokemon2.Weakness == Pokemon1.Type:
                    actual_damage = int(Pokemon1.Attack_2_Damage*random.triangular(0,.9,1) + 20)
                    Pokemon2.HitPoints -= actual_damage
                else:
                    actual_damage = int(Pokemon1.Attack_2_Damage*random.triangular(0,.9,1))
                    Pokemon2.HitPoints -= actual_damage
                
                attack_sound(Pokemon1.Name,int(Player_choice))
                self.Attack_Damage(Pokemon1.Name, Pokemon2.Name, actual_damage)
                self.show_hp(Pokemon1.Name, Pokemon2.Name, Pokemon1.HitPoints, Pokemon2.HitPoints)
                return None
            elif Player_choice == 3:
                self.Attack_Text(Pokemon1.Name, Pokemon1.Attack_3_Name)
                if Pokemon2.Weakness == Pokemon1.Type:
                    actual_damage = int(Pokemon1.Attack_3_Damage*random.triangular(0,.9,1) + 20)
                    Pokemon2.HitPoints -= actual_damage
                else:
                    actual_damage = int(Pokemon1.Attack_3_Damage*random.triangular(0,.9,1))
                    Pokemon2.HitPoints -= actual_damage
               
                attack_sound(Pokemon1.Name,int(Player_choice))
                self.Attack_Damage(Pokemon1.Name, Pokemon2.Name, actual_damage)
                self.show_hp(Pokemon1.Name, Pokemon2.Name, Pokemon1.HitPoints, Pokemon2.HitPoints)
                return None
            else:
                self.Attack_Text(Pokemon1.Name, Pokemon1.Attack_4_Name)
                if Pokemon2.Weakness == Pokemon1.Type:
                    actual_damage = int(Pokemon1.Attack_4_Damage*random.triangular(0,.5,1) + 20)
                    Pokemon2.HitPoints -= actual_damage
                else:
                    actual_damage = int(Pokemon1.Attack_4_Damage*random.triangular(0,.5,1))
                    Pokemon2.HitPoints -= actual_damage
                
                attack_sound(Pokemon1.Name,int(Player_choice))
                self.Attack_Damage(Pokemon1.Name, Pokemon2.Name, actual_damage)
                self.show_hp(Pokemon1.Name, Pokemon2.Name, Pokemon1.HitPoints, Pokemon2.HitPoints)
                return None
       
        else:
            Comp_Choice = random.randrange(1,4)
            if Comp_Choice == 1:
                self.Attack_Text(Pokemon1.Name, Pokemon1.Attack_1_Name)

                if Pokemon2.Weakness == Pokemon1.Type:
                    actual_damage = int(Pokemon1.Attack_1_Damage*random.triangular(0,.9,1) + 20)
                    Pokemon2.HitPoints -= actual_damage
                else:
                    actual_damage = int(Pokemon1.Attack_1_Damage*random.triangular(0,.9,1))
                    Pokemon2.HitPoints -= actual_damage
                attack_sound(Pokemon1.Name,int(Comp_Choice))
                self.Attack_Damage(Pokemon1.Name, Pokemon2.Name, actual_damage)
                self.show_hp(Pokemon1.Name, Pokemon2.Name, Pokemon1.HitPoints, Pokemon2.HitPoints)
                return None
            elif Comp_Choice == 2:
                self.Attack_Text(Pokemon1.Name, Pokemon1.Attack_2_Name)
                if Pokemon2.Weakness == Pokemon1.Type:
                    actual_damage = int(Pokemon1.Attack_2_Damage*random.triangular(0,.9,1) + 20)
                    Pokemon2.HitPoints -= actual_damage
                else:
                    actual_damage = int(Pokemon1.Attack_2_Damage*random.triangular(0,.9,1))
                    Pokemon2.HitPoints -= actual_damage
                attack_sound(Pokemon1.Name,int(Comp_Choice))
                self.Attack_Damage(Pokemon1.Name, Pokemon2.Name, actual_damage)
                self.show_hp(Pokemon1.Name, Pokemon2.Name, Pokemon1.HitPoints, Pokemon2.HitPoints)
                return None
            elif Comp_Choice == 3:
                self.Attack_Text(Pokemon1.Name, Pokemon1.Attack_3_Name)
                if Pokemon2.Weakness == Pokemon1.Type:
                    actual_damage = int(Pokemon1.Attack_3_Damage*random.triangular(0,.9,1) + 20)
                    Pokemon2.HitPoints -= actual_damage
                else:
                    actual_damage = int(Pokemon1.Attack_3_Damage*random.triangular(0,.9,1))
                    Pokemon2.HitPoints -= actual_damage
                attack_sound(Pokemon1.Name,int(Comp_Choice))
                self.Attack_Damage(Pokemon1.Name, Pokemon2.Name, actual_damage)
                self.show_hp(Pokemon1.Name, Pokemon2.Name, Pokemon1.HitPoints, Pokemon2.HitPoints)
                return None
            else:
                self.Attack_Text(Pokemon1.Name, Pokemon1.Attack_4_Name)
                if Pokemon2.Weakness == Pokemon1.Type:
                    actual_damage = int(Pokemon1.Attack_4_Damage*random.triangular(0,.5,1) + 20)
                    Pokemon2.HitPoints -= actual_damage
                else:
                    actual_damage = int(Pokemon1.Attack_4_Damage*random.triangular(0,.5,1))
                    Pokemon2.HitPoints -= actual_damage
                attack_sound(Pokemon1.Name,int(Comp_Choice))
                self.Attack_Damage(Pokemon1.Name, Pokemon2.Name, actual_damage)
                self.show_hp(Pokemon1.Name, Pokemon2.Name, Pokemon1.HitPoints, Pokemon2.HitPoints)
                return None


class Battle():
    def __init__(self, Pokemon1, Pokemon2):
        self.Pokemon1 = Pokemon1
        self.Pokemon2 = Pokemon2
        self.Winner = None
        self.Loser = None
        self.UserWins = False
        

    def Attack_Text(self,PokemonName1, AttackName):
        os.system('clear')
        print(f"{PokemonName1} will use {AttackName}!")
        sleep(1.5)

    def Attack_Damage(self,PokemonName1,PokemonName2, AttackDamage):
        print(f"{PokemonName1} has inflicted {AttackDamage} hp in attack damage onto {PokemonName2}!")
        sleep(3)

    
    def show_hp(self, PokemonName1,PokemonName2, pokemonhp1, pokemonhp2):
        os.system("clear")
        if pokemonhp1 <= 0:
            print(f"{PokemonName1} has 0 hp\n")
            print(f"{PokemonName2} has {pokemonhp2} hp\n")
            sleep(3.5)
        elif pokemonhp2 <= 0:
            print(f"{PokemonName1} has {pokemonhp1} hp\n")
            print(f"{PokemonName2} has 0 hp\n")
            sleep(3.5)
        else:
            print(f"{PokemonName1} has {pokemonhp1} hp\n")
            print(f"{PokemonName2} has {pokemonhp2} hp\n")
            sleep(3.5)


    def Pokemon_Battle(self):
        Pokemon_Holder = [self.Pokemon1, self.Pokemon2]
        sleep(1)
        waiting_for_pokemon()
        print("Wait! What is hidng behind that bush!?")
        sleep(2.7)
        show_bush()
        print(".")
        sleep(2)
        print("..")
        sleep(2)
        print("...")
        sleep(2)
        stop_all_sounds()
        sleep(.5)
        wild_pokemon()
        os.system('clear')
        print(f"Watch out, you have an encountered a challenger Pokemon!\n")
        sleep(2.5)
        show_pokemon_image(self.Pokemon2.Name)
        print(f"It's a wild {self.Pokemon2.Name}\n\n")
        sleep(2)
        enter_battle = input(f"Should {self.Pokemon1.Name} enter battle?(y/n) ")
        if enter_battle == "n":
            return None
        sleep(1.5)
        while True :
            
            Pokemon_Attack(self, Pokemon_Holder[0], Pokemon_Holder[1])
            if self.Pokemon1.HitPoints <= 0:
                sleep(2)
                print(f"Oh no, that was a damaging hit...{self.Pokemon1.Name} has fainted")
                sleep(3)
                self.Winner = self.Pokemon2
                self.Loser = self.Pokemon1

                break
            elif self.Pokemon2.HitPoints <= 0:
                sleep(3)
                print(f"What a hit! {self.Pokemon2.Name} has fainted!")
                sleep(2)
                self.Winner = self.Pokemon1
                self.Loser = self.Pokemon2
                self.UserWins = True
                break
            else:
                Pokemon_Holder.reverse()
        return None

    def Battle_Summary(self,boolean):
        if boolean:
            stop_all_sounds()
            victory()
            print(f"\nYou and your Pokemon have won the battle! Congratulations!!!")
            sleep(5)
            os.system('clear')
            input("Let's heal your Pokemon and get on our way shall we? ")

            stop_all_sounds()
            pokemon_heal()
            os.system('clear')
            print("Your Pokemon is nice and healthy again.")
            sleep(3)
            os.system('clear')
        
        else:
            stop_all_sounds()
            play_lost_battle()
            print(f"\nYou have lost the battle! Try to master your Pokemon and improve your skills for next time!")
            sleep(4)
            os.system('clear')
            print(f"Goodbye!!!")
            sleep(2)
        return None

    


