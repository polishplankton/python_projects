# I will assign each hand a strength index
# it will be the type from 0 to 6
# type*13^5 + 1st_card*13^4 + 2nd_card*13^3 + 3rd_card*13^2 + 4th_card*13^1 + 5th_card*13^0

def card_value(c):
   if c >= '2' and c <= '9':
      return int(c) - 2
   elif c == 'T':
      return 8
   elif c == 'J':
      return 9
   elif c == 'Q':
      return 10
   elif c == 'K':
      return 11
   else:
      return 12

def value(s):
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
   result += 13**4 * card_value(s[0])
   result += 13**3 * card_value(s[1])
   result += 13**2 * card_value(s[2])
   result += 13**1 * card_value(s[3])
   result += 13**0 * card_value(s[4])
   return result

hands = []

f = open("advent07.txt", "r")
while True:
   s = f.readline()
   if len(s) == 0:
      break
   hands.append(s.split())
f.close()

for hand in hands:
   hand.append(value(hand[0]))

hands.sort(key=lambda x: x[2])

rank = 1
sum = 0
for hand in hands:
   sum += int(hand[1]) * rank
   rank += 1
print(sum)
