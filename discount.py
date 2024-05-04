##############################################################
## If the subtotal is $50 or greater and today is Tuesday or 
## Wednesday, your program must subtract 10% from the subtotal. 
## Your program must then compute the total amount due by adding 
## sales tax of 6% to the subtotal. Your program must print the 
## discount amount if applicable, the sales tax amount, and the 
## total amount due.
##############################################################

from datetime import datetime

current_date_and_time = datetime.now()

sub = float(input("Enter the total: "))
day = current_date_and_time.weekday()

if (day == 1):
    if(sub >= 50):
        rebate = sub - (sub * 0.10)
        tax = rebate * 0.06
        print(f"{rebate:.2f}")
        print(f"{tax:.2f}")
elif (day == 4):
    if (sub >= 50):
        discount = (sub - sub * 0.10)
        tax = discount * 0.06
    print(f"{discount:.2f}")
    print(f"{tax:.2f}")
elif (day == 4):
    if (sub < 50):
        print("No discount. You did not buiy enough.")
else:
    print("No discount.  Today is not Tuesday or Wednesday.")
