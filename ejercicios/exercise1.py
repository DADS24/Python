str = "The greatest victory is that which requires no battle"

def reverse(string):
  strIntoList = string.split()
  revList = list(reversed(strIntoList))
  return revList

print(reverse(str))