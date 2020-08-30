#Rock Paper Scissor Game
from datetime import datetime
import random

def Title():
    print(' ____            _    ____                       ____       _               ')
    print('|  _ \ ___   ___| | _|  _ \ __ _ _ __   ___ _ __/ ___|  ___(_)___ ___  ___  ____')
    print("| |_) / _ \ / __| |/ / |_) / _` | '_ \ / _ \ '__\___ \ / __| / __/ __|/ _ \| '__|")
    print("|  _ < (_) | (__|   <|  __/ (_| | |_) |  __/ |   ___) | (__| \__ \__ \ (_) | |")
    print("|_| \_\___/ \___|_|\_\_|   \__,_| .__/ \___|_|  |____/ \___|_|___/___/\___/|_|")
    print("                                |_|                                         ")


Title()
#print('Rock,Paper,Scissor\n------------------')
while True:
    #com_choice = random.choice(['rock','paper','scissor'])
    time_now = datetime.now().second
    choices = ['rock','paper','scissor','exit']
    com_choice = choices[time_now%3]
    print('1)Rock\n2)Paper\n3)Scissor\n4)Exit')
    x=str(input('Enter your choice: ')).lower()
    Results = ['Draw!','You Win!','You lost!']
    
    if x not in choices:
        print('Wrong input! Try again\n')
    else:
        if com_choice == x:
            who_win = 0
        elif x == 'exit':
            print('Thank You!!')
            break
        else:
            if com_choice == 'rock':
                if x == 'paper':
                    who_win = 1
                else:
                    who_win = 2
            elif com_choice == 'paper':
                if x == 'rock':
                    who_win = 2
                else:
                    who_win = 1
            elif com_choice == 'scissor':
                if x == 'rock':
                    who_win = 1
                else:
                    who_win = 2
        print('com_choice:',com_choice)
        print('\n***********\n',Results[who_win],'\n***********\n')
    


