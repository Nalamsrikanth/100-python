import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
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
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''']
list_words =["hangman", "hungama", "srikanth", "naveen", "sports"]
selected_word = random.choice(list_words)
word_len = len(selected_word)
display = list("_" * word_len)
print(f"{' '.join(display)}")
lives =  6
end_game = False
while end_game == False:
    guess_letter = input().lower()
    for position in range(word_len):
        if selected_word[position] == guess_letter:
            #print(f'the guess word is\n{guess_letter} and the position is\n{position}')
            display[position] = guess_letter

    print(f"{' '.join(display)}")

    if guess_letter not in selected_word:
        lives -= 1

        if  lives == 0:
            end_game = True
            print("you loss")
        print(stages[lives])


    if "_"  not in display:
        end_game = True
        print("you won")



