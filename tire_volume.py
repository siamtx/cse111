# Information of the math for this assignment
# https://byui-cse.github.io/cse111-course/lesson01/approx_tire_vol.html 

import math
from datetime import datetime

z = math.pi

# Get the user input
w = float(input("Enter the width of the tire in mm (ex 205): "))
ar = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Math goes here
t = (z * w**2 * ar *(w * ar + 2540 * d))/ 10000000000

# Output the results
print(f"The approximate volume is {t:.2f} liters.")

## Get the current date and time
current_day_and_time = datetime.now()

## Isolate the date
present_date = current_day_and_time.date()

## Open text file for storage
with open("volumes.txt", mode="at") as volumes_file:
    ## print tire data to file.
    print(f"{present_date}, {w}, {ar}, {d}, {t:.2f}", file = volumes_file)

## if...elif...else for tire sizes
if (w == 205):
    if (ar == 55):
        if(d == 15):
            print("Your tire price is $121.08.")
            response = input("Would you like to purchase these tires? ")
            if (response == "yes"):
                name = input("Please enter your phone number for a follow up call. ")
                with open("volumes.txt", mode="at") as volumes_file:
                    print(f"{present_date}, {w}, {ar}, {d}, {t:.2f}, {name}", file = volumes_file)
elif (w == 215):
        if (ar == 55):
            if(d == 16):
                print("Your tire price is $186.99.")
                response = input("Would you like to purchase these tires? ")
                if (response == "yes"):
                    name = input("Please enter your phone number for a follow up call. ")
                    with open("volumes.txt", mode="at") as volumes_file:
                        print(f"{present_date}, {w}, {ar}, {d}, {t:.2f}, {name}", file = volumes_file)
elif (w == 215):
        if (ar == 65):
            if(d == 16):
                print("Your tire price is $170.99.")
                response = input("Would you like to purchase these tires? ")
                if (response == "yes"):
                    name = input("Please enter your phone number for a follow up call. ")
                    with open("volumes.txt", mode="at") as volumes_file:
                        print(f"{present_date}, {w}, {ar}, {d}, {t:.2f}, {name}", file = volumes_file)
elif (w == 225):
        if (ar == 55):
            if(d == 17):
                print("Your tire price is $214.89.")
                response = input("Would you like to purchase these tires? ")
                if (response == "yes"):
                    name = input("Please enter your phone number for a follow up call. ")
                    with open("volumes.txt", mode="at") as volumes_file:
                        print(f"{present_date}, {w}, {ar}, {d}, {t:.2f}, {name}", file = volumes_file)
else: print("We do not have your tire size.")


