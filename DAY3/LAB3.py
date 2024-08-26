# # q1

# import random

# def hangman():
#     words = ['hangman', 'python', 'javascript', 'iti', 'django']
#     word = random.choice(words)
#     guessed_letters = set()
#     attempts = 7
    
#     user_name = input("Please enter your name: ")
#     print(f"Hello, {user_name}")
#     print(f"The word that was picked is: {'_ ' * len(word)}")
    
#     while attempts > 0:
#         guess = input("Guess a letter: ").lower()

#         if len(guess) == 1 and guess.isalpha():
#             if guess in word:
#                 guessed_letters.add(guess)
#                 current_progress = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
#                 print(f"Nice That was in the word: {current_progress}")
#             else:
#                 attempts -= 1
#                 current_progress = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
#                 print(f"No, that isn't in the word: {current_progress}")
#                 print(f"You have {attempts} attempts left.")
#         else:
#             print("Invalid. Please enter a single letter.")

#         if all(letter in guessed_letters for letter in word):
#             print(f"Congratulations {user_name} you guessed the word '{word}' ")
#             break

#     if attempts == 0:
#         print(f"Sorry {user_name} you've run out of attempts The word was '{word}'.")

# if __name__ == "__main__":
#     hangman()


# ===============================================================================================================================

# q2 


# import csv
# import sys
# import random

# N = 1000

# def main():
#     if len(sys.argv) != 2:
#         sys.exit("Usage: python LAB3.py FILENAME")

#     teams = load_teams(sys.argv[1])
#     counts = simulate_tournaments(teams, N)
#     print_results(counts)

# def load_teams(filename):
#     teams = []
#     with open(filename, "r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             row["rating"] = int(row["rating"])
#             teams.append(row)
#     return teams

# def simulate_tournaments(teams, n):
#     counts = {}
#     for _ in range(n):
#         winner = simulate_tournament(teams)
#         if winner in counts:
#             counts[winner] += 1
#         else:
#             counts[winner] = 1
#     return counts

# def simulate_game(team1, team2):
#     rating1 = team1["rating"]
#     rating2 = team2["rating"]
#     probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
#     return random.random() < probability

# def simulate_round(teams):
#     winners = []
#     for i in range(0, len(teams), 2):
#         if simulate_game(teams[i], teams[i + 1]):
#             winners.append(teams[i])
#         else:
#             winners.append(teams[i + 1])
#     return winners

# def simulate_tournament(teams):
#     while len(teams) > 1:
#         teams = simulate_round(teams)
#     return teams[0]["team"]

# def print_results(counts):
#     for team, wins in sorted(counts.items(), key=lambda item: item[1], reverse=True):
#         print(f"{team}: {wins} tournaments won")

# if __name__ == "__main__":
#     main()
