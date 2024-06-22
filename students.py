import csv

def main():

    # Provide index of Inumber
    INUMBER_INDEX = 0
    NAME = 1

    # Read the contents of the students.csv into a
    # compound dictionary named students_dict. Use
    # the phone numbers as the keys in the dictionary.
    students_dict = read_dictionary("students.csv", INUMBER_INDEX)

    print(students_dict)
    # Add extra line for space.
    print()

    # Get an I-number from student.
    num = input("Please provide an I-Number (xxxxxxxxx): ")

    # Check if the student ID is in the dictionary.
    if num in students_dict:

        # Find the student ID in the dictionary and
        # retrieve the corresponding student name.
        NAME = students_dict[num]

        # Print the student's name.
        print(NAME)

    else:
        print("No such student")


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # Create a place holder dictionary.
    dictionary = {}

    # Open the file and read it.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
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
