import dis
import random
word_list =[ "PIZZA","BURGER","SPRINGROLLS","NOODLES","ICECREAM","CHOCOLATE"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
end_of_game = False
wrong=6
display=[]
Won= False

for i in range(word_len):
    display += '_'
    
print(display)



while not end_of_game:
    guess = input('Guess a letter :').upper()
    correct = False

    for position in range(word_len):
        letter = chosen_word[position]
        
        if(letter == guess):
            if(display[position] == '_'): 
                display[position] = guess
                correct = True
            else: break
                    
    if(correct):
        print(display)
    else:
        print(stages[wrong])
        print(display)
        wrong -= 1
        
    if(wrong == 0):
        print(stages[0])
        print('Lost! You let him hanged')
        break
    elif("_" not in display): 
        end_of_game = True
        print('Won! You saved the person')
        break
    
    
print('Game Over')
        
        
        
   


    
