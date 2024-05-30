"""
I feel that I am a person of worth, at least on an equal plane with others.
I feel that I have a number of good qualities.
All in all, I am inclined to feel that I am a failure.
I am able to do things as well as most other people.
I feel I do not have much to be proud of.
I take a positive attitude toward myself.
On the whole, I am satisfied with myself.
I wish I could have more respect for myself.
I certainly feel useless at times.
At times I think I am no good at all.

Notice that five of the statements (numbers 1, 2, 4, 6, 7) are positive and are scored like this:

Choice	Points
Strongly Disagree	0
Disagree	1
Agree	2
Strongly Agree	3
The other five statements (numbers 3, 5, 8, 9, 10) are negative and are scored like this:

Choice	Points
Strongly Disagree	3
Disagree	2
Agree	1
Strongly Agree	0

As a team, write a Python program named esteem.py that implements the Rosenberg self-esteem scale. Your program must ask the user to respond to each of the ten statements with D, d, a, or A which mean strongly disagree, disagree, agree, and strongly agree. Your program must compute the score for each answer and sum and display the person’s total score. You should think about how you will separate this program into functions before you begin writing the program.

Core Requirements
Your program prints the introductory text as shown in the Testing Procedure section below.
Your program prints each of the ten statements and gets a response from the user.
Your program computes the score for each response and sums all the scores and displays the total score.
negative:                   Positive:
if (ans == "D"):          if (ans == "D"):
    points = 3              points = 0
elif (ans == "d"):        elif (ans == "d"):
    points = 2              points = 1
elif (ans == "a"):        elif (ans == "a"): 
    points = 1              points = 2
else:                     else:
    points = 0              points = 3

"""
def main():
    stuff = intro()
    one = ques1()
    two = ques2()
    three = ques3()
    four = ques4()
    five = ques5()
    six = ques6()
    seven = ques7()
    eight = ques8()
    nine = ques9()
    ten = ques10()
    total = score(one, two, three, four, five, six,
          seven, eight, nine, ten)
    display = results(total)

def intro():
    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")


def ques1():
    print()
    print("1. I feel that I am a person of worth, at least on an \
equal plane with others.")
    ans = input("Enter: D, d, a, or A: ")
    if (ans == "D"):
        points = 0
    elif (ans == "d"):
        points = 1
    elif (ans == "a"):
        points = 2
    else:
        points = 3
    
    return points
    
def ques2():
    print("2. I feel that I have a number of good qualities.")
    ans = input("Enter: D, d, a, or A: ")
    if (ans == "D"):
        points = 0
    elif (ans == "d"):
        points = 1
    elif (ans == "a"):
        points = 2
    else:
        points = 3
    
    return points

def ques3():
    print("3. All in all, I am inclined to feel that I am a failure.")
    ans = input("Enter: D, d, a, or A: ")
    if (ans == "D"):
        points = 3
    elif (ans == "d"):
        points = 2
    elif (ans == "a"):
        points = 1
    else:
        points = 0
    
    return points

def ques4():
    print("4. I am able to do things as well as most other people.")
    ans = input("Enter: D, d, a, or A: ")
    if (ans == "D"):
        points = 0
    elif (ans == "d"):
        points = 1
    elif (ans == "a"):
        points = 2
    else:
        points = 3
    
    return points

def ques5():
    print("5. I feel I do not have much to be proud of.")
    ans = input("Enter: D, d, a, or A: ")
    if (ans == "D"):
        points = 3
    elif (ans == "d"):
        points = 2
    elif (ans == "a"):
        points = 1
    else:
        points = 0
    
    return points

def ques6():
    print("6. I take a positive attitude toward myself.")
    ans = input("Enter: D, d, a, or A: ")
    if (ans == "D"):
        points = 0
    elif (ans == "d"):
        points = 1
    elif (ans == "a"):
        points = 2
    else:
        points = 3
    
    return points

def ques7():
    print("7. On the whole, I am satisfied with myself.")
    ans = input("Enter: D, d, a, or A: ")
    if (ans == "D"):
        points = 0
    elif (ans == "d"):
        points = 1
    elif (ans == "a"):
        points = 2
    else:
        points = 3
    
    return points

def ques8():
    print("8. I wish I could have more respect for myself.")
    ans = input("Enter: D, d, a, or A: ")
    if (ans == "D"):
        points = 3
    elif (ans == "d"):
        points = 2
    elif (ans == "a"):
        points = 1
    else:
        points = 0
    
    return points

def ques9():
    print("9. I certainly feel useless at times.")
    ans = input("Enter: D, d, a, or A: ")
    if (ans == "D"):
        points = 3
    elif (ans == "d"):
        points = 2
    elif (ans == "a"):
        points = 1
    else:
        points = 0
    
    return points

def ques10():
    print("10. At times I think I am no good at all.")
    ans = input("Enter: D, d, a, or A: ")
    if (ans == "D"):
        points = 3
    elif (ans == "d"):
        points = 2
    elif (ans == "a"):
        points = 1
    else:
        points = 0
    
    return points

def score(one, two, three, four, five, six,
          seven, eight, nine, ten):
    
    total = (one + two + three + four + five +
        six + seven + eight + nine + ten)
    
    return total
def results(total):
    print(f"Your score is {total}.")
    print("A score below 15 may indicate problematic low self-esteem.")

main()