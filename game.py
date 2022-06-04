print('ROCK PAPER AND SCISSORS GAME')
import random

choices = ['R', 'P', 'S']


comp = random.choice(choices) 
player_choice = None
while player_choice not in choices: 
    player_choice = input('rock, paper or scissors  ').upper()
    if player_choice == comp :
        print('Player ' +(player_choice) + ':' 'CPU '+ (comp)) 
        print('TIE! PLAY AGAIN')    
    elif comp == 'R':
        if player_choice == 'P':
            print('Player ' + (player_choice) + ':' 'CPU '+ (comp)) 
            print('YOU WIN')
        if player_choice == 'S':
           print('Player ' + (player_choice) + ':' 'CPU '+ (comp))
           print('YOU LOSE')
    elif comp == 'P':
        if player_choice == 'R':
            print('Player ' + (player_choice) + ':' 'CPU '+ (comp))
            print('YOU LOSE')
        if player_choice == 'S':
            print('Player ' + (player_choice) + ':' 'CPU '+ (comp))
            print('YOU WIN')
    elif comp == 'S':
        if player_choice == 'P':
            print('Player ' + (player_choice) + ':' 'CPU '+ (comp))
            print('YOU LOSE')
        if player_choice == 'R':
            print('Player ' + (player_choice) + ':' 'CPU '+ (comp))
            print('YOU WIN') 

