import os 
import time, datetime
import smtplib
import random
import requests
import feedparser
from pyfiglet import Figlet
import json
import socket
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

#from Core.main import *
from SpeechDriver.tts.ttsdefault import speak

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

""" IMPORING PROFILE """
from Core.main import greetingTTS_path, greetingMail, schedule_Gcalendar, default_CityLocation, openweatherAPI, \
    slave_passwd, slave_sender,receiver, Ctoken_pickle, Ccredentials
greetingTTS = greetingTTS_path + '/SpeechDriver/tts/ServicesTTS/greetingTTS/'
#print(greetingTTS)
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'

    
""" GREETING SKILL """
def banner(greetingMail):
    custom_fig = Figlet(font='graffiti')
    poster = custom_fig.renderText('Dismis')
    #print(custom_fig.renderText('Dismis'))
    d=open(greetingMail,'a+')
    d.write("\n" + poster)
def extractTime(greetingMail):
    import datetime
    now = str(datetime.datetime.now())
    d=open(greetingMail, "a+")
    d.write("\n Extracted time is: " + now + "\n-----------------------------------------------------------------------------------------\n----------------------------------------------------------------------------------------- \n")

"********************************************************************************************************"

import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import pytz
import subprocess
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
def authenticate_google(Ctoken_pickle, Ccredentials):
    creds = None
    if os.path.exists(Ctoken_pickle):
        with open(Ctoken_pickle, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:            
            flow = InstalledAppFlow.from_client_secrets_file(Ccredentials, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(Ctoken_pickle, 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    return service
def get_events(day, service):
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)
    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        noEvent = 'No upcoming events found for today.'
        d=open(greetingMail,'a+')
        d.write("\n\t\t-- GOOGLE CALENDAR! --\nToday:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events today!!'
        d=open(greetingMail,'a+')
        d.write ("\n\t\t-- GOOGLE CALENDAR! --\nToday:>\n" + numEvent + "\n")
        for event in events:
            start = event['start'].get('dateTime' , event['start'].get('date'))
            #print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            #if int(start_time.split(":")[0]) < 12:
            #    start_time = start_time + " a m"
            #else:
            #    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            #    start_time = start_time + " p m"
            todayEvents = event["summary"] + " at " + start_time 
            d=open(greetingMail,'a+')
            d.write(todayEvents + "\n")
def get_date():
    today = datetime.date.today()
    return today
SERVICE = authenticate_google(Ctoken_pickle, Ccredentials)
def todayCal():
    date = get_date()
    if date:
        get_events(date, SERVICE)


""" FOR TOMORROW """
def authenticate_google2(Ctoken_pickle, Ccredentials):
    creds = None
    if os.path.exists(Ctoken_pickle):
        with open(Ctoken_pickle, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:            
            flow = InstalledAppFlow.from_client_secrets_file(Ccredentials, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(Ctoken_pickle, 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    return service

def get_events2(day, service):
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)
    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        noEvent2 = 'No events found for tomorrow.'
        d=open(greetingMail,'a+')
        d.write("Tomorrow:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent2 = f'You have {len(events)} events for tomorrow!!'
        d=open(greetingMail,'a+')
        d.write("\n\nTomorrow:>\n" + numEvent2 + "\n")
        for event in events:
            start = event['start'].get('dateTime' , event['start'].get('date'))
            #print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            #if int(start_time.split(":")[0]) < 12:
            #    start_time = start_time + " a m"
            #else:
            #    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            #    start_time = start_time + " p m"
            tomorrowEvents2 = event["summary"] + " at " + start_time 
            d=open(greetingMail,'a+')
            d.write(tomorrowEvents2 + "\n")
def get_date2():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return tomorrow 
SERVICE2 = authenticate_google2(Ctoken_pickle, Ccredentials)
def tomorrowCal():
    date = get_date2()
    if date:
        get_events2(date, SERVICE2)

"********************************************************************************************************"

def Jokes():
    import requests
    res = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    if res.status_code == requests.codes.ok:
        return str(res.json()["joke"])
def in_Dismis():
    jokes = [
        'What happens to a frogs car when it breaks down? It gets toad away.',
        'Why was six scared of seven? Because seven ate nine.',
        'Why are mountains so funny? Because they are hill areas.',
        'Have you ever tried to eat a clock?'
        'I hear it is very time consuming.',
        'What happened when the wheel was invented? A revolution.',
        'What do you call a fake noodle? An impasta!',
        'Did you hear about that new broom? It is sweeping the nation!',
        'What is heavy forward but not backward? Ton.',
        'No, I always forget the punch line.',
        'It’s hard to explain puns to kleptomaniacs because they always take things literally.',
        'A soldier survived mustard gas in battle, and then pepper spray by the police. He\'s now a seasoned veteran.'
        'What\'s the best thing about Switzerland? I don\'t know, but their flag is a huge plus.',
        'A Buddhist walks up to a hotdog stand and says, Make me one with everything.',
        'What\'s the difference between my ex and the titanic? The titanic only went down on 1,000 people.',
        'Two fish are sitting in a tank. One looks over at the other and says: Hey, do you know how to drive this thing?',
        'I told my doctor that I broke my arm in two places. He told me to stop going to those places.',
        'How do you keep an idiot in suspense?',
        'I hate Russian dolls...they\'re so full of themselves.',
        'My granddad has the heart of a lion and a lifetime ban from the San Diego Zoo.',
        'Rick Astley will let you borrow any movie from his Pixar collection, except one. He\'s never gonna give you up.',
        'There\'s no (I) in Denial.',
        'There are 10 types of people in the world: those who understand binary, and those who don\'t.',
        'What is red and smells like blue paint? Red Paint.',
        'What do you call bears with no ears? B',
        'I invented a new word! Plagiarism']
    return random.choice(jokes)
DismisJokeAPI = [Jokes, in_Dismis]
def tell_joke(greetingMail):
    dismis_jokes = random.choice(DismisJokeAPI)()
    #print(dismis_jokes)
    d=open(greetingMail,'a+')
    d.write ("-----------------------------------------------------------------------------------------\n\n\t\t-- JOKE! --\n" + dismis_jokes + "\n-----------------------------------------------------------------------------------------")

"********************************************************************************************************"

def quote(greetingMail):
    oftheday = feedparser.parse("https://www.brainyquote.com/link/quotebr.rss")     #QuoteOfTheDay
    Love = feedparser.parse("https://www.brainyquote.com/link/quotelo.rss")         #LoveQuoteOfTheDay
    Art = feedparser.parse("https://www.brainyquote.com/link/quotear.rss")          #ArtQuoteOfTheDay
    Funny = feedparser.parse("https://www.brainyquote.com/link/quotefu.rss")        #FunnyQuoteOfTheDay
    Natures = feedparser.parse("https://www.brainyquote.com/link/quotena.rss")      #NaturesQuoteOfTheDay
    quoteoftheday1 = oftheday['feed']['title']
    quoteoftheday2 = oftheday ["entries"][0]["description"]
    quoteoftheday2 = quoteoftheday2.replace('"', '')
    lovequote1 = Love['feed']['title']
    lovequote2 = Love["entries"][0]["description"]
    lovequote2 = lovequote2.replace('"', '')
    artquote1 = Art['feed']['title']
    artquote2 = Art["entries"][0]["description"]
    artquote2 = artquote2.replace('"', '')
    funnyquote1 = Funny['feed']['title']
    funnyquote2 = Funny["entries"][0]["description"]
    funnyquote2 = funnyquote2.replace('"', '')
    naturequote1 = Natures['feed']['title']
    naturequote2 =Natures["entries"][0]["description"]
    naturequote2 = naturequote2.replace('"', '')
    d=open(greetingMail,'a+')
    d.write("\n\n" + quoteoftheday1)
    d.write("\n" + quoteoftheday2 )
    d.write("\n\n" + lovequote1)
    d.write("\n" + lovequote2)
    d.write("\n\n" + artquote1)
    d.write("\n" + artquote2)
    d.write("\n\n" + funnyquote1)
    d.write("\n" + funnyquote2)
    d.write("\n\n" + naturequote1)
    d.write("\n" + naturequote2 + "\n-----------------------------------------------------------------------------------------")

"********************************************************************************************************"

def weather_DefaultCity(default_CityLocation, openweatherAPI, greetingMail):
    api_key = openweatherAPI
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + default_CityLocation 
    json_data=requests.get(complete_url).json()
    try:
        temp=json_data['main']
        temp=str(int(int(temp['temp'])-273.15))
        temp1=json_data['weather'][0]['description']
        wind_speed =json_data['wind']['speed']
        p = "\n\n\t\t-- CURRENT TEMPERATURE IN KAKARVITTA, NEPAL! --\nCurrent temperature in "+default_CityLocation+" is "+temp+" degree celsius with "+temp1+ " and \n" + 'wind speed is {} metre per seconds.'.format(wind_speed)
        d=open(greetingMail,'a+')
        d.write (p + "\n-----------------------------------------------------------------------------------------")
    except KeyError:
        error = "Key invalid or city not found"
        d=open(greetingMail,'a+')
        d.write ("\n\n" + error + "\n-----------------------------------------------------------------------------------------")

"********************************************************************************************************"

def Alert4(slave_sender, slave_passwd, receiver):
    try:
        fromaddr = slave_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "GREETING MAIL DATA!"# storing the subject  
        body = ''    # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "greetingMail.txt"    # open the file to be sent  
        attachment = open(greetingMail, "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, slave_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        speak('Greeting mail send boss.')
    except socket.gaierror:
        pass
    except:
        DisError = 'System Failure sir! Unable to send greeting data.'
        print('****************************************************************')
        print(' ')
        Log_Time()
        print('***' + DisError + '***')
        print(' ')
        print('****************************************************************')
        speak(DisError)
        
""" Main Greeting SKILLS """
def Greeting(accept_path):
    os.system('aplay ' + accept_path +' &')
    banner(greetingMail)
    extractTime(greetingMail)
    todayCal()
    tomorrowCal()
    tell_joke(greetingMail)
    quote(greetingMail)
    weather_DefaultCity(default_CityLocation, openweatherAPI,greetingMail)
    currentH = int(datetime.datetime.now().hour)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    if currentH >= 0 and currentH < 12:
        speak('Good Morning sir! It is '+time.strftime("%I:%M:%S %A"))
        print('Good Morning sir! It is '+time.strftime("%I:%M:%S am %A"))
    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon sir! It is '+time.strftime("%I:%M:%S %A"))
        print('Good Afternoon sir! It is '+time.strftime("%I:%M:%S pm %A"))
    if currentH >= 18 and currentH != 0:
        speak('Good Evening sir! It is '+time.strftime("%I:%M:%S %A"))
        print('Good Evening sir! It is '+time.strftime("%I:%M:%S pm %A"))
    Alert4(slave_sender, slave_passwd, receiver)
    Log_Time()
    print('\nGreeting mail sent accomplish')
    d=open(greetingMail,'r')
    greetingData = d.read()
    print(greetingData)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: Greeting')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    os.system('rm ' + greetingMail)


def imgoingout(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'PEMBA please check the schedule before going out.'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: imgoingout')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    speak(result)
    #imgoingout_txt = open(temporaryfiles + 'imgoingout.txt','w+')
    #imgoingout_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + conversationTTS + 'imgoingout__tts.py &')
    import smtplib, socket
    from email.mime.multipart import MIMEMultipart 
    from email.mime.text import MIMEText 
    from email.mime.base import MIMEBase 
    from email import encoders 
    try:
        fromaddr = slave_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "SCHEDULE AND GOOGLE CALENDAR's EVENTS!"# storing the subject  
        body = 'no body'   # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "schedule_Gcalendar.txt"    # open the file to be sent  
        attachment = open(schedule_Gcalendar, "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, slave_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        speak('Schedule send successfully in your primary mail')
    except socket.gaierror:
        pass
    #except:
    #    DisError = 'System Failure! Unable to perform I am going out skill sir'
    #    print('****************************************************************')
    #    print(' ')
    #    Log_Time()
    #    print('***' + DisError + '***')
    #    print(' ')
    #    print('****************************************************************')
    #    speak(DisError)

