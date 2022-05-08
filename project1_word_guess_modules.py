import random
import math
import xml.etree.ElementTree as ET

def category_selection(categories_dict):
  for category in categories_dict:
    print(category)
  print("")
  selected_category = input()
  print(f"\nThe selected category is: {selected_category}")
  print(f"The words in the selected category are: {categories_dict[selected_category]}")
  return selected_category

def index_lottery(categories_dict, selected_category):
  rand_index = random.randrange(0, len(categories_dict[selected_category]))  
  print(f"The lucky index is: {rand_index}") # printed for control in tests
  return rand_index

def intro(categories_dict):
  print("\n# # # # # # # # # # # # # # #")
  print("# Welcome to the Big Game!  #")
  print("# # # # # # # # # # # # # # #\n")
  print("Please select a category from the list:\n")
  
  selected_category = category_selection(categories_dict)
  rand_index = index_lottery(categories_dict, selected_category)
  word_to_guess = categories_dict[selected_category][rand_index]

  return word_to_guess

def guess_next_letter(remaining_guesses, num_of_guessed_letters, num_of_guesses):
  print(f"\nThe number of remaining guesses is {remaining_guesses}")
  print(f"The number of guessed letters is: {num_of_guessed_letters}")
  print(f"\nPlease enter your {'first' if remaining_guesses == num_of_guesses else 'next'} guess")
  guessed_letter = input()
  return guessed_letter


def guess_cycle(num_of_guesses, word_to_guess, word_length):
    remaining_guesses = num_of_guesses
    num_of_guessed_letters = 0
    word_in_progress = ["_" for i in range(word_length)]    
    already_guessed_letters = []
    while remaining_guesses > 0 and num_of_guessed_letters < word_length:
      guessed_letter = guess_next_letter(remaining_guesses, num_of_guessed_letters, num_of_guesses)
      if guessed_letter in already_guessed_letters:
        print("This letter was already guessed, please select another letter")
        continue
      already_guessed_letters.append(guessed_letter)
      print(already_guessed_letters)

      indices_to_uncover = [i for i, ltr in enumerate(word_to_guess) if ltr.casefold() == guessed_letter.casefold()]
      if indices_to_uncover:
        num_of_guessed_letters += len(indices_to_uncover)
      remaining_guesses -= 1

      for index in indices_to_uncover:
        word_in_progress[index] = guessed_letter
      word_in_progress_string = ''.join(word_in_progress)
      print(f"Current guess: {word_in_progress_string}")

    return remaining_guesses, num_of_guessed_letters


def main():
  
  # with open('categories_dict.xml', 'r', encoding = 'utf-8') as f:
  #   categories_xml = f.read()

  tree = ET.parse('categories_xml.xml')
  root = tree.getroot()

  categories_dict = {"Animals": ["dog", "cat", "chicken"], "furniture": ["closet", "chair", "table"], "food": ["pizza", "falafel", "chocolate"]} # need to change to a function that loads from xml
  
  while True:
    # getting initial parameters
    word_to_guess = intro(categories_dict)
    word_length = len(word_to_guess)
    num_of_guesses = math.ceil(word_length*1.5)

    print("\nNow you need to guess the right word, letter by letter")
    print(f"The number of letters in the word is {word_length} and the number of guesses you have is {num_of_guesses}")
    
    remaining_guesses, num_of_guessed_letters = guess_cycle(num_of_guesses, word_to_guess, word_length)    
    if remaining_guesses == 0 and num_of_guessed_letters < word_length:
      print("\nYou lost")
    else:
      print("\nWay to go!")

    print("\nWould you like to play again? Please specify with y, yes, n or no")
    is_another_game = input()
    if is_another_game == "n" or is_another_game == "no":
      print("\nThank you for playing, and see you in the next match!")
      print("\n********************************************************\n")
      break

if __name__ == "__main__":
  main()