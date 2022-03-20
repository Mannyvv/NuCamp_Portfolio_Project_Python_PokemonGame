from ast import ExtSlice
from time import sleep
from tkinter import *
import pygame




pygame.mixer.init()
pygame.mixer.set_num_channels(64)

def play_homescreen():
    

    pygame.mixer.Channel(0).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\Opening.mp3'),loops=10)
    new_volu = pygame.mixer.Channel(0).get_volume()
    pygame.mixer.Channel(0).set_volume(new_volu*.30)


def play_intro():
    
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\Professor Oak.mp3'), loops=10)
    new_volu = pygame.mixer.Channel(1).get_volume()
    pygame.mixer.Channel(1).set_volume(new_volu*.30)

def choosing_pokemon():
    
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\1-20 - Pokémon Gym.mp3'), loops=10)
    new_volu = pygame.mixer.Channel(2).get_volume()
    pygame.mixer.Channel(2).set_volume(new_volu*.30)

def pokemon_heal():
    pygame.mixer.Channel(3).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\1-11 - Recovery.mp3'))

def victory():
    pygame.mixer.Channel(4).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\22 Victory! (Trainer Battle).mp3'), loops=10)

def wild_pokemon():
    pygame.mixer.Channel(5).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\Battle (VS Wild Pokémon).mp3'),loops=10)
    new_volu = pygame.mixer.Channel(5).get_volume()
    pygame.mixer.Channel(5).set_volume(new_volu*.30)

def ah_here_it_is():
    pygame.mixer.Channel(6).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\item_sound.mp3'))
    new_volu = pygame.mixer.Channel(6).get_volume()
    pygame.mixer.Channel(6).set_volume(new_volu*.30)

def traveling():
    pygame.mixer.Channel(7).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\road_to.mp3'))
    new_volu = pygame.mixer.Channel(7).get_volume()
    pygame.mixer.Channel(7).set_volume(new_volu*.30)

def play_lost_battle():
    pygame.mixer.Channel(8).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\lost_battle2.mp3'),loops=2)
    new_volu = pygame.mixer.Channel(8).get_volume()
    pygame.mixer.Channel(8).set_volume(new_volu*.30)

def waiting_for_pokemon():
    pygame.mixer.Channel(17).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\waiting.mp3'))
    new_volu = pygame.mixer.Channel(17).get_volume()
    pygame.mixer.Channel(17).set_volume(new_volu*.30)

def obtained_pokemon():
    pygame.mixer.Channel(18).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\Fanfare Pokémon Caught.mp3'))
    new_volu = pygame.mixer.Channel(18).get_volume()
    pygame.mixer.Channel(18).set_volume(new_volu*.30)



def attack_sound(pokemon_name, attack_number):
    if pokemon_name == "Pikachu":
        if attack_number == 1:
            pygame.mixer.Channel(9).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\Electrify.mp3'))
            sleep(4)
            pygame.mixer.Channel(9).stop()
        elif attack_number == 2:
            pygame.mixer.Channel(10).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\Thunder Shock.mp3'))
            sleep(4)
            pygame.mixer.Channel(10).stop()
        elif attack_number == 3:
            pygame.mixer.Channel(11).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\Electro Ball.mp3'))
            sleep(4)
            pygame.mixer.Channel(11).stop()
        elif attack_number == 4:
            pygame.mixer.Channel(12).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\Thunderbolt.mp3'))
            sleep(4)
            pygame.mixer.Channel(12).stop()

    elif pokemon_name == "Charizard":
        if attack_number == 1:
            pygame.mixer.Channel(13).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\fEmber.mp3'))
            sleep(4)
            pygame.mixer.Channel(13).stop()
        elif attack_number == 2:
            pygame.mixer.Channel(14).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\fireblast.mp3'))
            sleep(4)
            pygame.mixer.Channel(14).stop()
        elif attack_number == 3:
            pygame.mixer.Channel(15).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\FirePunch.mp3'))
            sleep(4)
            pygame.mixer.Channel(15).stop()
        elif attack_number == 4:
            pygame.mixer.Channel(16).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\Flamethrower.mp3'))
            sleep(4)
            pygame.mixer.Channel(16).stop()
    elif pokemon_name == "Blastoise":
        if attack_number == 1:
            pygame.mixer.Channel(13).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\WaterGun.mp3'))
            sleep(4)
            pygame.mixer.Channel(13).stop()
        elif attack_number == 2:
            pygame.mixer.Channel(14).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\wBubblebeam2.mp3'))
            sleep(4)
            pygame.mixer.Channel(14).stop()
        elif attack_number == 3:
            pygame.mixer.Channel(15).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\FirePunch.mp3'))
            sleep(4)
            pygame.mixer.Channel(15).stop()
        elif attack_number == 4:
            pygame.mixer.Channel(16).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\Flamethrower.mp3'))
            sleep(4)
            pygame.mixer.Channel(16).stop()
    elif pokemon_name == "Venusaur":
        if attack_number == 1:
            pygame.mixer.Channel(13).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\pCut.mp3'))
            sleep(4)
            pygame.mixer.Channel(13).stop()
        elif attack_number == 2:
            pygame.mixer.Channel(14).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\Poisoned.mp3'))
            sleep(4)
            pygame.mixer.Channel(14).stop()
        elif attack_number == 3:
            pygame.mixer.Channel(15).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\pRazorWind.mp3'))
            sleep(4)
            pygame.mixer.Channel(15).stop()
        elif attack_number == 4:
            pygame.mixer.Channel(16).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\pSolarBeam3.mp3'))
            sleep(4)
            pygame.mixer.Channel(16).stop()
    elif pokemon_name == "Blastoise":
        if attack_number == 1:
            pygame.mixer.Channel(13).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\WaterGun.mp3'))
            sleep(4)
            pygame.mixer.Channel(13).stop()
        elif attack_number == 2:
            pygame.mixer.Channel(14).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\wBubblebeam2.mp3'))
            sleep(4)
            pygame.mixer.Channel(14).stop()
        elif attack_number == 3:
            pygame.mixer.Channel(15).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\FirePunch.mp3'))
            sleep(4)
            pygame.mixer.Channel(15).stop()
        elif attack_number == 4:
            pygame.mixer.Channel(16).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\Flamethrower.mp3'))
            sleep(4)
            pygame.mixer.Channel(16).stop()
    elif pokemon_name == "Mew":
        if attack_number == 1:
            pygame.mixer.Channel(13).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\mewConfusion.mp3'))
            sleep(4)
            pygame.mixer.Channel(13).stop()
        elif attack_number == 2:
            pygame.mixer.Channel(14).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\mewHypnosis.mp3'))
            sleep(4)
            pygame.mixer.Channel(14).stop()
        elif attack_number == 3:
            pygame.mixer.Channel(15).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\mewPsybeam3.mp3'))
            sleep(4)
            pygame.mixer.Channel(15).stop()
        elif attack_number == 4:
            pygame.mixer.Channel(16).play(pygame.mixer.Sound('Pokemon_Battle_pkg\\Sounds\\mewPsychic.mp3'))
            sleep(4)
            pygame.mixer.Channel(16).stop()


def stop_all_sounds():
    pygame.mixer.stop()
   
    
