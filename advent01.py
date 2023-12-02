def first_digit(s):
   # go forward thru the string, return the first digit char
   n = 0
   while True:
      if "0" <= s[n:n+1] <= "9":
         return int(s[n:n+1])
      n += 1

def last_digit(s):
   # go backward thru string, return the last digit char
   n = len(s) - 1
   while True:
      if "0" <= s[n:n+1] <= "9":
         return int(s[n:n+1])
      n -= 1

def get_all_numbers(s):
   # go fwd thru substrings, return list of all digits in words or chars
   result = []
   n = 0
   while n < len(s):
      if "0" <= s[n:n+1] <= "9":
         result.append(int(s[n:n+1]))
      elif s[n:n+3] == "one":
         result.append(1)
      elif s[n:n+3] == "two":
         result.append(2)
      elif s[n:n+5] == "three":
         result.append(3)
      elif s[n:n+4] == "four":
         result.append(4)
      elif s[n:n+4] == "five":
         result.append(5)
      elif s[n:n+3] == "six":
         result.append(6)
      elif s[n:n+5] == "seven":
         result.append(7)
      elif s[n:n+5] == "eight":
         result.append(8)
      elif s[n:n+4] == "nine":
         result.append(9)
      n += 1
   return result

file = open('advent02.txt', 'r')
for n in range(100):
   s = file.readline()
   if n < 9:
      print(s[9:])
   elif n == 100:
      print(s[11:])
   else:
      print(s[10:])
file.close()
