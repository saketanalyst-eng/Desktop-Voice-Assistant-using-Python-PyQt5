from md import *

from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import pywhatkit
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import pyautogui as p
import os
import keyboard
import datetime
from playsound import playsound
import smtplib
import random
import PyPDF2
import requests
from bs4 import*



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good night")

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    
        self.JARVIS()

    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text
    
    def read():
      book= open('python book.pdf',"rb")
      pdf=PyPDF2.PdfFileReader(book)
      pages=pdf.numPages
      for num in range(7,pages):
        page=pdf.getPage(7)
        text=page.extractText()
        speak(text)
        
    def wishme():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak('good morning sir')
            speak('its time to wake up sir ')
        elif hour>=12 and hour<18:
            speak('good after noon sir ')
        else:
            speak('good evening ')
        speak('i amm saket how can help you')
    
   
    def game_play(self):
      speak ('lets play  rock paper scissor game sir')
      
      i=0
      My_score=0
      com_score=0

      while(i<5):
          choose=('rock','paper','secissor')
          com_choose=random.choice(choose)
          query= self.STT().lower()
          if(query=='rock'):
            if(com_choose=='rock'):
                speak('rock')
                print(f'score:-Me:-{My_score}:Com:-{com_score}')
            elif(com_choose=='paper'):
                speak('paper')
                com_score+=1
                print(f'score:-Me:-{My_score}:Com:-{com_score}')
            else:
                speak('scissor')
                My_score+=1
                print(f'score:-Me:-{My_score}:Com:-{com_score}')

          elif(query=='paper'):
            if(com_choose=='rock'):
                speak('rock')
                My_score=+1
                print(f'score:-Me:-{My_score}:Com:-{com_score}')
            elif(com_choose=='paper'):
                speak('paper')
                
                print(f'score:-Me:-{My_score}:Com:-{com_score}')
            else:
                speak('scissor')
                com_score+=1
                print(f'score:-Me:-{My_score}:Com:-{com_score}')
          elif(query=='scissor'):
            if(com_choose=='rock'):
                speak('rock')
                com_score+=1
                print(f'score:-Me:-{My_score}:Com:-{com_score}')
            elif(com_choose=='paper'):
                speak('paper')
                My_score+=1
                print(f'score:-Me:-{My_score}:Com:-{com_score}')
            else:
                speak('scissor')
                
                print(f'score:-Me:-{My_score}:Com:-{com_score}')
          i+=1
      print(f'Final score:-My:-{My_score}:com:-{com_score}')
    
        

    




    

   

    def JARVIS(self):
        wish()
        speak('now may to introdude my self i amm your personal voice assitant i amm here to help you twenty four hours in a day seven days in weak')
        def game_play(self):
            speak ('lets play  rock paper scissor game sir')
            
            i=0
            My_score=0
            com_score=0

            while(i<5):
                choose=('rock','paper','secissor')
                com_choose=random.choice(choose)
                query= self.STT().lower()
                if(query=='rock'):
                    if(com_choose=='rock'):
                        speak('rock')
                        print(f'score:-Me:-{My_score}:Com:-{com_score}')
                    elif(com_choose=='paper'):
                        speak('paper')
                        com_score+=1
                        print(f'score:-Me:-{My_score}:Com:-{com_score}')
                    else:
                        speak('scissor')
                        My_score+=1
                        print(f'score:-Me:-{My_score}:Com:-{com_score}')

                elif(query=='paper'):
                    if(com_choose=='rock'):
                        speak('rock')
                        My_score=+1
                        print(f'score:-Me:-{My_score}:Com:-{com_score}')
                    elif(com_choose=='paper'):
                        speak('paper')
                        
                        print(f'score:-Me:-{My_score}:Com:-{com_score}')
                    else:
                        speak('scissor')
                        com_score+=1
                        print(f'score:-Me:-{My_score}:Com:-{com_score}')
                elif(query=='scissor'):
                    if(com_choose=='rock'):
                        speak('rock')
                        com_score+=1
                        print(f'score:-Me:-{My_score}:Com:-{com_score}')
                    elif(com_choose=='paper'):
                        speak('paper')
                        My_score+=1
                        print(f'score:-Me:-{My_score}:Com:-{com_score}')
                    else:
                        speak('scissor')
                        
                        print(f'score:-Me:-{My_score}:Com:-{com_score}')
                i+=1
            print(f'Final score:-My:-{My_score}:com:-{com_score}')
            
         


        

         


        def sendmail(to, content):
            server=smtplib.SMTP('smntp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.login('psaket755@gmail.com','satyam pandey')
            server.sendmail('psaket755@gmail.com',to,content)
            server.close()

        def read():
            book= open('python book.pdf',"rb")
            pdf=PyPDF2.PdfFileReader(book)
            pages=pdf.numPages
            for num in range(7,pages):
                page=pdf.getPage(7)
                text=page.extractText()
                speak(text)
        
        def openApps(self):
          speak('wait a secound')
          if'chrome'in self.query:
            os.startfile('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
          elif'instagram'in self.query:
            pywhatkit.search(self.query)
          elif'facebook'in self.query:
            pywhatkit.search(self.query)
          elif'YouTube search'in self.query:
            webbrowser.open('https://www.youtube.com//results?search_query')
          speak('your command completed')
     
        
        
        
        while True:
            
            self.query = self.STT()
            if 'good bye' in self.query:
                sys.exit()
            elif 'open google' in self.query:
                pywhatkit.search(self.query)
                speak("opening google")
            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
            
            if'hello' in self.query:
              
              speak('hello sir ,i amm saket')
              speak('how can i help you')
            
            elif'how are you'in self.query:
                speak('i amm fine ')
                speak('what about you')
            elif'thank you bye'in self.query:


              speak('ok sir , bye!')
              break
              sys.exit()
            elif'YouTube search'in self.query:
                speak('ok sir tish is your search')
                query=query.replace('saket',  '  ')
                query=query.replace('youTube search','  ')
                webbrowser.open='https://www.youtube.com/results?search_query='+query
            elif'google search'in self.query:
                speak('ok sir this is your search')
                query.replace('saket',' ')
                query.replace('google search',' ')
                pywhatkit.search(query)
                speak('done sir')        
            elif'wikipedia'in self.query:
                speak('searching wikipedia----')
                query.replace('saket','')
                query.replace('wikipedia---',' ') 
                wiki= wikipedia.summary(query,3)
                speak(f'acording to wikipedia : {wiki}')
             
            elif'chrome'in self.query:
                openApps(self)
            elif'my location' in self.query:
              speak('ok sir')
              pywhatkit.search(query)
            
            elif'meaning of'in self.query:
              speak ('ok')
              query.replace('meaning of',' ')
              pywhatkit.search(query)
            elif 'tell me time 'in self.query:

              strTime=datetime.datetime.now().strftime('%H:%M:%S')
              speak(f"sir the time is{strTime}")
            elif'send mail to 'in self.query:
                try:
                    speak('teel me massage sir')
                    content= self.STT()
                    to='triptipandey@gmail.com'
                    sendmail(to,content)
                    speak('done sir')
                except Exception as e:
                    print(e)
                    speak('sorry sir i cant send the massge sir')
            elif'i want to play game'in self.query:
               speak('play sir')
            
               game_play(self)
            elif'click my photo'in  self.query:
              speak('ok sir')
              p.press('super')
              p.typewrite('camera')
              p.press('enter')
              p.sleep(3)
              speak('smile please')
              p.press('enter') 
              speak('looking handsomesi')
            elif'read python book'in self.query:
              read()





        
startfunction=mainT

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.startTask)
        self.ui.pushButton.clicked.connect(self.close)
    def startTask(self):
        
        
        
        self.ui.movies=QtGui.QMovie("../gui material/gif 2.gif")
        self.ui.label_4.setMovie(self.ui.movies)
        self.ui.movies.start()
        self.ui.movies=QtGui.QMovie("../gui material/coner gif.gif")
        self.ui.label_5.setMovie(self.ui.movies)
        self.ui.movies.start()
       
        startfunction=mainT()
         
        



Gui_App=QApplication(sys.argv)
Gui_jarvis=main()
Gui_jarvis.show()
exit(Gui_App.exec_())











