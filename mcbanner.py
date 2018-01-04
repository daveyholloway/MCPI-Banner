# This is the minecraft library
import mcpi.minecraft as minecraft

# BannerLib contains the code to build and wrap a message
import bannerlib as bn

# A little debug routine to post useful info in the chat console
def debug(pM,pMessage):
    pM.postToChat(pMessage)


# ##############################################################################
# This procedre plots a given character at a given coordinate
#
# Currently it prints in the x-y plane only
#
# TODO:
# Add a direction parameter so messages can be written in
# N->S, S->N, E->W, W->E, U->D and D->U
#
# ##############################################################################
def blockPrintChar(pX, pY, pZ, pChar, pBlockType, pBlockStyle):

    # Store the coordinates (not really needed
    x = pX
    y = pY
    z = pZ

    # Use the banner code to get the "pixel art" definition of
    # the character
    blockToPrint=bn.getChar(pChar)

    # Loop thru the pixel art and print it in blocks
    for i in range(len(blockToPrint)):
        if blockToPrint[i]=="x":
            mc.setBlock( x+(i%8), y+8-(i//8), z, pBlockType, pBlockStyle)
        else:
            mc.setBlock( x+(i%8), y+8-(i//8), z, 102)

# ##############################################################################
# This procedre uses the blockPrintChar procedure to print a message.
#
# ##############################################################################

def blockPrint(pX, pY, pZ, pMessage, pBlockType, pBlockStyle):
    for i in range(len(pMessage)):
        blockPrintChar(pX+(8*(i+1)), pY, pZ, pMessage[i],pBlockType, pBlockStyle)

# ##############################################################################
# The program starts here
# ##############################################################################

# Create a minecraft object
mc = minecraft.Minecraft.create()

# Tell us we've started
mc.postToChat("Started")

# Where am I, get the coordinates
pos = mc.player.getTilePos()

# Think of a suitable message
wMessage = "trust me trust no one"
debug(mc, wMessage)

# Wrap the message
wWrappedMessage = bn.wrap(wMessage,9)

# How many lines in the message ?
wLines = len(wWrappedMessage)
debug(mc,str(wLines) + " lines in the message")

# Print each line offset by 9 blocks
for i in range(wLines):

    # Print a message line
    debug(mc,wWrappedMessage[i])
    blockPrint(pos.x, pos.y+3+((wLines-i-1)*8), pos.z, wWrappedMessage[i], 48, 0)

# Tell us we're done
mc.postToChat("Finished")
