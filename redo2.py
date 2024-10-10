import random
import time
import os


def calculate_hit(skill, fatigue, targets, shot):
    if skill * fatigue < random.randint(1, 100)/100:
        print('Miss')
        return
        
    if targets[int(shot) - 1] == '*':
        print('Hit on open target\n')
        targets[int(shot) - 1] = 'O'
    else:
        print('Hit on closed target\n')
        
    

def game(skill, fatigue, num_targets):
    targets = ['*' for _ in range(num_targets)]
    print(f'you got {num_targets} shots')
    
    for i in range(num_targets):
        print(' '.join(targets)+'\n')
        
        shot = input(f'Shot number {i + 1} at: ')
        calculate_hit(skill, fatigue, targets, shot)
       
    print(' '.join(targets)+'\n')
    print(f'You hit {targets.count("O")} out of {num_targets}')
    clear_screen_after_delay(2)
    return targets.count("O")


def create_players():
    player1 = {
        'name':'Player1',
        'skill':random.randint(85, 100)/100,
        'fatigue':random.randint(90, 100)/100,
        'score':0
    } 
    
    player2 = {
        'name':'Player2',
        'skill':random.randint(85, 100)/100,
        'fatigue':random.randint(90, 100)/100,
        'score':0
    }    
    
    return player1, player2



def start_game():
    v = '''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Biathlon

            a hit or miss game
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    print(v)
    clear_screen_after_delay(2)
    
    num_targets = int(input('number of targets? '))
    playto = int(input('winning score? '))
    clear_screen_after_delay(1)
    
    return num_targets, playto

def player_round(player, num_targets):
    print(f'{player["name"]}:')
    
    player['score'] += game(player['skill'], player['fatigue'], num_targets) 
    
    player['fatigue'] *= random.randint(90, 100)/100
   
def check_win(score1, score2, playto):
    if max([score1, score2]) >= playto:
        print(f'player {[score1, score2].index(max([score1, score2])) + 1} wins!!!!!!')
        return True
    return False
    
   
def game_round(round_number, num_targets, player1, player2):
    print(f'begin round {round_number}...\n')
    
    player_round(player1, num_targets)
    time.sleep(1)
    player_round(player2, num_targets)
    
    print(f'\nscore: {player1["score"]}-{player2["score"]}\n')
    clear_screen_after_delay(2)

def clear_screen_after_delay(seconds):
    time.sleep(seconds)
    os.system('cls')

if __name__ == '__main__':
    player1, player2 = create_players()
    num_targets, playto = start_game()
    
    x = 0
    while True:
        x += 1
        game_round(x, num_targets, player1, player2)
        if check_win(player1['score'], player2['score'], playto):
            break
    
    


