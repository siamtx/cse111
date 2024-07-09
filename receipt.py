import csv
from datetime import datetime

def main():
    # Index of the product number column
    # in the products.csv file.
    PRODUCT_ID_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2

    # Index of items in request.csv
    PRODUCT_NUM = 0
    QUANTITY = 1

    # Call the read_dictionary function from the
    # variable products_dict.
    products_dict = read_dictionary("products.csv", PRODUCT_ID_INDEX)

    # Print products_dict and add a blank line.
    print(f"All Products \n {products_dict} \n")

    print(f"Inkom Emporium \n")
    
    total = 0
    items = 0
    tax = 0

    # Create an empty list that will
    # store th data from teh CSV file.
    compound_list = []

    try:
    
        # Open the request.csv file for reading
        with open("request.csv", "rt") as request_file:

            # Use the csv module to create a reader object 
            # that will read from the opened CSV file.
            reader = csv.reader(request_file) 

            # The first row of the CSV file contains column
            # headings and not data, so this statement skips
            # the first row of the CSV file.
            next(reader)

            # Read the rows in teh CSV file one row at a time.
            # The reader object returns each row as a list.
            for row_list in reader:

                # If the current row is not blank, add the 
                # data from the current to teh dictionary.
                if len(row_list) != 0:

                    # Append one row from the CSV
                    # file to the compound list.
                    compound_list.append(row_list)

                    # For each item in the list add the number
                    # of credits that the student has earned.
                    for request_key in compound_list:
                        # Get the list information for the 
                        # request list.
                        product_key = request_key[PRODUCT_NUM]
                        product_list = products_dict[product_key]
                        product_name = product_list[NAME_INDEX]
                        product_price = product_list[PRICE_INDEX]
                        amount = request_key[QUANTITY]

                        # Count the number of items in receipt
                        items += int(QUANTITY)
                        

            #    subtotal =0
            #    subtotal = (float(items) * float(product_price))

                # Compute Sales Tax
                # 6% for tax rate
            #    tax = (subtotal * .06)


            #    total = (subtotal + tax)
                    
                print(f"{product_name}: {amount} @ {product_price}")

        subtotal =0
        subtotal = (float(items) * float(product_price))

                # Compute Sales Tax
                # 6% for tax rate
        tax = (subtotal * .06)


        total = (subtotal + tax)

    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file {filename} doesn't exist.")
        print("Please check the name of the file " \
                "and try again.")
        
    except KeyError as key_err:
        # Code that the computer executes if the code in the
        # try block caused a function to raise a KeyError.    
        print(type(key_err).__name__, key_err, sep=": ")
        print(f"unknown product_id in the request.csv file {product_key}")

    except Exception as excep:
        # This code will be executed if some
        # other type of exception occurs.
        print()
        print(type(excep).__name__, excep, sep=": ")


    print()
    print(f"Number of Items: {items}")
    # print the sub total
    print(f'Subtotal: {subtotal}')
    print(f"Sales Tax: {tax:.2f}")
    print(f"Total: {total:.2f} \n")
    print("Thank you for shopping at the Inkom Emporium.")


    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    # Use an f-string to print the current
    # day of the week and the current time.
    print(f"{current_date_and_time:%A %I:%M %p}")



def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and returnt eh dictionary
    
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: teh index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dicionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading an store a reference
    # to the opened file in a varable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object 
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file) 

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in teh CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the 
            # data from the current to teh dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

    # Return the dictionary.
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()
