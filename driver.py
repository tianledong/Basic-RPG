'''
CS 5001
Fall 2019
Homework #7
'''
from game import *

def main():
    print('*' * 46)
    print('*                ALIGN QUEST                 *')
    print('*            CS5001 Final Project            *')
    print('*' * 46 + '\n')

    filename_items = 'aquest_items.txt'
    filename_rooms = 'aquest_rooms.txt'
    filename_puzzles = 'puzzles_n_monsters.txt'
    
    game(filename_items, filename_rooms, filename_puzzles)
    
main()
