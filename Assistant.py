from gtts import gTTS
from playsound import playsound
import random
#===============================================INITIALIZATION==========================================================
initialization = "Initializing data"
language = 'en'
myobj = gTTS(text=initialization, lang=language, slow=False)
myobj.save("initialization.mp3")
playsound("initialization.mp3")
import datetime
#==============================================Asking the user for input================================================
askinit = gTTS(text="What should I do for you?", lang=language, slow=False)
askinit.save("askinit.mp3")
playsound("askinit.mp3")
#============================================Functions==================================================================
def time():
    timern = datetime.datetime.now()
    mytimern= gTTS(text="Please see the screen to see the time", lang=language, slow=False)
    mytimern.save("mytimern.mp3")
    playsound("mytimern.mp3")
    print(timern)
def nofunc():
    nofuncstr = gTTS(text="Sorry we don't provide this function right now", lang=language, slow=False)
    nofuncstr.save("nofuncstr.mp3")
    playsound("nofuncstr.mp3")
    print("Sorry we don't provide this function right now")

def help():
    helpstr=gTTS(text="List of available commands are  Time  help  calculator  nofunc", lang=language, slow=False)
    helpstr.save("help.mp3")
    playsound("help.mp3")
    print("List of all commands\n"
          "1)Help\n"
          "2)Time\n"
          "3)nofunc\n"
          "4)calculator\n")
def calculator():
    print("calculator")

def greet(yo):
    name = raw_input("What's your name: ")
    return yo + name
print greet("hi! ")


#================================================Asking the user for input==============================================
while True:
   r1 = random.randint(1, 10000000)
   r2 = random.randint(1, 10000000)
   task = input('What should I do for you?')
   mytask = gTTS(text="Received Query   "+task , lang=language , slow=False)
   mytask.save(str(r1)+("task")+str(r2)+(".mp3"))
   playsound(str(r1)+("task")+str(r2)+(".mp3"))
if task==("time"):
       time()
   elif task==("calculate"):
       calculator()
   elif task==("help"):
       help()
   elif task==("calculator"):
       calculator()
   else:
       nofunc()



