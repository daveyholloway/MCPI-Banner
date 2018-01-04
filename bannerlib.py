# #####################################################################
#
# getChar:
#
# This function returns a string that represents an 8 * 8
# representation of the character passed in.
#
# USAGE:
#
#    myValue = getChar("a")
#
# MODIFICAION HISTORY:
#
# When       Who              Why
# ========== ================ =========================================
# 23/07/2015 Dave Hol'        Initial Version, numbers, alpha
#                             (upper and lower) and a few special
#                             characters supported.
#
#
# #####################################################################


def getChar(pIn):
    if pIn=="1":
        return("   xx   " + \
               "  xxx   " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               " xxxxxx " + \
               "        ")
    elif pIn=="2":
        return("  xxxx  " + \
               " x   xx " + \
               "     xx " + \
               "    xx  " + \
               "   xx   " + \
               "  xx    " + \
               " xxxxxx " + \
               "        ")
    elif pIn=="3":
        return("  xxxx  " + \
               " xx  xx " + \
               "     xx " + \
               "   xxx  " + \
               "     xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="4":
        return("    xx  " + \
               "   xxx  " + \
               "  x xx  " + \
               " xx xx  " + \
               " xxxxxx " + \
               "    xx  " + \
               "    xx  " + \
               "        ")
    elif pIn=="5":
        return(" xxxxxx " + \
               " xx     " + \
               " xxxxx  " + \
               "     xx " + \
               "     xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="6":
        return("   xxx  " + \
               "  xx    " + \
               " xx     " + \
               " xxxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="7":
        return(" xxxxxx " + \
               "     xx " + \
               "    xx  " + \
               "   xx   " + \
               "  xx    " + \
               "  xx    " + \
               "  xx    " + \
               "        ")
    elif pIn=="8":
        return("  xxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="9":
        return("  xxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               "   xxxx " + \
               "     xx " + \
               "    xx  " + \
               "  xxx   " + \
               "        ")
    elif pIn=="0":
        return("  xxxx  " + \
               " xx  xx " + \
               " xx xxx " + \
               " xxxxxx " + \
               " xxx xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="A":
        return("  xxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               " xxxxxx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               "        ")
    elif pIn=="B":
        return(" xxxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               " xxxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               " xxxxx  " + \
               "        ")
    elif pIn=="C":
        return("  xxxx  " + \
               " xx  xx " + \
               " xx     " + \
               " xx     " + \
               " xx     " + \
               " xx  xx " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="D":
        return(" xxxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xxxxx  " + \
               "        ")
    elif pIn=="E":
        return(" xxxxxx " + \
               " xx     " + \
               " xx     " + \
               " xxxxx  " + \
               " xx     " + \
               " xx     " + \
               " xxxxxx " + \
               "        ")
    elif pIn=="F":
        return(" xxxxxx " + \
               " xx     " + \
               " xx     " + \
               " xxxxx  " + \
               " xx     " + \
               " xx     " + \
               " xx     " + \
               "        ")
    elif pIn=="G":
        return("  xxxx  " + \
               " xx  xx " + \
               " xx     " + \
               " xx xxx " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="H":
        return(" xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xxxxxx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               "        ")
    elif pIn=="I":
        return(" xxxxxx " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               " xxxxxx " + \
               "        ")
    elif pIn=="J":
        return("  xxxxx " + \
               "    xx  " + \
               "    xx  " + \
               "    xx  " + \
               "    xx  " + \
               " xx xx  " + \
               "  xxx   " + \
               "        ")
    elif pIn=="K":
        return(" xx  xx " + \
               " xx xx  " + \
               " xxxx   " + \
               " xxx    " + \
               " xxxx   " + \
               " xx xx  " + \
               " xx  xx " + \
               "        ")
    elif pIn=="L":
        return(" xx     " + \
               " xx     " + \
               " xx     " + \
               " xx     " + \
               " xx     " + \
               " xx     " + \
               " xxxxxx " + \
               "        ")
    elif pIn=="M":
        return(" xx   xx" + \
               " xxx xxx" + \
               " xxxxxxx" + \
               " xx x xx" + \
               " xx x xx" + \
               " xx   xx" + \
               " xx   xx" + \
               "        ")
    elif pIn=="N":
        return(" xx  xx " + \
               " xx  xx " + \
               " xxx xx " + \
               " xxxxxx " + \
               " xx xxx " + \
               " xx  xx " + \
               " xx  xx " + \
               "        ")
    elif pIn=="O":
        return("  xxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="P":
        return(" xxxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               " xxxxx  " + \
               " xx     " + \
               " xx     " + \
               " xx     " + \
               "        ")
    elif pIn=="Q":
        return("  xxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx x x " + \
               " xx xx  " + \
               "  xx xx " + \
               "        ")
    elif pIn=="R":
        return(" xxxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               " xxxxx  " + \
               " xx xx  " + \
               " xx  xx " + \
               " xx  xx " + \
               "        ")
    elif pIn=="S":
        return("  xxxx  " + \
               " xx  xx " + \
               " xx     " + \
               "  xxxx  " + \
               "     xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="T":
        return(" xxxxxx " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "        ")
    elif pIn=="U":
        return(" xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="V":
        return(" xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "   xx   " + \
               "        ")
    elif pIn=="W":
        return(" xx   xx" + \
               " xx   xx" + \
               " xx x xx" + \
               " xx x xx" + \
               " xxxxxxx" + \
               " xxx xxx" + \
               " xx   xx" + \
               "        ")
    elif pIn=="X":
        return(" xx  xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "   xx   " + \
               "  xxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               "        ")
    elif pIn=="Y":
        return(" xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "        ")
    elif pIn=="Z":
        return(" xxxxxx " + \
               "     xx " + \
               "    xx  " + \
               "   xx   " + \
               "  xx    " + \
               " xx     " + \
               " xxxxxx " + \
               "        ")
    elif pIn=="a":
        return("        " + \
               "        " + \
               "  xxxx  " + \
               "     xx " + \
               "  xxxxx " + \
               " xx  xx " + \
               "  xxxxx " + \
               "        ")
    elif pIn=="b":
        return(" xx     " + \
               " xx     " + \
               " xxxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xxxxx  " + \
               "        ")
    elif pIn=="c":
        return("        " + \
               "        " + \
               "  xxxx  " + \
               " xx  xx " + \
               " xx     " + \
               " xx  xx " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="d":
        return("     xx " + \
               "     xx " + \
               "     xx " + \
               "  xxxxx " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxxx " + \
               "        ")
    elif pIn=="e":
        return("        " + \
               "        " + \
               "  xxxx  " + \
               " xx  xx " + \
               " xxxxxx " + \
               " xx     " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="f":
        return("   xxx  " + \
               "  xx    " + \
               "  xx    " + \
               " xxxxx  " + \
               "  xx    " + \
               "  xx    " + \
               "  xx    " + \
               "        ")
    elif pIn=="g":
        return("        " + \
               "        " + \
               "  xxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxxx " + \
               "     xx " + \
               "  xxxx  ")
    elif pIn=="h":
        return(" xx     " + \
               " xx     " + \
               " xxxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               "        ")
    elif pIn=="i":
        return("   xx   " + \
               "        " + \
               "  xxx   " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="j":
        return("    xx  " + \
               "        " + \
               "   xxx  " + \
               "    xx  " + \
               "    xx  " + \
               "    xx  " + \
               "    xx  " + \
               "  xxx   ")
    elif pIn=="k":
        return(" xx     " + \
               " xx  xx " + \
               " xx xx  " + \
               " xx x   " + \
               " xxxx   " + \
               " xx xx  " + \
               " xx  xx " + \
               "        ")
    elif pIn=="l":
        return("  xxx   " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="m":
        return("        " + \
               "        " + \
               "  xx xx " + \
               " xxxxxxx" + \
               " xx x xx" + \
               " xx x xx" + \
               " xx   xx" + \
               "        ")
    elif pIn=="n":
        return("        " + \
               "        " + \
               " xxxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               "        ")
    elif pIn=="o":
        return("        " + \
               "        " + \
               "  xxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="p":
        return("        " + \
               "        " + \
               " xxxxx  " + \
               " xx  xx " + \
               " xx  xx " + \
               " xxxxx  " + \
               " xx     " + \
               " xx     ")
    elif pIn=="q":
        return("        " + \
               "        " + \
               "  xxxxx " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxxx " + \
               "     xx " + \
               "     xxx")
    elif pIn=="r":
        return("        " + \
               "        " + \
               " xx xx  " + \
               " xxx xx " + \
               " xx     " + \
               " xx     " + \
               " xx     " + \
               "        ")
    elif pIn=="s":
        return("        " + \
               "        " + \
               "  xxxxx " + \
               " xx     " + \
               "  xxxx  " + \
               "     xx " + \
               " xxxxx  " + \
               "        ")
    elif pIn=="t":
        return("   xx   " + \
               "   xx   " + \
               "  xxxxx " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "    xxx " + \
               "        ")
    elif pIn=="u":
        return("        " + \
               "        " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxxx " + \
               "        ")
    elif pIn=="v":
        return("        " + \
               "        " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxx  " + \
               "   xx   " + \
               "        ")
    elif pIn=="w":
        return("        " + \
               "        " + \
               " xx   xx" + \
               " xx x xx" + \
               " xx x xx" + \
               " xxxxxxx" + \
               "  xx xx " + \
               "        ")
    elif pIn=="x":
        return("        " + \
               "        " + \
               " xx  xx " + \
               "  xxxx  " + \
               "   xx   " + \
               "  xxxx  " + \
               " xx  xx " + \
               "        ")
    elif pIn=="y":
        return("        " + \
               " xx  xx " + \
               " xx  xx " + \
               " xx  xx " + \
               "  xxxxx " + \
               "     xx " + \
               "     xx " + \
               "  xxxx  ")
    elif pIn=="z":
        return("        " + \
               "        " + \
               " xxxxxx " + \
               "    xx  " + \
               "   xx   " + \
               "  xx    " + \
               " xxxxxx " + \
               "        ")
    elif pIn==" ":
        return("        " + \
               "        " + \
               "        " + \
               "        " + \
               "        " + \
               "        " + \
               "        " + \
               "        ")
    elif pIn=="!":
        return("   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "        " + \
               "   xx   " + \
               "        ")
    elif pIn==".":
        return("        " + \
               "        " + \
               "        " + \
               "        " + \
               "        " + \
               "        " + \
               "   xx   " + \
               "   xx   ")
    elif pIn==",":
        return("        " + \
               "        " + \
               "        " + \
               "        " + \
               "        " + \
               "   xx   " + \
               "   xx   " + \
               " xx     ")
    elif pIn=="(":
        return("     xx " + \
               "    xx  " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "    xx  " + \
               "     xx " + \
               "        ")
    elif pIn==")":
        return(" xx     " + \
               "  xx    " + \
               "   xx   " + \
               "   xx   " + \
               "   xx   " + \
               "  xx    " + \
               " xx     " + \
               "        ")
    elif pIn=="?":
        return("  xxxx  " + \
               " xx  xx " + \
               "    xx  " + \
               "   xx   " + \
               "   xx   " + \
               "        " + \
               "   xx   " + \
               "        ")
    elif pIn=="@":
        return("  xxxx  " + \
               " xx  xx " + \
               " xx xxx " + \
               " xx x x " + \
               " xx xxx " + \
               " xx     " + \
               "  xxxx  " + \
               "        ")
    elif pIn=="'":
        return("    xx  " + \
               "    xx  " + \
               "   x    " + \
               "        " + \
               "        " + \
               "        " + \
               "        " + \
               "        ")
    else:
        return("        " + \
               " xxxxxx " + \
               " x    x " + \
               " x    x " + \
               " x    x " + \
               " x    x " + \
               " xxxxxx " + \
               "        ")

# #####################################################################
#
# getSpecialChar:
#
# This function returns a string that represents an 8 * 8
# representation of a special character (e.g. a smiley). To use it
# pass in the string that corresponds to the character you want.
#
# SUPPORTED CHARACTERS:
# (Check the code to be sure!)
#
#    smiley, sad, block
#
# USAGE:
#
#    myValue = getChar("smiley")
#
# MODIFICAION HISTORY:
#
# When       Who              Why
# ========== ================ =========================================
# 23/07/2015 Dave Hol'        Initial Version, just a few characters at
#                             the moment.
#
#
# #####################################################################
def getSpecialChar(pIn):
    if pIn=="smiley":
        return("  xxxx  " + \
               " x    x " + \
               "x x  x x" + \
               "x      x" + \
               "x x  x x" + \
               "x  xx  x" + \
               " x    x " + \
               "  xxxx  ")
    if pIn=="sad":
        return("  xxxx  " + \
               " x    x " + \
               "x x  x x" + \
               "x      x" + \
               "x  xx  x" + \
               "x x  x x" + \
               " x    x " + \
               "  xxxx  ")
    elif pIn=="block":
        return("xxxxxxxx" + \
               "xxxxxxxx" + \
               "xxxxxxxx" + \
               "xxxxxxxx" + \
               "xxxxxxxx" + \
               "xxxxxxxx" + \
               "xxxxxxxx" + \
               "xxxxxxxx")
    else:
        return("        " + \
               " xxxxxx " + \
               " x    x " + \
               " x    x " + \
               " x    x " + \
               " x    x " + \
               " xxxxxx " + \
               "        ")

# #####################################################################
#
# wrap:
#
# Pass in a string and a line length and this function will return a
# list of lines that make up the original message but split so that
# no line exceeds the specified number of characters.
#
# USAGE:
#
#    messageLines = wrap("Hello everyone how are you",10)
#
# MODIFICAION HISTORY:
#
# When       Who              Why
# ========== ================ =========================================
# 23/07/2015 Dave Hol'        Initial Version, doesn't handle where a
#                             single word in the list is longer than
#                             the required length.
# 04/01/2018 Dave Hol'        Fixed the bug where a single line causes
#                             a crash! Bug reported above, still not
#                             fixed!
# #####################################################################
def wrap(pMessage, pLineWidth):

    # Define a list of lines to be passed back
    wLines=[]

    # First split the message into a list of words
    wWordList = pMessage.split()

    # Clear a line
    wLine = ""

    # Start looping through the words
    for i in wWordList:

        # If this is the first time through, just append the
        # first word in the list
        if wLine=="":
            wLine = i
        else:

            # Check to see if the current line plus a space and the next
            # word is greater than the allowed line width ...
            if len(wLine + " " + i) > pLineWidth:
                # ... it is greater so save what we've got and reset the
                # line.
                wLines.append(wLine)
                wLine=i
            else:
                # ... it isn't greater so just append and continue.
                wLine=wLine + " " + i

    # If the current line hasn't been written to the list then
    # append it. Do this by checking that that last element matches the
    # current wLine. Check for an empty list first.
    if (not wLines) or (wLines[-1] != wLine):
        wLines.append(wLine)

    # Return the result
    return(wLines)

# #####################################################################
#
# banner:
#
# Uses the wrap function to generate a banner style rendering of a
# supplied message.
#
# USAGE:
#
#    messageLines = banner("Hello everyone how are you",10)
#
# MODIFICAION HISTORY:
#
# When       Who              Why
# ========== ================ =========================================
# 23/07/2015 Dave Hol'        Initial Version, wouldn't it be great
#                             if it worked in Minecraft!!
#
# #####################################################################
def banner(pMessage, pWrap):

    # Convert the message into lines (wrap it!)
    wMessageLines = wrap(pMessage, pWrap)

    # Now loop through the lines
    for wMessage in wMessageLines:

        # Declare an array to store the characters
        wWordList=[]

        # Load the array with the characters that make up the message
        for i in range(len(wMessage)):
           wWordList.append(getChar(wMessage[i]))

        # Now we have a list of strings, lets print them

        # Let's use a loop to cycle through the 8 lines needed to print these
        for i in range(8):
            # Clear the print line
            wPrintLine=""

            # Now loop thru the message characters
            for j in range(len(wWordList)):

                # Assemble the print line
                wPrintLine = wPrintLine + wWordList[j][i*8:(i*8)+7]

            # Print it
            print(wPrintLine)




# Start of code #######################################################


# The message to print
# banner("There once was a young man called Seamus, who's ekit sessions were famous!",8)
