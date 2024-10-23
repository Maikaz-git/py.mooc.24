# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word): return 1
        elif len(player1_word) < len(player2_word): return 2

class MostVowels(WordGame):
    def __init__(self, rounds:int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        def most_vowels(string):
            vowels = ['a','e','o','u','i']
            return sum([1 for el in string if el in vowels])

        if most_vowels(player1_word) > most_vowels(player2_word): return 1
        elif most_vowels(player1_word) < most_vowels(player2_word): return 2


class RockPaperScissors(WordGame):
    def __init__(self, rounds:int):
        super().__init__(rounds)
    
    def round_winner(self, pl1:str, pl2:str):
        gm = ['rock', 'paper', 'scissors']
        if pl1 in gm and pl2 not in gm: return 1 
        if pl2 in gm and pl1 not in gm: return 2
        if pl1 == pl2: return 0

        if pl1 == "rock" and pl2 == 'scissors' or pl1 == 'paper' and pl2 == 'scissors' or pl1 == 'scissors' and pl2 == 'paper':
            return 1
        else: 
            return 2

p = RockPaperScissors(2)
p.play()