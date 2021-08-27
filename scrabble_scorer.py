#scrabble_scorer.py

OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

SIMPLE_POINT_STRUCTURE = {
  1: ['A', 'D', 'G', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T', 'U', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z'],
}

VOWEL_BONUS_STRUCTURE = {
    1: ['D', 'G','L', 'N', 'R', 'S', 'T', 'U', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z'],
    3: ['A', 'E', "I", 'O', 'U']
}


def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in OLD_POINT_STRUCTURE:

            if char in OLD_POINT_STRUCTURE[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")
   
   scrabble_word = input("Enter your word: ")

   return scrabble_word

def simple_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in SIMPLE_POINT_STRUCTURE:

            if char in SIMPLE_POINT_STRUCTURE[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

def vowel_bonus_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in VOWEL_BONUS_STRUCTURE:

            if char in VOWEL_BONUS_STRUCTURE[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints
     
simple_scorer_dict = {
    'name': 'Simple',
    'description': 'Each letter is worth 1 point',
    'score function': simple_scorer
}     

vowel_bonus_scorer_dict = {
    'name': 'Vowel Bonus',
    'description': 'Each vowel is worth 3 points while constenants are worth 1 point',
    'score function': vowel_bonus_scorer
    
}

old_scrabble_scorer_dict = {
    'name': 'Old Scrabbe Score',
    'Description': 'Words are scored using the original Scrabble rules',
    'score function': old_scrabble_scorer
}

scoring_algorithms = ( old_scrabble_scorer_dict, simple_scorer_dict, vowel_bonus_scorer_dict
)

def scorer_prompt():
    score_prompt = "Which Scrabble scoring rules would you like to use?"
    user_selection = 3

    while user_selection > 2:
         for index, scorer in enumerate(scoring_algorithms):
             print(f'{index} - {scorer["name"]}: {scorer["description"]}')

    user_selection = int(input('Enter a 1, 2, or 3:'))

    selected_score_algorithm_dict = scoring_algorithms[user_selection]

    return selected_score_algorithm_dict

def transform():
    return

def run_program():
    word = initial_prompt()
   
    selected_score_algorithm_dict = scorer_prompt()

    score = selected_score_algorithm_dict['score_function'](word)

    print(
        f'''
        The word you entered was "{word}".
        You selected the "{selected_score_algorithm_dict['name']}" scoring algorithm which {selected_score_algorithm_dict['description']}.
        Your score is {score}!'''
    )

run_program()