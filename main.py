from core.dungeon_game_task2 import BoxGame


def main() -> None:
    """
    The main function to start the game.
    """
    try:
        game = BoxGame()
        game.play_game()
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    main()
