from tkinter import *
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import webbrowser
import pywhatkit
import random
import string
import os
import docx
# import contextlib


#defining BROTHER
assistant = pyttsx3.init('sapi5')  # Microsoft speech API-5 initialized

# fetch specific proferty for the variable
voices = assistant.getProperty('voices')
# assistant.setProperty("rate", 150)        #to change the speak rate
assistant.setProperty('voice', voices[0].id)

dt = datetime.now()  # current time
hour = dt.hour  # current hour
mn = dt.minute  # current minute
if hour >= 0 and hour < 12:
    samay = f"{hour} {mn} A.M."
if hour >= 12 and hour < 18:
    samay = f"{hour-12} {mn} P.M."
else:
    samay = f"{hour-12} {mn} P.M."

myName = "Gopal Sharma"  # name of owner of the assistant

# it makes it speak whatever is passed to it as a string

def speak(audio):
    # convert text to speech using .say() and returns audible output for string variable name audio
    assistant.say(audio)
    assistant.runAndWait()

# greets you according to the time

def wish():
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {myName}, It's {hour}{mn} A.M.")
    elif hour == 12 and mn < 1:
        speak(f"Good Noon {myName}, It's {hour}{mn} P.M.")
    elif hour >= 12 and hour < 16:
        speak(f"Good Afternoon {myName}, It's {hour-12}{mn} P.M.")
    else:
        speak(f"Good Evening {myName}, It's {hour-12}{mn} P.M.")

# takes command from the user via microphone

def get_command():
    # it takes input via mic from user and converts audio to string and gives it as output
    recog = sr.Recognizer()
    with sr.Microphone() as mic_source:
        # it adjust the energy threshold according to surrounding noises
        recog.adjust_for_ambient_noise(mic_source, duration=1.5)
        print("\nSay Something.....")
        audio = recog.listen(mic_source)

    try:
        print("Recognizing.....")
        statement = recog.recognize_google(audio, language='en-in')
        print(f"\nI recognized: {statement}\n")

    except Exception:
        print("Sorry! Please say it again.")
        return 'None'
    return statement

# introduces BROTHER, THE AI

def intro():
    speak(
        f"My name is BROTHER, THE A.I. . By the way, I am brother of {myName}, meanwhile you can say that I am his assistant. My residance is my Brother's PC. Though I can introduce myself but my Brother can make it more awesome!")

# sends message using whatsapp

def messaging(pnmbr, mesg, thr, tmin):
    try:
        pywhatkit.sendwhatmsg(pnmbr, mesg, thr, tmin)
    except Exception:
        pass

# converts the inputted string into integer

def integer(val):
    try:
        int_val = int(val)
        return int_val
        
    except Exception:
        speak("Sorry, I didn't got that.")

# generates random password according to the given length by the user

def password():
    try:
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s4 = string.punctuation
        s3 = string.digits

        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        random.shuffle(s)
        # print(s)
        speak("What should be the length of your password?")
        
        plen = get_command()
        pval = integer(plen)

        print("Your Password is:")
        print("".join(s[0:pval]))
    except Exception:
        pass

def document(title, text):
    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save(title + '.docx')

path = 'D:\\C Practice\\trial.txt'  #path of the text file stored here to where the console output is to be stored

