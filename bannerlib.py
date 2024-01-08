#######################################################################
# 
#######################################################################
import string 

#######################################################################
#
# importChars
#
# Reads the character file and loads it into a dictionary.
#
# USAGE:
#
#    importChars()
#
# MODIFICAION HISTORY:
#
# When       Who              Why
# ========== ================ =========================================
# 02/01/2024 Dave Hol'        Initial Version
#
#######################################################################
def importChars(pCharFile):

    wCharDict = {}
    wLineNo = 1

    # Open the file
    wFile = open(pCharFile, "r+")

    # Read the first line
    wBuffer = wFile.readline()

    while wBuffer:

        # Is the current line a key?
        if (wLineNo%9 == 1):
            wCurChar = wBuffer.strip()
            if wCurChar == "":
                wCurChar = " "
            # Not a key so for the first line, set the dictionary value
            # then append the data to the value for subsequent 
            # lines for the current key
        elif (wLineNo%9 == 2):
            wCharDict[wCurChar] = wBuffer.strip()
        else:
            wCharDict[wCurChar] = wCharDict[wCurChar] + wBuffer.strip()

        # Read the next line
        wBuffer = wFile.readline()
        wLineNo = wLineNo + 1

    # Close the file
    wFile.close()

    # Return the loaded dictionary
    return wCharDict
    
#######################################################################
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
# 03/01/2024 Dave Hol'        Now driven by a file instead of hardcoded
#                             values.
#
#
#######################################################################
def getChar(pIn):

    # Define a default character if we don't have a matching key
    wDefault = "..####.." + \
               ".##..##." + \
               "....##.." + \
               "...##..." + \
               "...##..." + \
               "........" + \
               "...##..." + \
               "........"
    # Load the character definitions from the local text file into
    # a dictionary
    wDictionary = importChars("masterCharsWorking.txt")

    # Check that the character requred exists
    if (pIn in wDictionary):
        return(wDictionary[pIn])
    else:
        # Return a default character if we don't have a corresponding
        # dictionary entry
        return(wDefault)

#######################################################################
#
# chop:
#
# Chop a single word up based on the width specified, return a list
#
# USAGE:
#
#    myValue = chop("bananas",5)
#
# MODIFICAION HISTORY:
#
# When       Who              Why
# ========== ================ =========================================
# 03/01/2024 Dave Hol'        Initial Version
#
#######################################################################
def chop(pIn, pWidth):

    wResult=[]

    # First, if the input is already less than the width then
    # just return a single item
    if len(pIn) <= pWidth:
        return([pIn])

    else:
        # The string's too long so chop it into bits using slicing
        for i in range(0, (len(pIn)//pWidth)+1):
            #print(i*pWidth,":",((i+1)*pWidth)-1)
            wResult.append(pIn[(i*pWidth):(i+1)*pWidth])
        return(wResult)

#######################################################################
#
# getWordList:
#
# Start with a string of words and chop them up into individual words,
# where a word is longer then the required width, chop it up too.
# Return a list object.
#
# USAGE:
#
#    myValue = getWordList("I exude the essence of bananas",5)
#
# MODIFICAION HISTORY:
#
# When       Who              Why
# ========== ================ =========================================
# 03/01/2024 Dave Hol'        Initial Version
#
#######################################################################
def getWordList(pIn, pWidth):

    wResult=[]

    # First, just split into words (space delimited)
    wTempList = pIn.split()

    # Now look at each word in the list, if it's longer then the
    # required width, split that too.
    for wWord in wTempList:
        if len(wWord) <= pWidth:
            wResult.append(wWord)
        else:
            wResult = wResult + chop(wWord,pWidth)

    return(wResult)

#######################################################################
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
# 03/01/2024 Dave Hol'        Now splits the initial string up using
#                             the getWordList function which should fix
#                             the long single word bug above.
#######################################################################
def wrap(pMessage, pLineWidth):

    # Define a list of lines to be passed back
    wLines=[]

    # First split the message into a list of words
    wWordList = getWordList(pMessage, pLineWidth)

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

#######################################################################
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
# 03/01/2024 Dave Hol'        Uses replace to convert the periods and
#                             hashes (pound symbols) to space and block
#                             characters in the output. Possibly font
#                             dependant, I'm using Lucidia Console.
#######################################################################
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
            print(wPrintLine.replace("."," ").replace("#","\\u2588".encode().decode('raw_unicode_escape')))

# Start of code #######################################################


# The message to print
banner("The boy stood on the burning deck his feet were all a quiver, he had a cough, his leg fell off and floated down the river!",12)
#banner("£$%^&*!?<>@{}][",8)
#banner("A",8)
