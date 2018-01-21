# import modules
import os, time
import random
import sys

# word dictionar for bot memory
nameIn = ['What is your name','what is your name','whats your name','what is your name?','whats your name?',]
grettingsIn = ['hello','hi','Hi','hlw','hi there','hello there',]
birth = ['what is your date of birth','what is your date of birth?','what is your DOB', 'what is your DOB?',]
botmaster = ['who is your botmaster','who is your botmaster?','who is your father','who is your mother',]

nameOut = ['I am called Bot','Hi name is Bot','i am called Bot',]
grettingsOut = ['hi there','Hello','Hi my name is Bot, how can i help you','hello there']

B = '\n\n\n\n\n\n\n\n Mr.Bot is in Online....'

print(B)
while True:
    inputs = raw_input('=>').strip()
    Hlower = inputs.lower()

    if inputs == '':
        print '=> Thank you Boss, Nice to meet you.'
        time.sleep(1)
        # os.system('sudo shutdown -h now')
        os.system('exit')
        break
    elif Hlower in nameIn:
        print '=>' + (random.choice(nameOut))
    elif Hlower in grettingsIn:
        print '=>' + (random.choice(grettingsOut))
    elif Hlower in botmaster:
        print '=> My botmaster is Metamorphosis.'
    elif Hlower in birth:
        print '=> I was activated in the 28th of January 2018 By Mr.Arnav'
    else:
        print "=> Sorry i can't get you..."           

