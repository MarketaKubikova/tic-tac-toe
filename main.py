from random import choice


def get_grid(space):
    return "     |     |     \n"\
           + "  " + space[7] + "  |  " + space[8] + "  |  " + space[9] + "  \n" \
                                                                  "_____|_____|_____\n" \
                                                                  "     |     |     \n"\
           + "  " + space[4] + "  |  " + space[5] + "  |  " + space[6] + "  \n" \
                                                                  "_____|_____|_____\n" \
                                                                  "     |     |     \n"\
           + "  " + space[1] + "  |  " + space[2] + "  |  " + space[3] + "  \n" \
                                                                  "     |     |     \n"


def get_turn(last_turn):
    if last_turn != "":
        if last_turn == "player":
            return "computer"
        else:
            return "player"
    else:
        return choice(["player", "computer"])


def get_copy(space):
    copy = []
    for i in space:
        copy.append(i)
    return copy


def is_space_free(grid, space):
    return grid[space] == " "


def is_win(space, mark):
    return (
            (space[1] == mark and space[2] == mark and space[3] == mark) or
            (space[4] == mark and space[5] == mark and space[6] == mark) or
            (space[7] == mark and space[8] == mark and space[9] == mark) or
            (space[1] == mark and space[4] == mark and space[7] == mark) or
            (space[2] == mark and space[5] == mark and space[8] == mark) or
            (space[3] == mark and space[6] == mark and space[9] == mark) or
            (space[1] == mark and space[5] == mark and space[9] == mark) or
            (space[3] == mark and space[5] == mark and space[7] == mark)
    )


def is_grid_full(space):
    for i in range(1, 10):
        if is_space_free(space, i):
            return False
    print("It's tie!")
    return True


def make_move(grid, mark, cell):
    grid[cell] = mark


def get_computer_move(space, computer_mark, player_mark):
    # decision maker
    # if computer can win in next move, win
    for i in range(1, 10):
        copy = get_copy(space)
        if is_space_free(copy, i):
            copy[i] = computer_mark
            if is_win(copy, computer_mark):
                return i

    # if player can win in next move, block him
    for i in range(1, 10):
        copy = get_copy(space)
        if is_space_free(copy, i):
            copy[i] = player_mark
            if is_win(copy, player_mark):
                return i

    # if center is free, take it
    if is_space_free(space, 5):
        return 5

    # if any corner is free, take one
    possible_moves = []
    for i in [1, 3, 7, 9]:
        if is_space_free(space, i):
            possible_moves.append(i)
    if len(possible_moves) > 0:
        return choice(possible_moves)

    # otherwise, taky any free side
    else:
        for i in [2, 4, 6, 8]:
            if is_space_free(space, i):
                possible_moves.append(i)
        return choice(possible_moves)


def play_again():
    user_response = input("Wanna play again? Y/N\n").lower()
    if user_response == "y":
        space = [" "] * 10
        is_over = False
    else:
        space = None
        is_over = True
    return space, is_over


def gameplay():
    print("******************************\n"
          "*** Welcome to Tic Tac Toe ***\n"
          "******************************\n")

    player_mark = input("First, choose your sign, X or O?\n").capitalize()
    if player_mark == "X":
        computer_mark = "0"
    else:
        computer_mark = "X"
    print("You play for {}".format(player_mark))

    space = [" "] * 10
    is_over = False
    last_turn = ""

    while not is_over:
        turn = get_turn(last_turn)

        if turn == "player":
            player_move = int(input("Take your move, 1-9\n"))
            if is_space_free(space, player_move):
                make_move(space, player_mark, player_move)
            else:
                while not is_space_free(space, player_move):
                    player_move = int(input("This cell is already taken, choose any else\n"))
                make_move(space, player_mark, player_move)
            last_turn = "player"
            print(get_grid(space))
            if is_win(space, player_mark):
                print("You won. Congratulations!")
                is_over = True
        else:
            make_move(space, computer_mark, get_computer_move(space, computer_mark, player_mark))
            last_turn = "computer"
            print(get_grid(space))
            if is_win(space, computer_mark):
                print("Computer won. You lose!")
                is_over = True

        if is_over or is_grid_full(space):
            space, is_over = play_again()


gameplay()
