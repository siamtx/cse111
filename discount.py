##############################################################
## If the subtotal is $50 or greater and today is Tuesday or 
## Wednesday, your program must subtract 10% from the subtotal. 
## Your program must then compute the total amount due by adding 
## sales tax of 6% to the subtotal. Your program must print the 
## discount amount if applicable, the sales tax amount, and the 
## total amount due.
##############################################################

import datetime

sub = float(input("Enter the total: "))
day = datetime()

if (day == Tuesday && sub >= 50):
    sub - sub * 0.10
elif (day == Wednesday && sub >= 50):
    sub - sub * 0.10
else:
    print("No discount.  Today is not Tuesday or Wednesday.")

