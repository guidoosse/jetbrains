global vals
vals = list('         ')
grid = {0: '1 1', 1: '1 2', 2: '1 3', 3: '2 1', 4: '2 2', 5: '2 3', 6: '3 1', 7: '3 2', 8: '3 3'}
key_list = list(grid.keys())
val_list = list(grid.values())

def update_grid(newvals):
    global vals
    vals[0] = newvals[0]
    vals[1] = newvals[1]
    vals[2] = newvals[2]
    vals[3] = newvals[3]
    vals[4] = newvals[4]
    vals[5] = newvals[5]
    vals[6] = newvals[6]
    vals[7] = newvals[7]
    vals[8] = newvals[8]


def print_grid(newvals=''):
    global vals
    vals[0] = newvals[0]
    vals[1] = newvals[1]
    vals[2] = newvals[2]
    vals[3] = newvals[3]
    vals[4] = newvals[4]
    vals[5] = newvals[5]
    vals[6] = newvals[6]
    vals[7] = newvals[7]
    vals[8] = newvals[8]

    print("---------")
    print('|', vals[0], vals[1], vals[2], '|')
    print('|', vals[3], vals[4], vals[5], '|')
    print('|', vals[6], vals[7], vals[8], '|')
    print("---------")


def analyse_grid(vals):

    result = ''
    if (vals[0] == vals[3] and vals[3] == vals[6]) and (vals[1] == vals[4] and vals[4] == vals[7]):
        result = 'Impossible'


    elif (vals[0] == vals[4] and vals[4] == vals[8]) or (vals[0] == vals[3] and vals[3] == vals[6]) or (
            vals[0] == vals[1] and vals[1] == vals[2]):
        if ' wins' in result:
            result = 'Impossible'
        else:
            if vals[0] in 'XO':
                result = vals[0] + ' wins'

    elif (vals[1] == vals[4] and vals[4] == vals[7]):
        if 'wins' in result:
            result = 'Impossible'
        else:
            if vals[1] in 'XO':
                result = vals[1] + ' wins'

    elif (vals[2] == vals[5] and vals[5] == vals[8]) or (vals[2] == vals[4] and vals[4] == vals[6]):
        if 'wins' in result:
            result = 'Impossible'
        else:
            if vals[2] in 'XO':
                result = vals[2] + ' wins'

    elif (vals[3] == vals[4] and vals[4] == vals[5]):
        if 'wins' in result:
            result = 'Impossible'
        else:
            if vals[3] in 'XO':
                result = vals[3] + ' wins'


    elif (vals[6] == vals[7] and vals[7] == vals[8]):
        if 'wins' in result:
            result = 'Impossible'
        else:
            if vals[6] in 'XO':
                result = vals[6] + ' wins'


    elif vals.count('_') == 0 and result == '':
        result = 'Draw'


    elif vals.count('X') - vals.count('O') < 0 or vals.count('O') - vals.count('X') < 0:
        result = 'Impossible'


    elif vals.count('_') > 1:
        result = 'Game not finished'

    return result


def play_grid(val, pos):
        vals[pos] = val
        print_grid(vals)


def check_ingrid(coords_input):
    x , y = coords_input.split(' ')
    if 0 < int(y) < 4 or 0 < int(x) < 4:
        returner = 1
    else:
        print("Coordinates should be from 1 to 3!")
        returner = 0
    return returner


def get_move():
    ok = 0
    while ok < 1:
        try:
            coords = str(input('Enter the coordinates:'))
            if check_ingrid(coords):
                da_pos = val_list.index(coords)
                if vals[da_pos] == 'X' or vals[da_pos] == 'O':
                    print('This cell is occupied! Choose another one!')
                    ok = 0
                else:
                    try:
                        my_pos = val_list.index(coords)
                        ok = 1

                    except ValueError:
                        print('Coordinates should be from 1 to 3!')
                        ok = 0

        except ValueError:
            print('you should enter numbers!')
    return coords

#values = str(input('Enter cells:'))
print_grid(vals)


while True:
    cord = get_move()
    my_pos = val_list.index(cord)

    play_grid('X', int(my_pos))
    result = analyse_grid(vals)
    if "wins" in result or "Draw" in result:
        print(result)
        exit()






#print_grid(vals)
# print(my_val)


# /print(analyse_grid(values))
