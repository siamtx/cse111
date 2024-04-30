##  A manufacturing company needs a program that will help 
##  its employees pack manufactured items into boxes for shipping.


import math
# Get User input
items = int(input("Enter the number of manufactured items: "))
itemsBox = int(input("How many items will be packed in each box: "))

# Calculate number of boxes needed.
box = math.ceil(items / itemsBox)

print(f"For {items} items, packing {itemsBox}"
      f" items in each box, you will need {box} boxes.")