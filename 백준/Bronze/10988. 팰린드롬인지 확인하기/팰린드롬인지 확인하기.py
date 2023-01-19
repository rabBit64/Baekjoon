def pelendrom(str):
  return int(str == str[::-1])
str = input()
print(pelendrom(str))