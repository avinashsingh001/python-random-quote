import random


def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  # rmvd = quotes.remove(quotes[rnd])

  last = len(quotes) - 1
  second_rnd = random.randint(0, last)
  print(quotes[rnd], end = "")
  print(quotes[second_rnd])

if __name__== "__main__":
  primary()
