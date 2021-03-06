#!/usr/bin/python3
from pyfiglet import Figlet
import yaml, random
import sys
import os
import datetime
import time
from multiprocessing import Process, Queue

from SpeechDriver.tts.ttsdefault import speak
from Services import weather, jokes_quote
from Core import textAnimation
from Core.profile import *
from Services import greeting

"""
print("                                            ")
print("  ________  .__               .__           ")
print("  \______ \ |__| ______ _____ |__| ______   ")
print("   |    |  \|  |/  ___//     \|  |/  ___/   ")
print("   |    `   \  |\___ \|  Y Y  \  |\___ \    ")
print("  /_______  /__/____  >__|_|  /__/____  >   ")
print("          \/        \/      \/        \/    ")
print("                                            ")   """


""" Ping google.com """ #Current not using in main instead using in brain.
from urllib.request import urlopen
def internetExamine():
    while True:
        try:
            response = urlopen('https://www.google.com/', timeout=10)
            print('on')
            return True
        except: 
            print('false')
            return False


""" Greeting """
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
        print('Good Morning!')
    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')
        print('Good Afternoon!')
    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')
        print('Good Evening!')






""" MULTIPROCESSING """
def Aneey_wishMailer(Aneey_wishMailer_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + Aneey_wishMailer_path + " &")
def Aneey_birthdayAlert(AneeyC_BirthdayAlert_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + AneeyC_BirthdayAlert_path + " &")
def Anum_wishMailer(Anum_wishMailer_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + Anum_wishMailer_path + " &")
def AnumBirthdayProtocal(AnumBirthdayAlert_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + AnumBirthdayAlert_path + " &")
def Anisha_wishMailer(Anisha_wishMailer_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + Anisha_wishMailer_path + " &")
def ask_email(ask_abtEmailreminder):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + ask_abtEmailreminder + " &")
def BestfriendBirthdayProtocal(BestfriendBirthdayProtocal_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + BestfriendBirthdayProtocal_path + " &")
def PersonalGmailNotify(PersonalGmailNotify_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + PersonalGmailNotify_path + " &")
def flask_credentials(flask_credentials_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + flask_credentials_path + "&")
def schedule(schedule_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + schedule_path + "&")

""" Desktop Notification """
"""
from gi.repository import Notify
# One time initialization of libnotify
Notify.init("Dismis_slave1")
# Create the notification object
title = "Dismis_slave1!"
body = "Meeting at 3PM!"
notification = Notify.Notification.new(
    title, body)
# Actually show on screen
notification.show() """
      

""" Booting """
def startup():
    """ Start Up """
    textAnimation.load_animation()
    time.sleep(0.30)
    print(' ')
    
    """ Dismis Banner """
    custom_fig = Figlet(font='graffiti')
    print(custom_fig.renderText('Dismis'))
    
    """ Greeting """
    greetMe()
    #time.sleep(0.30)
    
    """ Weather of Default Location """
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        weather.weather_DefaultCity(default_CityLocation, openweatherAPI, accept_path)
        time.sleep(9)
    
    """ Jokes """
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        jokes_quote.tell_joke(accept_path)
        time.sleep(3)
    
    """ Quote of The Day """
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        jokes_quote.quote(accept_path)
    
    """ Final Animation """
    def delay_print(s):
        import time
        import sys
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)
    delay_print("Hi, I'm Dismis. Nice to meet you!\n")
    time.sleep(0.20)
        
""" Running All Main Functions """
#startup()
""" Running Parallel Processes """
Anneybirthday_wisher = Process(target= Aneey_wishMailer(Aneey_wishMailer_path))
Anneybirthday_wisher.start()

Anneybirthday = Process(target= Aneey_birthdayAlert(AneeyC_BirthdayAlert_path))
Anneybirthday.start()

bhaibirthday_wisher = Process(target= Anum_wishMailer(Anum_wishMailer_path))
bhaibirthday_wisher.start()

bhaibirthday = Process(target = AnumBirthdayProtocal(AnumBirthdayAlert_path))
bhaibirthday.start()

Anishabirthday_wisher = Process(target= Anisha_wishMailer(Anisha_wishMailer_path))
Anishabirthday_wisher.start()

reminder =  Process(target=ask_email(ask_abtEmailreminder))
reminder.start()

bffbirthday = Process(target = BestfriendBirthdayProtocal(BestfriendBirthdayProtocal_path))
bffbirthday.start()

chkMail = Process(target = PersonalGmailNotify(PersonalGmailNotify_path))
chkMail.start()

credentials = Process(target = flask_credentials(flask_credentials_path))
credentials.start()

routine = Process(target = schedule(schedule_path))
routine.start()

