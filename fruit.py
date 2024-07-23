# New OOP small program

def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # Reverse and print the list.
    fruit_list.reverse()
    print(f"reversed:{fruit_list}")

    # Append orange to the list and print.
    fruit_list.append("orange")
    print(f"orange appended: {fruit_list}")

    # Find the index for apple.
    # Insert "cherry" before apple.
    # Print the list.
    i = fruit_list.index("apple")
    #fruit_list[i - 1] = "cherry"
    fruit_list.insert(i, "cherry")
    print(f"added cherry: {fruit_list}")

    # Remove banana and print the list.
    fruit_list.remove("banana")
    print(f"Banana removed: {fruit_list}")

    # Pop last element from list.
    # Print element and list.
    print(f"Popped element:", fruit_list.pop())
    print(f"Last element popped: {fruit_list}")

    # Sort and print list.
    fruit_list.sort()
    print(f"Sorted list: {fruit_list}")

    # Clear and print list.
    fruit_list.clear()
    print(f"Cleared list: {fruit_list}")



# If this file was executed like this:
# > python accidents.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()