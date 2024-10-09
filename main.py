# Write your code here
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


#checks if there are doubles and returns highest doubles
def find_all_doubles_in_set(hand_to_find_doubles):
    index = 0
    highest = 0
    for i in range(len(hand_to_find_doubles)):
        if hand_to_find_doubles[i][0] == hand_to_find_doubles[i][1] and hand_to_find_doubles[i][0] > highest:
            highest = hand_to_find_doubles[i][0]
            index = i
    return highest, index


starting_tool = create_starting_set()
players_set = starting_tool[0]
computers_set = starting_tool[1]
stock = starting_tool[2]
players_doubles = find_all_doubles_in_set(players_set)
computers_doubles = find_all_doubles_in_set(computers_set)


if players_doubles[0] > computers_doubles[0]:
    print('Stock pieces: ', stock)
    print('Computer pieces: ', computers_set)
    players_set.pop(players_doubles[1])
    print('Player pieces: ', players_set)
    print('Domino snake: [[{}, {}]]'.format(players_doubles[0], players_doubles[0]))
    print('Status: computer')
if computers_doubles[0] > players_doubles[0]:
    print('Stock pieces: ', stock)
    computers_set.pop(computers_doubles[1])
    print('Computer pieces: ', computers_set)
    print('Player pieces: ', players_set)
    print('Domino snake: [[{}, {}]]'.format(computers_doubles[0], computers_doubles[0]))
    print('Status: player')
