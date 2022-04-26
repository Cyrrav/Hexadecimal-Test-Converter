# Welcome print statements:
print("Enter X at any time to quit the program")
print("This program will convert an input integer into hexadecimal for you")

# Ask for, and store user's input
inp = input("Enter an integer: ")

# While they keep inputting integers:
while inp != "X":
    if inp.isdigit():           # If they had a valid integer input:
        integer = int(inp)      # Convert the string into an integer, and
        print(hex(integer))     # print the hex version thanks to a neat function! :)
    else:                       # If they had invalid input,
        print("Invalid input")  # let them know and print it out.
    
    # After a valid or invalid input, ask for another integer and repeat!
    inp = input("Enter an integer: ")