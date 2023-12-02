def str2rgb(s):
   "convert strings into lists of color counts"
   r, g, b = 0, 0, 0
   if "red" in s:
      r = int(s[s.index("red")-3:s.index("red")])
   if "green" in s:
      g = int(s[s.index("green")-3:s.index("green")])
   if "blue" in s:
      b = int(s[s.index("blue")-3:s.index("blue")])
   return [r, g, b]

# use file to populate list of strings
data = []
file = open('advent02.txt', 'r')
for n in range(100): #we know we have one hundred lines
   s = file.readline()
   data.append(s.split(";"))
file.close()

# use the list above to convert strings to sets
# of integers and calculate the required totals
sum = power_sum = 0
for n in range(100):
   r = g = b = 0
   for mylist in data[n]:
      rgb = str2rgb(mylist)
      r = max(r, rgb[0])
      g = max(g, rgb[1])
      b = max(b, rgb[2])
   if r <= 12 and g <= 13 and b <= 14:
      sum += n + 1
   power_sum += r * g * b
print("answer to part 1 = " + str(sum))
print("answer to part 2 = " + str(power_sum))
