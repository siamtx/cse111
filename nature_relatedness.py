"""
My ideal vacation spot would be a remote, wilderness area.
I always think about how my actions affect the environment.
My connection to nature and the environment is a part of my spirituality.
I take notice of wildlife wherever I am.
My relationship to nature is an important part of who I am.
I feel very connected to all living things and the earth.

"""
def main():
    intro()
    one = ques1()
    two = ques2()
    three = ques3()
    four = ques4()
    five = ques5()
    six = ques6()
    total = rawTotal(one, two, three, four, five, six)
    average = rawAverage(total)
    display(average)


def intro():
    print()
    print("Short Form Version of the Nature Relatedness Scale (NR-6)")
    print("Instructions: For each of the following, please rate the extent to which you agree with each")
    print("statement, using the scale from 1 to 5 as shown below. Please respond as you really")
    print("feel, rather than how you think “most people” feel.")
    print()
    print()

  
def ques1():
    print("1. My ideal vacation spot would be a remote, wilderness area.")
    ans = input("Enter: 1, 2, 3, 4, or 5: ")
    if (ans == "1"):
        points = 1
    elif (ans == "2"):
        points = 2
    elif (ans == "3"):
        points = 3
    elif (ans == "4"):
        points = 4
    else:
        points = 5
    
    return points

def ques2():
    print("2. I always think about how my actions affect the environment.")
    ans = input("Enter: 1, 2, 3, 4, or 5: ")
    if (ans == "1"):
        points = 1
    elif (ans == "2"):
        points = 2
    elif (ans == "3"):
        points = 3
    elif (ans == "4"):
        points = 4
    else:
        points = 5
    
    return points

def ques3():
    print("3. My connection to nature and the environment is a part of my spirituality.")
    ans = input("Enter: 1, 2, 3, 4, or 5: ")
    if (ans == "1"):
        points = 1
    elif (ans == "2"):
        points = 2
    elif (ans == "3"):
        points = 3
    elif (ans == "4"):
        points = 4
    else:
        points = 5
    
    return points

def ques4():
    print("4. I take notice of wildlife wherever I am.")
    ans = input("Enter: 1, 2, 3, 4, or 5: ")
    if (ans == "1"):
        points = 1
    elif (ans == "2"):
        points = 2
    elif (ans == "3"):
        points = 3
    elif (ans == "4"):
        points = 4
    else:
        points = 5
    
    return points

def ques5():
    print("5. My relationship to nature is an important part of who I am.")
    ans = input("Enter: 1, 2, 3, 4, or 5: ")
    if (ans == "1"):
        points = 1
    elif (ans == "2"):
        points = 2
    elif (ans == "3"):
        points = 3
    elif (ans == "4"):
        points = 4
    else:
        points = 5
    
    return points

def ques6():
    print("6. I feel very connected to all living things and the earth.")
    ans = input("Enter: 1, 2, 3, 4, or 5: ")
    if (ans == "1"):
        points = 1
    elif (ans == "2"):
        points = 2
    elif (ans == "3"):
        points = 3
    elif (ans == "4"):
        points = 4
    else:
        points = 5
    
    return points

def rawTotal(one, two, three, four, five, six):
    total = (one + two + three + four + five + six)
    return total

def rawAverage(total):
    average = total / 6
    return average


def display(average):
    print(f"Your score is {average:.2}.")

main()
