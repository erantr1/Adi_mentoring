import random

categories = {"Alphabetic": ["abcba", "defgddy", "hijkl"], "Numeric": ["11223", "24124", "76809"], "Alphanumeric": ["121ab1", "556cd6", "09aa05bb"]}

while True:
  print("\n# # # # # # # # # # # # # # #")
  print("# Welcome to the Big Game!  #")
  print("# # # # # # # # # # # # # # #\n")
  print("Please select a category from the list:\n")
  for category in categories:
    print(category)
  print("")
  selected_category = input()
  print(f"\nThe selected category is: {selected_category}")
  print(f"The words in the selected category are: {categories[selected_category]}")

  rand_index = random.randrange(0, len(categories[selected_category]))
  print(f"The lucky index is: {rand_index}") # printed for control in tests
  word_to_guess = categories[selected_category][rand_index]

  word_length = len(word_to_guess)
  num_of_guesses = word_length + 2

  print("\nNow you need to guess the right word, letter by letter")
  print(f"The number of letters in the word is {word_length} and the number of guesses you have is {num_of_guesses}")

  remaining_guesses = num_of_guesses
  num_of_guessed_letters = 0
  word_in_progress = ["_" for i in range(word_length)]

  guessed_letters = []
  while remaining_guesses > 0 and num_of_guessed_letters < word_length:
    print(f"\nThe number of remaining guesses is {remaining_guesses}")
    print(f"The number of guessed letters is: {num_of_guessed_letters}")
    print(f"\nPlease enter your {'first' if remaining_guesses == num_of_guesses else 'next'} guess")
    guessed_letter = input()
    if guessed_letter in guessed_letters:
      print("This letter was already guessed, please select another letter")
      continue
    guessed_letters.append(guessed_letter)
    print(guessed_letters)

    indices_to_display = [i for i, ltr in enumerate(word_to_guess) if ltr.casefold() == guessed_letter.casefold()]
    if indices_to_display:
      num_of_guessed_letters += len(indices_to_display)
    remaining_guesses -= 1

    for index in indices_to_display:
      word_in_progress[index] = guessed_letter
    word_in_progress_string = ''.join(word_in_progress)
    print(f"You now have {word_in_progress_string}")

  if remaining_guesses == 0 and num_of_guessed_letters < word_length:
    print("\nYou lost")
  else:
    print("\nWay to go!")

  print("\nWould you like to play again? Please specify with y, yes, n or no")
  is_another_game = input()
  if is_another_game == "n" or is_another_game == "no":
    print("\nThank you for pleaying, and see you in the next match!")
    print("\n********************************************************\n")
    break