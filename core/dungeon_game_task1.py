import random
# from functools import reduce
from typing import Tuple
from config import (
    configure_logging,log_messages
)
from core import (
    clear_screen,
    show_help,
    check_move
)

MOVE = ('up', 'down', 'right', 'left')
EXIT_COMMAND = ("quit", "q", "ex", "exit")
LOG_FILE = "dungeon.log"

class BoxGame:
    def __init__(self) -> None:
        """
        Initialize the BoxGame object.
        """
        self.rows = 5
        self.cols = 5
        self.box = [["_" for _ in range(self.cols)] for _ in range(self.rows)]
        self.black_hole_row, self.black_hole_col = self.generate_random_location()
        self.dragon_row, self.dragon_col = self.generate_random_location()
        self.player_row, self.player_col = self.generate_random_location()

        while self.is_invalid_starting_position():
            self.black_hole_row, self.black_hole_col = self.generate_random_location()
            self.dragon_row, self.dragon_col = self.generate_random_location()
            self.player_row, self.player_col = self.generate_random_location()

        self.update_box()

    def generate_random_location(self) -> Tuple[int, int]:
        """
        Generate a random location on the grid.

        Returns:
            Tuple[int, int]: Random row and column values.
        """
        return random.randint(0, 4), random.randint(0, 4)

    def is_invalid_starting_position(self) -> bool:
        """
        Check if the starting positions of the player, dragon, and black hole are invalid.

        Returns:
            bool: True if the starting positions are invalid, False otherwise.
        """
        return (self.dragon_row == self.black_hole_row == self.player_row and
                self.dragon_col == self.black_hole_col == self.player_col)

    def handle_movement(self, movement: str) -> bool:
        """
        Handle the movement entered by the player.

        Args:
            movement (str): The movement entered by the player.

        Returns:
            bool: True if the game should exit, False otherwise.
        """
        if movement in MOVE:
            new_player_row, new_player_col = self.player_row, self.player_col

            if movement == "up" and self.player_row > 0:
                new_player_row -= 1
            elif movement == "down" and self.player_row < 4:
                new_player_row += 1
            elif movement == "right" and self.player_col < 4:
                new_player_col += 1
            elif movement == "left" and self.player_col > 0:
                new_player_col -= 1

            if check_move(new_player_row, new_player_col):
                self.box[self.player_row][self.player_col] = '-'
                self.player_row, self.player_col = new_player_row, new_player_col
                self.box[self.player_row][self.player_col] = 'x'
                self.update_box()
            else:
                raise ValueError("Invalid move. Try again.")

            if (self.player_row, self.player_col) == (self.black_hole_row, self.black_hole_col):
                print("YOU WON 🍻")
                self.log_result("You won")
                return True
            elif (self.player_row, self.player_col) == (self.dragon_row, self.dragon_col):
                print("SORRY YOU LOSE💔")
                self.log_result("You lost")
                return True
        elif movement == "help":
            print(show_help())
        elif movement in EXIT_COMMAND:
            return True
        else:
            raise ValueError("Please enter your movement correctly "
                             "(if you don't know, you can see the possible movements by entering 'help')")

        return False

    def play_game(self) -> None:
        """
        Start the game and handle player input.
        """
        while True:
            # clear_screen()
            print(f"You are in room: {self.player_row}, {self.player_col}")
            movement = input("Enter your movement: ")
            movement = movement.lower()
            
            try:
                valid_movements = list(filter(lambda m: m in MOVE or m in EXIT_COMMAND or m == "help", [movement]))
                if valid_movements:
                    print(valid_movements)
                    should_exit = self.handle_movement(valid_movements[0])
                    if should_exit:
                        break
                else:
                    raise ValueError("Invalid movement. Try again.")
            except ValueError as value_error:
                print(f"ValueError: {str(value_error)}")

    def update_box(self) -> None:
        """
        Update and display the game box.
        """
        for row in self.box:
            print(" ".join(row))

    def log_result(self, result: str) -> None:
        """
        Log the game result.

        Args:
            result (str): The game result to be logged.
        """
        try:
            with open(LOG_FILE, "a") as file:
                file.write(result + "\n")
        except Exception as error:
            print(f"An error occurred while logging the result: {str(error)}")
