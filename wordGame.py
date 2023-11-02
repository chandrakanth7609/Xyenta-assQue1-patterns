"""
    2. Write a program two players words are scored based on there
    points, and the number of points is the sum of the point values
    of each letter in the word.
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    1 3 3 2 1 4 2 4 1 8 5 1 3 1 1 3 10 1 1 1 1 4 4 8 4 10
    For example, if we wanted to score the word Code, we would
    note that in general rules above, the C is worth 3 points,
    the o is worth 1 point, the d is worth 2 points, and the e is
    worth 1 point. Summing these, we get that Code is worth 3 + 1
    + 2 + 1 = 7 points.
    Following are the examples.
    a. Player 1: Question?
    Player 2: Question!
    Tie!
    b. Player 1: Oh,
    Player 2: Hai!
    Player 2 wins!
"""

def calculate_word_score(word):
    score = 0
    for letter in word:
        letter = letter.upper()  
        if letter in letter_scores:
            score += letter_scores[letter]
    return score

letter_scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

# inputs
player1_word = input("Enter the player1_word:")
player2_word = input("Enter the player2_word:")

# calling calculate_word_score function
score_of_player1 = calculate_word_score(player1_word)
score_of_player2 = calculate_word_score(player2_word)

# scores
print("Score of player1_word is = ",score_of_player1)
print("Score of player2_word is = ",score_of_player2) 

 # results
if score_of_player1 > score_of_player2:
    print("Player 1 wins!")
elif score_of_player1 < score_of_player2:
    print("Player 2 wins!")
else:
    print("It's a tie!")