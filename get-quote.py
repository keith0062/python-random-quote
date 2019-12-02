import random

def initial():
  #print("Keep it logically awesome.")

  with open("quotes.txt") as f:
    quotes = f.readlines()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(quotes[rnd].strip())

if __name__== "__main__":
  initial()
