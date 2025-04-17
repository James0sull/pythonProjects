letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0


def score_word(word):
    return sum(letter_to_points.get(letter.upper(), 0) for letter in word)


player_to_words = {
    "Player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

player_to_points = {}

for player, words in player_to_words.items():
    player_to_points[player] = sum(score_word(word) for word in words)


def update_player_points(player, word):
    if player in player_to_points:
        player_to_points[player] += score_word(word)
    else:
        player_to_points[player] = score_word(word)


# Example usage
update_player_points('Player1', 'NEWWORD')

print("Player to Words:", player_to_words)
print("Player to Points:", player_to_points)
