'''
CS 5001
Fall 2019
Homework #7
'''
from room import *

MAX_WEIGHT = 10

def read_txt(file_name):
    '''
    Name: read_txt
    Input: string, name of the file
    Output: nothing
    Does: read data from txt document and store it in a list
    '''
    try:
        infile = open(file_name, 'r')
        lst = [line.split('|') for line in infile.read().splitlines()]
    except OSError:
        print('Could not open the file.')
    finally:
        infile.close()
        
    return lst[1::]

def item_list(items_data):
    '''
    Name: item_list
    Input: a list
    Output: list of class
    Does: read data from items_data and make it a list of class item
    '''
    lst = []
    for i in range(len(items_data)):
        item = Item(*items_data[i])
        lst.append(item)
    return lst

def puz_monster_list(puz_monster_data):
    '''
    Name: puz_monster_list
    Input: a list
    Output: list of class
    Does: read data from puz_monster_data and make it a list of class puz and
    monster
    '''
    lst = []
    for i in range(len(puz_monster_data)):
        if i <= 1:
            pu_monster = Monster(puz_monster_data[i][0], puz_monster_data[i][1],
                                 puz_monster_data[i][5], puz_monster_data[i][2],
                                 puz_monster_data[i][3], puz_monster_data[i][4],
                                 puz_monster_data[i][6], puz_monster_data[i][7],
                                 puz_monster_data[i][8])
        else:
            pu_monster = Puzzle(puz_monster_data[i][0], puz_monster_data[i][1],
                                puz_monster_data[i][5], puz_monster_data[i][2],
                                puz_monster_data[i][3], puz_monster_data[i][4],
                                puz_monster_data[i][6])
            
        if 'Room' in pu_monster.target:
            element = pu_monster.target.split()
            pu_monster.target = element[1]

        lst.append(pu_monster)
    return lst

def room_list(rooms_data):
    '''
    Name: room_list
    Input: a list
    Output: list of class
    Does: read data from rooms_data and make it a list of class room
    '''
    lst = []
    for i in range(len(rooms_data)):
        adjacent_room = rooms_data[i][3].split(' ')
        for num in range(len((adjacent_room))):
            adjacent_room[num] = int(adjacent_room[num])
        room = Room(rooms_data[i][0], rooms_data[i][1], rooms_data[i][2],
                    adjacent_room)

        room.items = rooms_data[i][6].split(',')
        if room.items != ['None']:
            for i in range(len(room.items)):
                room.items[i] = room.items[i].upper()
        room.picture = rooms_data[i][7]
        
        lst.append(room)
        
    return lst
def adjust_roomlist(puz_monster_class, rooms_class):
    '''
    Name: adjust_roomlist
    Input: two list of class
    Output: list of class
    Does: put relative puzzles and monsters into rooms
    '''
    for i in range(len(puz_monster_class)):
        for num in range(len(rooms_class)):
            if puz_monster_class[i].target == rooms_class[num].number:
                rooms_class[num].puzzles = puz_monster_class[i].name
    return rooms_class

def menu(answer):
    '''
    Name: menu
    Input: a string
    Returns: A string, which is users choice if it's in D, W, P, or Q. if not,
    they will have to chooce agian.
    '''
    answer = answer.upper()
    if answer in 'NSEWITDULQ' and len(answer) == 1:
            return answer
    else:
            print('Invalid. Please choose again.\n')
            return 'invalid'
        
def move(adjecent_room, choose, current_room):
    '''
    Name: move
    Input: adjecent_room, a list of direction; choose, a string of players choice;
    current_room, an int of the current room players are in.
    Returns: an int, if they can go to the room. Otherwise, it will return
    current_room, which plays will stay and cannot move to other rooms.
    Does: to change current location or stay
    '''
    if choose == 'N':
        index = 0
    elif choose == 'S':
        index = 1
    elif choose == 'E':
        index = 2
    elif choose == 'W':
        index = 3
        
    if adjecent_room[index] > 0:
        return adjecent_room[index] - 1
    
    elif adjecent_room[index] == 0:
        print('\n--->>There is no way to go!<<---...\n')
        return current_room
    else:
        print('\n--->>Something block the way<<---...\n')
        return current_room
def check_weight(weight, weight_dic, pick):
    '''
    Name: check_weight
    Input: a int, weight; a dictionary, weight_dic; a string, pick
    Output: Boolean
    Does: check if the weight can be handled.
    '''
    if (weight + weight_dic[pick]) <= MAX_WEIGHT:
        return True
    else:
        return False

def look(looking_stuff, items_class):
    '''
    Name: look
    Input: looking_stuff, a string of item players want to look. items_class,
    a list of class items.
    Returns: None
    Does: to print the description of the item players looking for
    '''
    for i in items_class:
        if looking_stuff == i.name.upper():
            print('You examine the ', looking_stuff, ':')
            print(i.description)
            print('=============================\n')
def check_item(inventory):
    '''
    Name: check_item
    Input: None
    Returns: None
    Does: print items the play is carrying.
    '''
    print('You are carrying: ')
    for i in inventory:
        print(i)
    
