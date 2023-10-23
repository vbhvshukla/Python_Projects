from gtts import gTTS
from playsound import playsound
import random
import pyttsx3

from langchain.tools import DuckDuckGoSearchRun
from langchain.utilities import WikipediaAPIWrapper

# ===============================================INITIALIZATION==========================================================
initialization = "Initializing data"
language = "en"
myobj = gTTS(text=initialization, lang=language, slow=False)
myobj.save("initialization.mp3")
playsound("initialization.mp3")
import datetime

# ==============================================Asking the user for input================================================
askinit = gTTS(text="What should I do for you?", lang=language, slow=False)
askinit.save("askinit.mp3")
playsound("askinit.mp3")


# ============================================Functions==================================================================
def time():
    timern = datetime.datetime.now()
    mytimern = gTTS(
        text="Please see the screen to see the time", lang=language, slow=False
    )
    mytimern.save("mytimern.mp3")
    playsound("mytimern.mp3")
    print(timern)


def nofunc():
    nofuncstr = gTTS(
        text="Sorry we don't provide this function right now", lang=language, slow=False
    )
    nofuncstr.save("nofuncstr.mp3")
    playsound("nofuncstr.mp3")
    print("Sorry we don't provide this function right now")


def help():
    helpstr = gTTS(
        text="List of available commands are  Time  help  calculator  nofunc",
        lang=language,
        slow=False,
    )
    helpstr.save("help.mp3")
    playsound("help.mp3")
    print("List of all commands\n" "1)Help\n" "2)Time\n" "3)nofunc\n" "4)calculator\n 5)Ask Wikipedia(wikipedia)\n 5)Search Web(search)\n ")


def calculator():
    num1 = int(input("enter first number= "))
    num2 = int(input("enter second number= "))
    op = input("+,-,*,/ ? = ")
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("Please choose from the given options only (+,-,*,/)")


def wiki():
    query = input("Ask me Anything: ")
    wikipedia = WikipediaAPIWrapper()
    result = wikipedia.run(query)
    print(result)


def search():
    query = input("Ask me Anything: ")
    search = DuckDuckGoSearchRun()
    result = search.run(query)
    print(result)

def greet(yo):
    name = input("What's your name: ")
    speak(yo + name)


def speak(audio):
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty("voices")

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty("voice", voices[0].id)

    # Method for the speaking of the assistant
    engine.say(audio)

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()


# ================================================Asking the user for input==============================================
while True:
    r1 = random.randint(1, 10000000)
    r2 = random.randint(1, 10000000)
    task = input("What should I do for you?")
    mytask = gTTS(text="Received Query " + task, lang=language, slow=False)
    mytask.save(str(r1) + "task" + str(r2) + ".mp3")
    playsound(str(r1) + "task" + str(r2) + ".mp3")

    if task == "time":
        time()
    elif task == "calculate":
        calculator()
    elif task == "help":
        help()
    elif task == "calculator":
        calculator()
    elif task == "wikipedia":
        wiki()

    elif task == "search":
        wiki()
    else:
        nofunc()
