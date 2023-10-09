# take input from the user after that computer will choose randomly and give whoever wins it 

# R -1, P 0,  S 1
#          -1  0  1
# cases :   R  P  S    -> computer
#  -1  R    D  Wi Lo                        cases  :    -1 0  -> 0   |  0 1 -> 1 | 1 -1 -> -1 
#   0  P    Lo D  Wi
#   1  S    Wi Lo D

# if same then give draw as answer 

import random

def checkwinner(game_dictionary_number_to_words,user_input,computer_input):
   

   # To ensure that there is always an unique input
   if computer_input == user_input :
       while(computer_input== user_input):
           computer_input = random.randrange(-1,1)
       
   if user_input == 0 and computer_input == -1 :
       print("You Won The game Your choice was : ", game_dictionary_number_to_words[user_input] , "\n It's Choice was : ", game_dictionary_number_to_words[computer_input])
   elif computer_input == 0 and user_input == -1 : 
       print("Computer Won The game It's choice was : ", game_dictionary_number_to_words[computer_input], "\n Your Choice was : ", game_dictionary_number_to_words[user_input] )
   
   elif user_input == 1 and computer_input == 0 :
       print("You Won The game Your choice was : ", game_dictionary_number_to_words[user_input] , "\n It's Choice was : ", game_dictionary_number_to_words[computer_input])
   elif computer_input == 1 and user_input == 0 : 
       print("Computer Won The game It's choice was : ", game_dictionary_number_to_words[computer_input], "\n Your Choice was : ", game_dictionary_number_to_words[user_input] )

   elif user_input == -1 and computer_input == 1 :
       print("You Won The game Your choice was : ", game_dictionary_number_to_words[user_input] , "\n It's Choice was : ", game_dictionary_number_to_words[computer_input])
   elif computer_input == -1 and user_input == 1 : 
       print("Computer Won The game It's choice was : ", game_dictionary_number_to_words[computer_input], "\n Your Choice was : ", game_dictionary_number_to_words[user_input] )


def RockPaperScissorGame() :
   
   game_dictionary_number_to_words = {-1 : 'Rock', 0: 'Paper', 1: 'Scissor'}
   game_dictionary_word_to_numbers = { 'Rock' : -1,  'Paper' : 0,  'Scissor' : 1}
   user_input = game_dictionary_word_to_numbers[input("Choose Rock Paper or Scissor : ")]
   computer_input = random.randrange(-1 , 1)

   checkwinner(game_dictionary_number_to_words,user_input,computer_input)


