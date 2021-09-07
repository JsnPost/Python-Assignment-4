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

VOWEL_BONUS = {
    # 1: ['D', 'G','L', 'N', 'R', 'S', 'T', 'U', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z'],
    3: ['A', 'E', "I", 'O', 'U']
}


def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = 0

    for char in word:

        for point_value in OLD_POINT_STRUCTURE:

            if char in OLD_POINT_STRUCTURE[point_value]:
                letterPoints += point_value

    return letterPoints

def simple_scorer(word):
    word = word.upper()
    letterPoints = 0

    for char in word:

        for point_value in SIMPLE_POINT_STRUCTURE:

            if char in SIMPLE_POINT_STRUCTURE[point_value]:
                letterPoints += point_value

    return letterPoints

def vowel_bonus_scorer(word):
    word = word.upper()
    vowels = "AEIOU"
    letterPoints = 0

    for char in word:

        if char in vowels:
            letterPoints += 3
        else:
            letterPoints += 1

    #      for point_value in VOWEL_BONUS:
    #          if char in VOWEL_BONUS[point_value]:
    #             letterPoints += point_value
                
    return letterPoints
        

def scrabble_scorer(word):
    score = 0

    for letter in word:
        if letter in new_point_structure:
            score += new_point_structure[letter]

    return score

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")
   
   scrabble_word = input("Enter your word: ")

   return scrabble_word  


def transform(provided_dict):
    new_dict = {}

    for (key, value) in provided_dict.items():
        for letter in value:
                new_dict[letter.lower()] = key
    
    return new_dict

new_point_structure = transform(OLD_POINT_STRUCTURE)

simple_scorer_dict = {
    "name": "Simple",
    "description": "Each letter is worth 1 point",
    "score_function": simple_scorer
}     

vowel_bonus_scorer_dict = {
    "name": "Vowel Bonus",
    "description": "Each vowel is worth 3 points while constenants are worth 1 point",
    "score_function": vowel_bonus_scorer
    
}

old_scrabble_scorer_dict = {
    "name": "Old Scrabbe Scorer",
    "description": "Words are scored using the original Scrabble rules",
    "score_function": scrabble_scorer
}

scoring_algorithms = ( old_scrabble_scorer_dict, simple_scorer_dict, vowel_bonus_scorer_dict
)

def scorer_prompt():
    score_prompt = "Which Scrabble scoring rules would you like to use?"
    user_selection = 3

    while user_selection > 2:
        for index, algorithm in enumerate(scoring_algorithms):
            print(f'{index} - {algorithm["name"]} : {algorithm["description"]}')

        user_selection = int(input("Enter a 0, 1, or 2:"))

    selected_score_algorithm_dict = scoring_algorithms[user_selection]

    return selected_score_algorithm_dict

def run_program():
    word = initial_prompt()
   
    selected_score_algorithm_dict = scorer_prompt()

    score = selected_score_algorithm_dict["score_function"](word)

    print(f'''
The word you entered was "{word}".
You selected the "{selected_score_algorithm_dict['name']}" scoring algorithm which {selected_score_algorithm_dict['description']}.
Your score is {score}!'''
    )

