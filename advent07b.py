# I will assign each hand a strength index
# it will be the type from 0 to 6
# type*13^5 + 1st_card*13^4 + 2nd_card*13^3 + 3rd_card*13^2 + 4th_card*13^1 + 5th_card*13^0

#this method differs in parts 1 & 2
def card_value(c):
   if c >= '2' and c <= '9':
      result = int(c) - 1
   elif c == 'T':
      result = 9
   elif c == 'J':
      result =  0
   elif c == 'Q':
      result = 10
   elif c == 'K':
      result = 11
   else:
      result = 12
   return result

def value(s, o):
   # find the type
   # first order the hand
   sorted_s = ''.join(sorted(s))
   if sorted_s[0] == sorted_s[4]:
      type = 6 #five of a kind
   elif sorted_s[0] == sorted_s[3] or sorted_s[1] == sorted_s[4]:
      type = 5 #four of a kind
   elif (sorted_s[0] == sorted_s[2] and sorted_s[3] == sorted_s[4]) or \
        (sorted_s[0] == sorted_s[1] and sorted_s[2] == sorted_s[4]):
      type = 4 #full house
   elif sorted_s[0] == sorted_s[2] or sorted_s[1] == sorted_s[3] or \
        sorted_s[2] == sorted_s[4]:
      type = 3 #three of a kind
   elif (sorted_s[0] == sorted_s[1] and sorted_s[2] == sorted_s[3]) or \
        (sorted_s[0] == sorted_s[1] and sorted_s[3] == sorted_s[4]) or \
        (sorted_s[1] == sorted_s[2] and sorted_s[3] == sorted_s[4]):
      type = 2 #two pair
   elif sorted_s[0] == sorted_s[1] or sorted_s[1] == sorted_s[2] or \
        sorted_s[2] == sorted_s[3] or sorted_s[3] == sorted_s[4]:
      type = 1 #one pair
   else:
      type = 0
   result = 13**5 * type
   result += 13**4 * card_value(o[0])
   result += 13**3 * card_value(o[1])
   result += 13**2 * card_value(o[2])
   result += 13**1 * card_value(o[3])
   result += 13**0 * card_value(o[4])
   return result

def max_value(s):
   maxvalue = 0
   for joker in ('2','3','4','5','6','7','8','9','T','Q','K','A'):
      maxvalue = max(maxvalue, value(s.replace('J', joker), s))
   return maxvalue

#initiate list
hands = []

#populate list
f = open("advent07.txt", "r")
while True:
   s = f.readline()
   if len(s) == 0:
      break
   hands.append(s.split())
f.close()

#add a value to each hand in the list
for hand in hands:
   hand.append(max_value(hand[0]))

#sort on the value
hands.sort(key=lambda x: x[2])

#calculate the answer
rank = 1
sum = 0
for hand in hands:
   sum += int(hand[1]) * rank
   rank += 1
print(sum)