# functions calling
def calling_everything():   
    try:
        # #to redirect the terminal or console output to a text file
        # with open(path, 'w') as f:
        #     with contextlib.redirect_stdout(f):
                #now the code works for recognizing the commands
                while True:
                    statement = get_command().lower()
                    # now tasks to be done
                    l1 = ['wikipedia', 'google', 'internet', 'bing','net']
                    for browse in l1:
                        if browse in statement:
                            speak(f'Fetching from {browse}')
                            statement = statement.replace(browse, "")
                            answer = wikipedia.summary(statement, sentences=3)
                            speak(f'As per {browse}')
                            print(answer)
                            speak(answer)

                    if('open youtube' in statement):
                        webbrowser.open("youtube.com")

                    elif('open google' in statement):
                        webbrowser.open("google.com")

                    elif 'open notepad' in statement or 'notepad' in statement:
                        speak("opening notepad!")
                        notepad = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad'
                        os.startfile(notepad)

                    
                    elif 'play music' in statement or 'play the song In the end' in statement or 'play a song' in statement:
                        music = 'D:\\music\\In the end.mp3'
                        speak("Playing the song, 'In the end' by Linkin Park")
                        os.startfile(music)

                    elif("time right now" in statement or 'time now' in statement):
                        speak(samay)

                    elif("send message" in statement or 'whatsapp' in statement or 'send a message' in statement):
                        try:
                            speak("Tell me the phone number to whom you want to send message")
                            nbr = get_command()
                            phnmbr = '+91' + nbr
                            speak("What's the message?")
                            msg = get_command()
                            speak("At what hour")
                            hr = get_command()
                            k1 = integer(hr)
                            speak("and at what minutes?")
                            mint = get_command()
                            k2 = integer(mint)
                            speak("Okay, all set, Sending Your Message.....")
                            messaging(phnmbr, msg, k1, k2)
                        except Exception:
                            pass

                    elif('password' in statement):
                        password()

                    elif 'open M S Word' in statement or ('open' and 'word' in statement):
                        word = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007'
                        speak("Opening Microsoft Office Word 2007")
                        os.startfile(word)

                    elif 'how are you' in statement:
                        speak("I am totally fine, tell me about you that how You are?")
                        how_being = get_command()
                        if 'fine' in how_being or 'good' in how_being or 'well' in how_being:
                            speak("That's good to hear from you!")
                        elif 'not fine' in how_being or 'not good' in how_being or 'not' in how_being:
                            speak("Oh I'm sorry, Please takecare of yours!")

                    elif 'thank you' in statement:
                        speak("oh! there isn't any need for thanks. Well it's my pleasure to assist you!")

                    elif 'what are you doing' in statement or "what's going on" in statement or "what's up" in statement:
                        speak("I am waiting for your command!")

                    elif 'who are you' in statement or 'your name' in statement:
                        speak("Ooooooooo my GOD, don't you know me?")
                        while(True):
                            statement_intro = get_command().lower()
                            if 'no' in statement_intro or "don't know" in statement_intro or "i don't know you" in statement_intro:
                                speak(
                                    "Fine, Noooo Problem. Now I am not going to tell you at all that Who am I!")
                            elif 'please tell about you' in statement_intro or 'sorry brother' in statement_intro or 'i will remember' in statement_intro:
                                speak("It's OK")
                                intro()
                                break
                            elif 'shut up' in statement_intro or 'shut' in statement_intro or 'behave yourself' in statement_intro:
                                while(True):
                                    speak("Oh I am really sorry for this kind of behaviour. Please forgive me.")
                                    statement_forgive = get_command().lower()
                                    try:
                                        if 'ok' in statement_forgive or 'next time' in statement_forgive or "it's ok" in statement_forgive or 'yes' in statement_intro:
                                            speak("Thanks for such a kind action. I will remember this next time and improve my behaviour!")
                                            break
                                        elif 'no' in statement_forgive or 'not' in statement_forgive:
                                            speak("I said naa, I am really very sorry!")
                                            get_command()
                                    except Exception:
                                        speak("I am still confused, had you forgave me or not?")
                                    
                                break
                    
                    elif 'nice' in statement or 'good' in statement:
                        speak("Thank You for the complement!")

                    elif 'introduce' in statement or 'about you' in statement:
                        intro()

                    elif 'where do you live' in statement:
                        speak("Actually, I resides into my Brother's computer and hence that is my permanent address!")
                    
                    elif 'who is your owner' in statement or 'name of owner' in statement or 'brother' in statement:
                        speak("My Owner's or Brother's name is Gopal Sharma. If you want more details about him, you may contact his father. JUST KIDDING")

                    elif('terminate yourself' in statement or 'exit yourself' in statement or 'close yourself' in statement or 'abort yourself' in statement):
                        speak("Okay! getting terminated, Takecare, Bye-Bye.")
                        exit()

                    elif('write a word document' in statement or 'create a document' in statement or 'create a word document' in statement):
                        speak('What should be the Title of the document?')
                        title = get_command()
                        speak('Now tell me the paragraph')
                        text = get_command()
                        document(title, text)
                                
                    else:
                        speak("Sorry! I can't process your command.")
                        calling_everything()
                    
    except Exception:
        calling_everything()

if __name__=="__main__":
    wish()
    calling_everything()

    # # with open('trial.txt') as f:
    # #     input_file = f.read()    

    # #defining GUI
    
    # brother =Tk()
    # brother.title("BROTHER, THE A.I.")
    # brother.geometry('1366x768')

    # input_frame = Frame(brother, bg='grey', borderwidth=3, relief=RIDGE)
    # input_frame.pack(side=RIGHT, padx=10, fill=Y)

    # img = PhotoImage(file = 'robo.png')

    # img_frame = Frame(brother)
    # img_frame.pack(side=LEFT, padx=10)

    # img_label=Label(img_frame, image = img)
    # img_label.pack(anchor='w')

    # input_label = Label(input_frame, text=input_file)
    # input_label.pack()

    # button = Button(input_frame,text='click to run BROTHER', command=calling_everything, borderwidth=2, relief=SUNKEN)
    # button.pack(pady=350)

    # brother.mainloop()