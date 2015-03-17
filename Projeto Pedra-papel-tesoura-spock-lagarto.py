# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:22:16 2015

@author: Lucas

Jogue o jogo rock-paper-scissors agora com lizard e spock!

clique em run e comece sua aventura!

por lucas scarlato astur
"""

import random

Comprandom = ["rock" , "paper", "scissor", "lizard", "spock"]
computer_score = 0
user_score = 0
turns = 0

r = "rock"
p = "paper"
s = "scissor"
l = "lizard"
sp = "spock"



while turns <3:
    a = input("escolha sua arma!")
    comp_choice = random.choice(Comprandom)
    turns+=1
    print(comp_choice)
    
    if comp_choice == "rock" and (a == p or a== sp):
        print ("boa!")
        user_score +=1
        
    if comp_choice == "rock" and (a == l or a == s):
        print ("mal")
        computer_score +=1
        
    if comp_choice == "paper" and (a == s or a == l):
        print ("boa!")
        computer_score +=1
        
    if comp_choice == "scissor" and (a == r or a == sp):
        print ("boa parca!")
        user_score +=1
        
    if comp_choice == "paper" and (a == sp or a == r):
        print ("foi mal hein?")
        computer_score +=1
        
    if comp_choice == "scissor" and (a == l or a == p):
        print ("nao foi desta vez parca")
        computer_score +=1
        
    if comp_choice == "lizard" and (a == r or a == s):
        print ("boa!")
        user_score +=1
        
    if comp_choice == "lizard" and (a == sp or a == p):
        print ("perdeu playboy")
        computer_score +=1
        
    if comp_choice == "spock" and (a == l or a == p):
        print ("boaaaa")
        user_score +=1
        
    if comp_choice == "spock" and (a == r or a == s):
        print("mallz")
        computer_score +=1
        
        
if turns == 3:
    print ("acabou!")
    print ("o PC acertou", computer_score)
    print ( "Voce acertou", user_score)
    if user_score > computer_score:
        print ("Parabens campeao!")
    if computer_score > user_score:
        print ("Mas que ma sorte!")
    if computer_score == user_score:
        print ("nao deu em poha nenhuma")
        