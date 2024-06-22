import csv

def main():

    # Call the read_dictionary function from the
    # variable products_dict.
    products_dict = read_dictionary

    # Print products_dict and add a blank line.
    print(products_dict, "\n")

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
            print(row_list)

            # If the current row is not blank, add the 
            # data from the current to teh dictionary.
         #   if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
        #        key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
         #       dictionary[key] = row_list







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
