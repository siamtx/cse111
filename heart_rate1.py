"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

max = 220
a = (max * 0.65) 
b = (max * 0.85)

age = input("Please enter your age: ")
print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {a:.0f} and {b:.0f} beats per minute.")
