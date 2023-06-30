import random
from hangam_art import logo, stages

word_list = ['ironman', 'captain america', 'hulk']   # you can replace manes here...
chosen_word = random.choice(word_list)
print(logo)

wrd_len = len(chosen_word)
lives = 6
display = []
end = True
for _ in range(wrd_len): 
        display+='_'
print(display)

while end:
    gussed_wrd = input("Guess the word: ")
    if gussed_wrd in display:
        print("The word is already guessed!!")
    if gussed_wrd not in chosen_word:
        print(f"The word '{gussed_wrd}' is not in the word")
        
    for position in range(wrd_len):
        letter = chosen_word[position]
        if gussed_wrd == letter:
            display[position]=letter
    print(display)       
    
   
    if gussed_wrd not in chosen_word:
        lives-=1
        print(stages[lives])
        print("You lose a life")
        if lives == 0:
            print("Game Over!!")
            end = False
    if '_' not in display:
        print(" Congratulations,You Win!!")
        end = False
