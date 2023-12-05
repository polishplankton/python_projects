CARD_COUNT = 211

total = 0 #used for both parts 1 & 2
wins = [] #filled in part 1, used in part 2

file = open('advent04.txt', 'r')
for p in range(CARD_COUNT):
   s = file.readline()

   #put the winning numbers in a list
   winners = [int(s[n:n+2]) for n in range(10, 38, 3)]

   #count the matching numbers
   my_picks = [int(s[n:n+2]) for n in range(42, 115, 3)]
   win_count = len(set(winners) & set(my_picks))

   wins.append([1, win_count]) #these are used in part 2
   total += int(2**(win_count-1))
file.close()

print("part 1 answer: " + str(total))

total = 0
for n in range(CARD_COUNT):
   for x in range(wins[n][1]):
      wins[n+x+1][0] += wins[n][0]
   total += wins[n][0]

print("part 2 answer: " + str(total))
