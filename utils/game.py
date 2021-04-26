import random

class Hangman():
    """
    A Hangman class.
    """
    
    def __init__(self):
        """
        The Python constructor for this class.
        """
        self.possible_words =['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = random.choice(self.possible_words).upper()
        self.lives = 5
        self.correctly_guessed_letters = "_" * len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.well_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
    

    def play(self, word_to_find):
        """
        This is the main driver of the game.
        It checks if the guessed letter is correct or not.
        """
        
        self.guessed = False
        print("####################")
        print("Welcome to Hangman!")
        print("####################")
        print("Tries: ", self.lives)
        print("\n")
        print(self.correctly_guessed_letters)
        print("\n")
        
        while (not self.guessed) and (self.lives > 0):

            self.guess = input("Please guess a letter:\n ").upper()
            
            
            if self.guess:
               
                self.turn_count += 1
                
            if len(self.guess) == 1 and self.guess.isalpha():
                if self.guess not in word_to_find:
                    print(self.guess, "is not in the word")
                    self.lives -= 1
                    self.wrongly_guessed_letters.append(self.guess)
                    self.error_count += 1
                else:
                    print("Good job, ", self.guess, "is in the word!") 
                    self.well_guessed_letters.append(self.guess) 
                    self.word_as_list = list(self.correctly_guessed_letters)
                    indices = [i for i, letter in enumerate(self.word_to_find) if letter == self.guess]

                    for i in range(len(self.word_to_find)):
                        if self.guess == self.word_to_find[i]:
                    # so_far is spliced this way:
                    # so_far [from the start : up until, but not including the
                    #     position of the correctly guessed letter]
                    # + guessed letter
                    # + so_far [from the position next to the
                    #     correctly guessed letter : to the end]
                            self.correctly_guessed_letters = self.correctly_guessed_letters[:i] + self.guess + self.correctly_guessed_letters[i+1:]
                    print(self.correctly_guessed_letters)

                    if "_" not in self.correctly_guessed_letters:
                        self.guessed = True
                        self.well_played()
                           
            else:
               print("Not a valid guess!")
            

    def start_game(self):
        
        """
        Starts the game and
        Prints the final progress of the game.
        """
        self.play(self.word_to_find)
        print("Correctly letters: ", self.correctly_guessed_letters)
        print("Wrongly letters: ", self.wrongly_guessed_letters)
        print("Tries: ", self.lives)
        print("Error: ", self.error_count)
        print("Turn: ", self.turn_count)    
        print("\n")

        if self.lives == 0:
            self.game_over()
        if self.guessed:
            self.well_played()
       

    def game_over(self):
        """
        Resets the game by condition in play method.
        """
        print("Game over!")

    def well_played(self):
        """
        Resets the game by condition in play method.
        """
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")

