import random

def AB_first():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)

  print(quotes[rnd])
  
if __name__== "__main__":
  AB_first()
