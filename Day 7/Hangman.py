
import random

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

word_list=["ardvak","baboon","camel"]
end_of_game=False                                                          # end_of_game=0
lives=6
chosen_word=random.choice(word_list)
print(chosen_word)
word_length=len(chosen_word)

display=[]
for _ in range(word_length):
    display+="_"
print(display)
  
while not end_of_game:                                                      # while end_of_game<word_length:
    guess = input("Guess a letter: ").lower()
                                                                            # end_of_game+=1
    boll=False
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
                display[position] = letter       
                boll=True  
    print(display)    
    if boll==False:
        lives-=1
        print(f"No. of lifes Reamning are {lives}")   
        print(display)
        print(stages[lives])
        if lives==0:
            end_of_game=True
            

