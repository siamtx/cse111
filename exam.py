# python
# Your Name: Timothy W. Howell
# Date: 20 July 2024
# Purpose of the Assignment: This program is a password 
# generator.  It provides two passwords.
# Sources Used: https://www.101computing.net/random-password-generator/
# https://www.shiksha.com/online-courses/articles/ord-and-chr-functions-in-python/
# https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python
# https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
#######################################################################################


# Random is used to generate characters for the password.
import random

# This password generator will randomly generate a password 
# each time it is run. There will be 12 characters randomly 
# generated from the ASCII chart to include special 
# characters, upper and lower case letters.  It will also 
# shuffle the base password for an even more random pawword.

def main():
  
  # Call the character generation functions.

    on = twh_one()
    tw = twh_two()
    th = twh_three()
    fo = twh_four()
    fi = twh_five()
    si = twh_six()
    se = twh_seven()
    ei = twh_eight()
    ni = twh_nine()
    te = twh_ten()
    el = twh_eleven()
    tl = twh_twelve()


    # Concatenates the function output into a string.
    password = on + tw + th + fo + fi + si + se + ei + ni + te + el + tl
    
    # Prints password string.
    print(f"This is the orignal password: {password} \n")

    # Calls the shuffle function.
    twh_shuffle(password)



# Generate a random character between 48 and 122
# of the ASCII table.
def twh_one():
  letter = chr(random.randint(48, 122))
  return letter

# Generate a random character between 48 and 122
# of the ASCII table.
def twh_two():
  letter = chr(random.randint(48, 122))
  return letter

# Generate a random character between 48 and 122
# of the ASCII table.
def twh_three():
  letter = chr(random.randint(48, 122))
  return letter

# Generate a random character between 48 and 122
# of the ASCII table.
def twh_four():
  letter = chr(random.randint(48, 122))
  return letter

# Generate a random character between 48 and 122
# of the ASCII table.
def twh_five():
  letter = chr(random.randint(48, 122))
  return letter

# Generate a random character between 48 and 122
# of the ASCII table.
def twh_six():
  letter = chr(random.randint(48, 122))
  return letter

# Generate a random character between 48 and 122
# of the ASCII table.
def twh_seven():
  letter = chr(random.randint(48, 122))
  return letter

# Generate a random character between 48 and 122
# of the ASCII table.
def twh_eight():
  letter = chr(random.randint(48, 122))
  return letter

# Generate a random character between 48 and 122
# of the ASCII table.
def twh_nine():
  letter = chr(random.randint(48, 122))
  return letter

# Generate a random character between 48 and 122
# of the ASCII table.
def twh_ten():
  letter = chr(random.randint(48, 122))
  return letter

# Generate a random character between 48 and 122
# of the ASCII table.
def twh_eleven():
  letter = chr(random.randint(48, 122))
  return letter

# Generate a random character between 48 and 122
# of the ASCII table.
def twh_twelve():
  letter = chr(random.randint(48, 122))
  return letter

# Shuffles the characters of password for a more 
# random string of characters. Prints a string not 
# a list.
def twh_shuffle(password):
  tempList = list(password)
  random.shuffle(tempList)
  print(f"This the shuffled password: {''.join(tempList)} \n") 



# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()