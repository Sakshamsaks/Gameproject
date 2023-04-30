import random
print("---------------WELCOME TO THE ROCK PAPER SCISSOR GAME---------------")
while(True):
    n=input("\nEnter your name: ")
    b=input('\nEnter your choice: ')
    ls=['rock','papar','scissor']
    c=random.choice(ls)
    if ((c=='scissor' and b=='papar')or(c=='rock'and b=='scissor')or(c=='papar'and b=='rock')):
        print('\nComputer Win the Game!')
    elif ((c=='papar' and b=='scissor') or (c=='scissor' and b=='rock') or (c=='rock' and b== 'papar')):
        print (n,'Win the Game!')
    else:
        print('\nMatch is draw')
    print("\nPress any key if you wants to play again....otherwise press 'Q'")
    w=input()
    if w=='Q':
        break
print('\nTHANK YOU... For playing the game')
