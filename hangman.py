import random

# Create list of word the program will randomly choose from.

word_list = ['apple', 'pear', 'car', 'astronomy', 'random']

def hangman():
# Randomly choose a word
    # Generate random number between 0 and word_list's length
    ran_num = random.randrange(0, len(word_list))
    
# When the game starts, store that randomly chosen word as 'answer' variable
    answer = word_list[ran_num]
    # Create a dict with letters and their indexes in an array
    answer_map = {}
    for idx, letter in enumerate(answer):
        if letter in answer_map.keys():
            answer_map[letter].append(idx)
        else:
            answer_map[letter] = [idx]
# Track number of tries with 'remaining_tries' variable
    remaining_tries = 7
# Show the users how many letters the answer has with underscores
    user_progress = '_' * len(answer)

    # Start a loop that keeps looping until remaining_tries == 0 or all underscores are replaced.
    while remaining_tries > 0 and '_' in user_progress:
        # Ask for user input
        user_guess = input('Guess a letter: ')
        # Determine if there are any letters same as user's guess in answer_map
        if user_guess in answer_map.keys():
            # If a user gets a letter correct, replace the underscore in the same indexes as the rightfully guessed letter
            letter_indexes = answer_map[user_guess]
            # Check for all the indexes and replace underscore with guressed letter
            for index in letter_indexes:
                user_progress = user_progress[0:index] + user_guess + user_progress[index + 1:]

            print(f"Your guess was right!")
            print(f"Current progress: {user_progress}")
            print(f"Remaining tries: {remaining_tries}\n")

        # Wrong guess
        else:
            remaining_tries = remaining_tries - 1
            print(f"There is no '{user_guess}' in this word.")
            print(f"Remaining tries: {remaining_tries}\n")

    # If the user is out of tries:
    if remaining_tries == 0:
        print("You are out of tries. Better luck next time!")
        return

    # If all the letter is guessed correctly:
    if '_' not in user_progress:
        print("You guessed the right word!")
        return

    

hangman()
input('Press Enter to Exit...')