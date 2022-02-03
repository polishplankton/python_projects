import sys

def valid_roll(roll):
    ''' Make sure argument is a valid yahtzee roll (e.g. 42521) '''
    
    Values = ('1', '2', '3', '4', '5', '6')

    if len(roll) != 5:
        return False

    # check for invalid characters
    for n in range(5):
        if roll[n:n+1] not in Values:
            return False
        
    return True

def padl(input):
    return ("               " + input)[-16:]

def padn(input):
    return ("  " + str(input))[-2:]

def show_roll_values(roll_string):
    categories = ('ones', 'twos', 'threes', 'fours', 'fives', 'sixes', 'three of a kind', 'four of a kind', \
                  'full house', 'small straight', 'large straight', 'chance', 'yahtzee')    
    roll_numbers = []
    for n in range(5):
        roll_numbers.append(int(roll_string[n:n+1]))
    roll_numbers.sort()
    score_list = [0] * 13

    # populate top row values (ones, twos,... sixes)
    for n in range(6):
        score_list[n] = roll_numbers.count(n+1) * (n+1)

    print(roll_numbers[2], roll_numbers[4])
    # three of a kind
    if roll_numbers[0] == roll_numbers[2] or \
       roll_numbers[1] == roll_numbers[3] or \
       roll_numbers[2] == roll_numbers[4]:
        for n in range(5):
            score_list[6] += roll_numbers[n]

    # four of a kind
    if roll_numbers[0] == roll_numbers[3] or roll_numbers[1] == roll_numbers[4]:
        for n in range(5):
            score_list[7] += roll_numbers[n]

    # full house
    if (roll_numbers[0] == roll_numbers[2] and roll_numbers[3] == roll_numbers[4]) or \
       (roll_numbers[0] == roll_numbers[1] and roll_numbers[2] == roll_numbers[4]):
        score_list[8] = 25

    # small straight
    if (roll_numbers[0] + 1 == roll_numbers[1] and roll_numbers[1] + 1 == roll_numbers[2] and roll_numbers[2] + 1 == roll_numbers[3]) or \
       (roll_numbers[1] + 1 == roll_numbers[2] and roll_numbers[2] + 1 == roll_numbers[3] and roll_numbers[3] + 1 == roll_numbers[4]):
        score_list[9] = 30

    # large straight
    if roll_numbers[0] + 1 == roll_numbers[1] and \
       roll_numbers[1] + 1 == roll_numbers[2] and \
       roll_numbers[2] + 1 == roll_numbers[3] and \
       roll_numbers[3] + 1 == roll_numbers[4]:
        score_list[10] = 40

    # chance
    for n in range(5):
        score_list[11] += roll_numbers[n]

    # yahtzee
    if roll_numbers[0] == roll_numbers[4]:
        score_list[12] = 50

    for n in range(13):
        print(padl(categories[n]), end = ' ')
        print(padn(score_list[n]))

if len(sys.argv) != 2:
    print("Incorrect number of arguments")
elif not valid_roll(sys.argv[1]):
    print('Invalid roll')
else:
    show_roll_values(sys.argv[1])
