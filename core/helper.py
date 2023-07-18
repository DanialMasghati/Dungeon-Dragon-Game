import os

def clear_screen():
    return os.system('cls' if os.name == 'nt' else 'clear')


def show_help():
    help_comment = """
    You can use these commands to move in the box:
    ❌ 'up', 'down', 'right', 'left' ❌

    You can use these commands to quit the game:
    ❌ 'quit', 'q', 'ex', 'exit' ❌
    """
    return help_comment


def check_move(player_row, player_col):
    return 0 <= player_row < 8 and 0 <= player_col < 8


def update_box(box, player_row, player_col):
    for row in box:
        print(" ".join(row))



