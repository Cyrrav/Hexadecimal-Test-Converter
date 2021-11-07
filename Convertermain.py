import math

#put everything in a class to keep things organised
class hexcode:

    #user input prompt
    print("Press X at any time to quit the program")
    print("This program will convert an input integer into hexadecimal for you")

    #to loop until exit key is input
    while True:

        giveoutput = True
        getinput = input("Enter an integer:\n")

        #asks for a valid input if not a positive integer
        if not getinput.isdigit():
            #exits script if "X" is input
            if getinput == "X":
                break
            print("Invalid input")
            while True:
                input("Please enter a valid input:\n")
                
        #a list containing hexadecimal components
        hexcode = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]

        #finds out how many digits the resulting hex code will have
        #and defines key variables
        userinput = int(getinput) 
        digitcount = math.ceil(math.log(userinput + 1, 16))
        firstkey = secondkey = thirdkey = fourthkey = fifthkey = sixthkey = ""

        #for each digit, finds the corresponding hexadecimal component
        #then reduces the digit count by 1 and continues on to the next digit
        if digitcount == 6:
            key = math.floor(userinput / 1048576)
            sixthkey = hexcode[key]
            userinput %= 1048576
            digitcount -= 1
        
        if digitcount == 5:
            key = math.floor(userinput / 65536)
            fifthkey = hexcode[key]
            userinput %= 65536
            digitcount -= 1
            
        if digitcount == 4:
            key = math.floor(userinput / 4096)
            fourthkey = hexcode[key]
            userinput %= 4096
            digitcount -= 1
                 
        if digitcount == 3:
            key = math.floor(userinput / 256)
            thirdkey = hexcode[key]
            userinput %= 256
            digitcount -= 1
    
        if digitcount == 2:
            key = math.floor(userinput / 16)
            secondkey = hexcode[key]
            userinput %= 16
            digitcount -= 1
                        
        if digitcount == 1:
            key = math.floor(userinput / 1)
            firstkey = hexcode[key]
            digitcount = 0
                            
        if digitcount == 0:
            hexadecimal = 0

        #WARNING: If the input value is above 16777215 this will return an error                       
        else:
            print("Input value is too high")
            giveoutput = False

        #Places the hexadecimal components together
        hexadecimal = str(sixthkey) + str(fifthkey) + str(fourthkey) + \
                      str(thirdkey) + str(secondkey) + str(firstkey)

        #outputs a hexadecimal in the form of the integer input
        if giveoutput == True:
            hexout = "0x" + str(hexadecimal)
            print(hexout)