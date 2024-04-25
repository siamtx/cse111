# Information of the math for this assignment
# https://byui-cse.github.io/cse111-course/lesson01/approx_tire_vol.html 

import math

z = math.pi

# Get the user input
w = float(input("Enter the width of the tire in mm (ex 205): "))
ar = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Math goes here
t = (z * w**2 * ar *(w * ar + 2540 * d))/ 10000000000

# Output the results
print(f"The approximate volume is {t:.2f} liters.")

print(" the github has too many files in it.")


