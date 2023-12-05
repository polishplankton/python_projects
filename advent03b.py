def is_gear_near_number(gear, number):
   result = False
   for row in range(number[1]-1, number[1]+2):
      for col in range(number[2]-1, number[2]+1+len(str(number[0]))):
         if gear[0] == row and gear[1] == col:
            result = True
   return result

# read the data into a list, & surround it with
# periods so we don't run into boundary errors
data = ["." * 142]
file = open('advent03.txt', 'r')
while True:
   s = file.readline()
   if len(s) == 0:
      break
   data.append("." + s.replace("\n", "") + ".")
file.close()
data.append("." * 142)

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

gear_locations = []
for s in range(1, 141):
   for n in range(1, len(data[s])):
      if data[s][n:n+1] == "*":
         gear_locations.append([s, n])

number_locations = []
for s in range(1, 141):
   for n in range(1, len(data[s])-1):
      if data[s][n-1:n] not in digits and data[s][n:n+1] in digits and data[s][n+1:n+2] in digits and data[s][n+2:n+3] in digits:
         number_locations.append([int(data[s][n:n+3]), s, n])
      elif data[s][n-1:n] not in digits and data[s][n:n+1] in digits and data[s][n+1:n+2] in digits:
         number_locations.append([int(data[s][n:n+2]), s, n])
      elif data[s][n-1:n] not in digits and data[s][n:n+1] in digits:
         number_locations.append([int(data[s][n:n+1]), s, n])

sum = 0 
for gear in gear_locations:
   zam = []
   for number in number_locations:
      if is_gear_near_number(gear, number):
         zam.append(number[0])
   if len(zam) == 2:
      sum += zam[0] * zam[1]
print(sum)