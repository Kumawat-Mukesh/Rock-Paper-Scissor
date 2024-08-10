import random

"""
Task 1 : Rock,Paper and Scissors Game
Develop a Python console-based Rock, Paper, Scissors game where players can compete against the computer. Each player selects their choice (rock, paper, or scissors), and the program determines the winner based on the classic game rules. Display the result of each round, keep track of the score, and allow players to play multiple rounds. Ensure the game handles invalid inputs and provides a user-friendly experience.

-> logic 

rock vs paper -> paper win
paper vs scissor -> rock win
scissor vs paper -> scissor win
"""


class RockPaperScissor:
    def __init__(self):
        # Initializes the attributes
        self.user_count = 0
        self.computer_count = 0
        self.draw_score = 0

    def game_rules(self):
        # print the rules of the game
        print(
            """
            Rules:
                -> This game has 5 rounds
                -> If you enter wrong choice from 1 to 3 then you are out from the game
                
                -> Winning possiblites
                    rock vs paper -> paper win
                    paper vs scissor -> rock win
                    scissor vs paper -> scissor win
            """
        )

    def get_user_choice(self):

        while True:
            try:
                # User input and convert into integer
                user_input = int(
                    input(
                        """
                        1 for Rock
                        2 for Scissor
                        3 for Paper               
                        """
                    )
                )
                # chek if the input is valid option or not
                if user_input in [1, 2, 3]:
                    return user_input
                else:
                    print("Invalid Input : Please enter a number from 1 to 3")
            except ValueError:
                print("Invalid Input : Please enter a number from 1 to 3")

    def user_input_to_string(self, user_input):
        # Convert numeric user input to its string
        user_choice = {1: "Rock", 2: "Scissor", 3: "Paper"}
        return user_choice[user_input]

    def winner(self, user_choice, computer_choice):
        # Find the winner based on the game rules
        if user_choice == computer_choice:
            return "Draw"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissor")
            or (user_choice == "Paper" and computer_choice == "Rock")
            or (user_choice == "Scissor" and computer_choice == "Paper")
        ):
            return "User"
        else:
            return "Computer"

    def play_game(self):

        # Display the game rules
        self.game_rules()

        for i in range(1, 6):
            print(f"\n Round {i}")

            # Get the user choice
            user_input = self.get_user_choice()

            # Convert user choice to string
            user_choice = self.user_input_to_string(user_input)

            # Random choice from the computer
            computer_choice = random.choice(["Rock", "Paper", "Scissor"])

            # Print the Choice
            print(f"User choice : {user_choice}")
            print(f"Computer choice : {computer_choice}")

            # Find the winner player
            winner_player = self.winner(user_choice, computer_choice)

            # Count the Score
            if winner_player == "Draw":
                self.draw_score += 1
                print("It's a draw!")
            elif winner_player == "User":
                self.user_count += 1
                print("User wins this round!")
            else:
                self.computer_count += 1
                print("Computer wins this round!")

        # Print the test results
        print("\n-----Result-----")
        if self.user_count == self.computer_count:
            print("Match Draw! Both user and computer have the same score.")
        elif self.user_count > self.computer_count:
            print("User wins the match!!")
        else:
            print("Computer wins the match!!")

        # Print the Scores
        print(f"User Score : {self.user_count}")
        print(f"Computer Score : {self.computer_count}")
        print(f"Draw Score : {self.draw_score}")


def main():
    game = RockPaperScissor()

    while True:
        try:
            # Input the choice to start the game
            user_choice = int(
                input(
                    """
            Start Game:
            Press 1 to start game 
            Press 0 to exit the game
            """
                )
            )

            if user_choice == 1:
                # If user enter 1 then game starts
                game.play_game()
            elif user_choice == 0:
                # If user choose 0 then user exit from the game
                print("You have exited the game")
                break
            else:
                print("Invalid choice. Please select 1 to start game or 0 to exit.")

        except ValueError:
            print(
                "Invalid input. Please enter a number 1 for start game or 0 for exit."
            )


if __name__ == "__main__":
    main()
