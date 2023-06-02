################################### Import Modules ##################################

from MainFiles.Database.modules import playsound

################################### Opening Sound ##################################

def openSound():
    try:
        playsound("MainFiles\\sound\\Alfred.mp3")

    except Exception as e:
        pass

################################### Mid Sound ##################################

def midSound():
    try:
        playsound("MainFiles\\sound\\AlfredClosed.mp3")

    except Exception as e:
        pass

################################### Closing Sound ##################################

def closeSound():
    try:
        playsound("MainFiles\\sound\\AlfredMid.mp3")

    except Exception as e:
        pass

################################### Screeshot Camera Sound ##################################

def screenshotSound():
    try:
        playsound("MainFiles\\sound\\Screenshot.wav")

    except Exception as e:
        pass

################################### Email has been sent Sound ##################################

def EmailSent():
    try:
        playsound("MainFiles\\sound\\EmailSent.wav")

    except Exception as e:
        pass

################################### Coin flipping Sound ##################################

def coinFlip():
    try:
        playsound("MainFiles\\sound\\coin.mp3")

    except Exception as e:
        pass

################################### rolling dice Sound ##################################

def diceRoll():
    try:
        playsound("MainFiles\\sound\\dice.mp3")

    except Exception as e:
        pass

################################### Message has been sent Sound ##################################

def MsgSent():
    try:
        playsound("MainFiles\\sound\\MessageSent.wav")

    except Exception as e:
        pass

################################### End ##################################