import random


#creates set of dominoe pieces with unique combinations only, [1,2] and [2,1] are the same domino
def form_full_set_of_pieces():
    stock_pieces = []
    for i in range(7):
        for j in range(7):
            piece = []
            piece.append(i)
            piece.append(j)
            reverse = piece[::-1]
            if reverse not in stock_pieces:
                stock_pieces.append(piece)
    random.shuffle(stock_pieces)
    return stock_pieces


#calls two functions and generates full set, players set, computers set and stock
def create_starting_set():
    full_set = form_full_set_of_pieces()
    players_set = full_set[0:7]
    computers_set = full_set[7:14]
    stock = full_set[14:]
    return players_set, computers_set, stock


#checks if there are doubles and returns highest double (only one of the pair and the index where it is located in set
def find_all_doubles_in_set(hand_to_find_doubles):
    index = 0
    highest = 0
    for i in range(len(hand_to_find_doubles)):
        if hand_to_find_doubles[i][0] == hand_to_find_doubles[i][1] and hand_to_find_doubles[i][0] > highest:
            highest = hand_to_find_doubles[i][0]
            index = i
    return highest, index


#forms a print statement
def print_result(stock, computers_set, players_set, snake):
    print('='*70)
    print('Stock size:', len(stock))
    print('Computer pieces:', len(computers_set))
    print()
    if len(snake) <= 6:
        print(*snake)
    else:
        print(snake[0], snake[1], snake[2], "...", snake[-3], snake[-2], snake[-1])
    print()
    print('Your pieces:')
    for i in range(len(players_set)):
        print('{}:{}'.format(i+1, players_set[i]))
    print()


def determine_first_move(players_set, players_doubles, computers_set, computers_doubles, snake):
    if players_doubles[0] > computers_doubles[0]:
        the_index = players_doubles[1]
        the_piece = players_set[the_index]
        players_set.pop(the_index)
        snake.append(the_piece)
        return 'player', snake, the_index
    if computers_doubles[0] > players_doubles[0]:
        the_index = computers_doubles[1]
        the_piece = computers_set[the_index]
        snake.append(the_piece)
        computers_set.pop(the_index)
        return 'computer', snake, the_index


def make_move(the_set, stock, snake, move):
    if len(move) == 0:
        snake.append(the_set[0])
        the_set.pop(0)
    else:
        try:
            int(move)
        except ValueError:
            print("Invalid input. Please try again.")
            move = input()
        if abs(int(move)) > len(the_set):
            move = input()
        if len(move) == 0:
            snake.append(the_set[0])
            the_set.pop(0)
        if int(move) == 0:
            the_set.append(stock[0])
            stock.pop(0)
            return the_set
        if int(move) > 0:
            snake.append(the_set[int(move) - 1])
        elif int(move) < 0:
            snake.insert(0, the_set[abs(int(move)) - 1])
        the_set.pop(abs(int(move)) - 1)


starting_tool = create_starting_set()
players_set = starting_tool[0]
computers_set = starting_tool[1]
stock = starting_tool[2]
players_doubles = find_all_doubles_in_set(players_set)
computers_doubles = find_all_doubles_in_set(computers_set)
snake = []
first_move = determine_first_move(players_set, players_doubles, computers_set, computers_doubles, snake)
starting_player = first_move[0]
starting_index = first_move[2]

if starting_player == 'computer':
    count = 1
elif starting_player == 'player':
    count = 0
while len(players_set) != 0 or len(computers_set) != 0:
    if count % 2 == 0:
        print_result(stock, computers_set, players_set, snake)
        print("Status: Computer is about to make a move. Press Enter to continue...")
        move = input()
        make_move(computers_set, stock, snake, move)
        count += 1
        if len(computers_set) == 0:
            print_result(stock, computers_set, players_set, snake)
            print("Status: The game is over. The computer won!")
            break
    if count % 2 != 0:
        print_result(stock, computers_set, players_set, snake)
        print("Status: It's your turn to make a move. Enter your command.")
        move = input()
        make_move(players_set, stock, snake, move)
        count += 1
        if len(players_set) == 0:
            print_result(stock, computers_set, players_set, snake)
            print("Status: The game is over. You won!")
            break
