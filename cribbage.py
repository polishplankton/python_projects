import itertools

def valid_hand(hand):
    ''' Make sure argument is in value-suit-value-suit... format '''
    
    Values = ('1', '2', '3', '4', '5', '6', '7',
              '8', '9', 'T', 'J', 'Q', 'K')
    Suits = ('S', 'C', 'H', 'D')

    if len(hand) != 10:
        return False

    # check for invalid values or suits
    for n in (0, 2, 4, 6, 8):
        if hand[n:n+1] not in Values:
            return False
        if hand[n+1:n+2] not in Suits:
            return False
        
    # check for duplicate cards
    for m in range(4):
        for n in range(m+1, 5):
            if hand[2*m:2*m+2] == hand[2*n:2*n+2]:
                return False
            
    return True

def point_count(hand):
    '''return to point value of a cribbage hand'''
    
    hand = hand.upper()
    hand = hand.replace('A', '1')
    
    if not valid_hand(hand):
        print("Hand input not recognized")
        return None
    
    total_points = 0
    
    # count combinations that sum to 15
    value_list = []
    for n in [0, 2, 4, 6, 8]:
        if hand[n:n+1].isalpha():
            value_list.append(10)
        else:
            value_list.append(int(hand[n:n+1]))
    for n in [2, 3, 4, 5]:
        a = itertools.combinations(value_list, n)
        for combo in list(a):
            if sum(combo) == 15:
                total_points += 2

    # count runs
    run_count = [0, 0, 0] #refers to runs of 3, 4, & 5 respectively
    card_list = []
    for n in [0, 2, 4, 6, 8]:
        card_list.append(hand[n:n+1])
    card_list.sort()
    
    # count runs of 3
    a = itertools.combinations(card_list, 3)
    for combo in list(a):
        if combo in [('1', '2', '3'), ('2', '3', '4'), ('3', '4', '5'),
                     ('4', '5', '6'), ('5', '6', '7'), ('6', '7', '8'),
                     ('7', '8', '9'), ('8', '9', 'T'), ('9', 'J', 'T'),
                     ('J', 'Q', 'T'), ('J', 'K', 'Q')]:
            run_count[0] += 1

    # count runs of 4
    a = itertools.combinations(card_list, 4)
    for combo in list(a):
        if combo in [('1', '2', '3', '4'), ('2', '3', '4', '5'),
                     ('3', '4', '5', '6'), ('4', '5', '6', '7'),
                     ('5', '6', '7', '8'), ('6', '7', '8', '9'),
                     ('7', '8', '9', 'T'), ('8', '9', 'J', 'T'),
                     ('9', 'J', 'T', 'Q'), ('J', 'K', 'Q', 'T')]:
            run_count[1] += 1

    # count runs of 5
    a = itertools.combinations(card_list, 5)
    for combo in list(a):
        if combo in [('1', '2', '3', '4', '5'), ('2', '3', '4', '5', '6'),
                     ('3', '4', '5', '6', '7'), ('4', '5', '6', '7', '8'),
                     ('5', '6', '7', '8', '9'), ('6', '7', '8', '9', 'T'),
                     ('7', '8', '9', 'J', 'T'), ('8', '9', 'J', 'T', 'Q'),
                     ('9', 'J', 'K', 'T', 'Q')]:
            run_count[2] += 1
            
    if run_count[2] > 0:
        total_points += 5
    elif run_count[1] > 0:
        total_points += 4*run_count[1]
    elif run_count[0] > 0:
        total_points += 3*run_count[0]
    
    # count pairs
    a = itertools.combinations(card_list, 2)
    for combo in list(a):
        if combo[0] == combo[1]:
            total_points += 2
    
    # count flushes
    if hand[3] == hand[5] and hand[5] == hand[7] and hand[7] == hand[9]:
        total_points += 4
        if hand[1] == hand[3]:
            total_points += 1
            
    # count "right jack"
    for n in range(2,10,2):
        if hand[n] == 'J' and hand[1] == hand[n+1]:
            total_points += 1
    
    return total_points
    
print(point_count('5hjh5d5c5s'))
