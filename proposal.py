
# Random is needed for the project.
import random

# This password generator will randomly 
# generate a password each time it is run.
# There will 12 characters randomly generated
# from the ASCII chart to include special
# characters, upper and lower case letters.

def main():
  
  # Create a temporary list to store random values
  # for the password string.

  string = " "

  pass_random()
  shuffle(pass_random)
  #pass_display(pass_random)


def pass_random():
  p_word = []
  for i in range(12):
    letter = chr(random.randint(48, 122))
    p_word.append(letter)

  print(p_word) 


def shuffle(pass_random):
  tempList = list(pass_random)
  random.shuffle(tempList)
  print("".join(tempList))

  

def pass_display(shuffle):
  print(f"{"".join(templist)}") 


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()

  