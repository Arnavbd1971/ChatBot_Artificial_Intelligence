import os, time
import random
import sys
import pyttsx

class Common():
    # word dictionar for bot memory
    grettingsIn = ['hello','hi','Hi','hlw','hi there','hello there','hola']
    grettingsOut = ['hi there','Hello','Hi my name is Bot, how can i help you','hello there']

    nameIn = ['What is your name','what is your name','whats your name','what is your name?','whats your name?','who are you?','who are you']
    nameOut = ['I am called Bot','Hi name is Bot','i am called Bot',]
    
    birth = ['what is your date of birth','what is your date of birth?','what is your DOB', 'what is your DOB?',]
    botmaster = ['who is your botmaster','who is your botmaster?','who is your father','who is your mother','who is your master',]

    

    def bot_speak(self, text):
        engine = pyttsx.init()
        engine.say(text)
        engine.runAndWait()

class MainEngine(Common):
    def __init__(self):
        B = '\n\n\n\n Mr.Bot is Online....'
        print(B)
        while True:
            
            user_inputs = raw_input('=>').strip()
            user_inputs_lower = user_inputs.lower()

            if user_inputs == '':
                reply = 'Thank you Boss, Nice to meet you.'
                print '=> '+ reply

                self.bot_speak(reply)

                time.sleep(1)
                os.system('exit')
                break

            elif user_inputs_lower in self.grettingsIn:
                grettingsreply = random.choice(self.grettingsOut)
                print '=> '+ grettingsreply
                self.bot_speak(grettingsreply)

            elif user_inputs_lower in self.nameIn:
                namereply = random.choice(self.nameOut)
                print '=> '+ namereply
                self.bot_speak(namereply)  

            elif user_inputs_lower in self.birth:
                birthreply = 'I was activated in the 28th of January 2018 By Mr.Arnav'
                print '=> '+ birthreply
                self.bot_speak(birthreply)

            elif user_inputs_lower in self.botmaster:
                botmasterreply = 'My botmaster is Metamorphosis.'
                print '=> '+ botmasterreply
                self.bot_speak(botmasterreply)           
                
            else:
                elsereply = "Sorry i can't get you." 
                print "=> "+elsereply
                self.bot_speak(elsereply)



chatBot =  MainEngine()      

    