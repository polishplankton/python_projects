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

#create a distinct list of symbols
symbols = []
for s in data:
   for n in range(len(s)):
      if s[n:n+1] not in symbols:
         symbols.append(s[n:n+1])
symbols.remove(".")
#for n in range(10):
for n in range(10):
   symbols.remove(str(n))

sum = 0
for s in range(1, 141):
   for n in range(1, len(data[s])-1):
      if data[s][n-1:n] not in digits and data[s][n:n+1] in digits and data[s][n+1:n+2] in digits and data[s][n+2:n+3] in digits:
         if data[s-1][n-1:n] in symbols or data[s-1][n:n+1] in symbols or data[s-1][n+1:n+2] in symbols or data[s-1][n+2:n+3] in symbols or data[s-1][n+3:n+4] in symbols or \
            data[s][n-1:n] in symbols or data[s][n+3:n+4] in symbols or \
            data[s+1][n-1:n] in symbols or data[s+1][n:n+1] in symbols or data[s+1][n+1:n+2] in symbols or data[s+1][n+2:n+3] in symbols or data[s+1][n+3:n+4] in symbols:
            sum += int(data[s][n:n+3])
      elif data[s][n-1:n] not in digits and data[s][n:n+1] in digits and data[s][n+1:n+2] in digits:
         if data[s-1][n-1:n] in symbols or data[s-1][n:n+1] in symbols or data[s-1][n+1:n+2] in symbols or data[s-1][n+2:n+3] in symbols or \
            data[s][n-1:n] in symbols or data[s][n+2:n+3] in symbols or \
            data[s+1][n-1:n] in symbols or data[s+1][n:n+1] in symbols or data[s+1][n+1:n+2] in symbols or data[s+1][n+2:n+3] in symbols:
            sum += int(data[s][n:n+2])
      elif data[s][n-1:n] not in digits and data[s][n:n+1] in digits:
         if data[s-1][n-1:n] in symbols or data[s-1][n:n+1] in symbols or data[s-1][n+1:n+2] in symbols or \
            data[s][n-1:n] in symbols or data[s][n+1:n+2] in symbols or \
            data[s+1][n-1:n] in symbols or data[s+1][n:n+1] in symbols or data[s+1][n+1:n+2] in symbols:
            sum += int(data[s][n:n+1])
print(sum)