def game(filename_items, filename_rooms, filename_puzzles):
    '''
    Name: game
    Input: 3 strings, which are the file name of 3 data txt documents.
    Returns: None
    Does: the core function of this game.
    '''
    # initialize current_room for the location and weight for invenotry weight
    current_room = 0
    weight = 0
    inventory = []
    
    # read data from those txt documents
    items_data = read_txt(filename_items)
    rooms_data = read_txt(filename_rooms)
    puz_monster_data = read_txt(filename_puzzles)
    
    # initialize these three classes
    raw_rooms_class = room_list(rooms_data)
    items_class = item_list(items_data)
    puz_monster_class = puz_monster_list(puz_monster_data)
    room_class = adjust_roomlist(puz_monster_class, raw_rooms_class)

    # create some dictionaries to store names and relative data for future use
    weight_dic = {}
    for i in items_class:
        weight_dic[i.name.upper()] = int(i.weight)
        
    value_dic = {}
    for i in items_class:
        value_dic[i.name.upper()] = int(i.value)

    attack_dic = {}
    count = 0
    for i in puz_monster_class:
        if count <= 1:
            attack_dic[i.name] = i.effect, i.attack
            count += 1
        else:
            attack_dic[i.name] = i.effect

    solve_dic = {}
    for i in puz_monster_class:
        solve_dic[i.name] = i.solution.upper()

    while True:
        # print current location every round
        print('You are now in the :', room_class[current_room].name)
        # if there is no puzzles in this room, print room description
        if len(room_class[current_room].puzzles) == 0:
            print(room_class[current_room].description)
            
        else:
            # only monsters' len is 2; one is effect another one is attack
            # print them separately
            if len(attack_dic[room_class[current_room].puzzles]) == 2:
                for n in attack_dic[room_class[current_room].puzzles]:
                    print(n)
            else:
                print(attack_dic[room_class[current_room].puzzles])
        # if this room has any item, print them out
        if room_class[current_room].items != ['None']:
            for i in room_class[current_room].items:
                print('A', i, 'is here in the room')
        print('=' * 30)
        
        answer = input('Enter N, S, E or W to move in those directions.\n'
                       'I for Inventory, L to look at something, U to Use'
                       ' <an item>\n'
                       'T to Take an item, D to Drop an item\n'
                       'or Q to Quit and exit the game\n'
                       'Your choice: ')
        # evaluate users input
        choose = menu(answer)

        # users use to move
        if choose in 'NSEW':
            current_room = move(room_class[current_room].adjacent_rooms,
                                choose, current_room)

        # choose to look items in inventory
        elif choose == 'I':
            check_item(inventory)
            print('\n')
            
        # choose to take item
        elif choose == 'T':
            if weight <= MAX_WEIGHT:
                pick = input('Take what item? ').upper()
                # if the item in current room
                if pick in room_class[current_room].items:
                    # if the user can handle the weight, take it up
                    if check_weight(weight, weight_dic, pick):
                        inventory.append(pick)
                        weight += weight_dic[pick]
                        room_class[current_room].del_item(pick)
                        print(pick, 'added to your inventory\n')
                    else:
                        print('Carrying too much weight. Cannot add', pick)
                else:
                    print('Cannot take this item.\n')
            else:
                print('Your bag is full.\n')

        # choose to look the function of an item
        elif choose == 'L':
            looking_stuff = input('Examine (look) at what? ').upper()
            # if the item in the room or in inventory, print the description
            if looking_stuff in room_class[current_room].items or\
               looking_stuff in inventory:
                look(looking_stuff, items_class)
            else:
                print('Cannot examine (look) at the item.')

        # choose to use an item      
        elif choose == 'U':
            use = input('Use what item? ').upper()
            # check the item is in inventory and it can work to the puzzles
            if use in inventory and\
               room_class[current_room].puzzles != [] and\
               solve_dic[room_class[current_room].puzzles] == use:
                for i in items_class:
                    # find the item in class
                    if use == i.name.upper():
                        # check the item still has use_remaining
                        if i.use():
                            # if it the item works, clean the path and puzzles
                            for n in range(4):
                                room_class[current_room].adjacent_rooms[n]\
                                = abs(room_class[current_room].adjacent_rooms[n]) 
                            print('Success! You used the', use, 'on the',\
                                  room_class[current_room].puzzles, '\n')
                            room_class[current_room].puzzles = []
                            
            else:
                print('You swing the', use, 'but it has no effect')
        # choose to drop. if the item in current inventory, remove the item, minus
        # its weight and add it into the current room item
        elif choose == 'D':
            drop_stuff = input('Drop what item? ').upper()
            if drop_stuff in inventory:
                inventory.remove(drop_stuff)
                weight -= weight_dic[drop_stuff]
                room_class[current_room].add_item(drop_stuff)
                print('A', drop_stuff, 'is dropped in',
                      room_class[current_room].name)

        # choose to quit, computer their score and end game       
        elif choose == 'Q':
            score = 0
            for i in inventory:
                score += value_dic[i]
            print('Your score is: ', score)
            if score >= 1000:
                print('Your rating is: a seasoned pathfinder.')
            else:
                print('Your rating is: an average pathfinder.')
            print('Goodbye!')
            break

        # users don't have vaild choose, start again
        else:
            pass
