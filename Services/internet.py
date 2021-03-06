#!/usr/bin/python3
from selenium import webdriver
import wikipedia
import wolframalpha
import re
import webbrowser
import os
import time

from SpeechDriver.tts.ttsdefault import speak


""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

""" IMPORING PROFILE """
from Core.profile import temporaryfiles, internetTTS_path
internetTTS = internetTTS_path + '/SpeechDriver/tts/ServicesTTS/internetTTS/'
#print(internetTTS)
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'


#search google
def google(voice_text, accept_path):
    os.system('aplay ' + accept_path +' &')
    try:
        webbrowser.open('https://www.google.com/search?q={}'.format(voice_text))
        result = 'Opening your query in google search engine sir'
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print(result)
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: google')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if os.uname()[1] == 'dslave':
            speak(result)
        else:
            google_txt = open(temporaryfiles + 'google.txt','w+')
            google_txt.write(result)
            os.system('gnome-terminal -- python3 ' + internetTTS + '__tts.py &')
    except:
        DisError = 'System Failure! Unable to perform google skill sir'
        print('****************************************************************')
        print(' ')
        Log_Time()
        print('***' + DisError + '***')
        print(' ')
        print('****************************************************************')
        speak(DisError)

def search_pics(voice_text, accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(0.28)
    try:
        #voice_text = input('name of picture: ')
        url = "https://www.google.com/search?tbm=isch&q={}".format(
            voice_text.replace("of", ""))
        webbrowser.open(url)
        result = 'show in the pictures of query sir'
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('show in the pictures of' + voice_text)
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: search_pics')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        #speak(result)
        search_pics_txt = open(temporaryfiles + 'search_pics.txt','w+')
        search_pics_txt.write(result)
        os.system('gnome-terminal -- python3 ' + internetTTS + 'search_pics__tts.py &')
    except:
        DisError = 'System Failure! Unable to perform search pics skill sir'
        print('****************************************************************')
        print(' ')
        Log_Time()
        print('***' + DisError + '***')
        print(' ')
        print('****************************************************************')
        speak(DisError)

def askinternet(voice_text, accept_path):
    os.system('aplay ' + accept_path +' &')
    reg_ex = re.search('internet(.+)', voice_text)
    if reg_ex:
        domain = reg_ex.group(1)
        result = 'extracting your query'
        try:
            app_id = "Q6Y3UQ-6T4J3423V7"
            client = wolframalpha.Client(app_id)
            res = client.query(domain)
            answer = next(res.results).text
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print(' ')
            print(' ')
            Log_Time()
            print('extract from Wolframalpha\n' + answer)
            print(' ')
            print(' ')
            print('\t\t\t\tSkill: askinternet')
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            result = answer
            askinternet_txt = open(temporaryfiles + 'askinternet.txt','w+')
            askinternet_txt.write(result)
            os.system('gnome-terminal -- python3 ' + internetTTS + 'askinternet__tts.py &')
        except:
            try:
                print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print(' ')
                print(' ')
                Log_Time()
                print('extract from wikipedia\n' + wikipedia.summary(domain, sentences=2))
                print(' ')
                print(' ')
                print('\t\t\t\tSkill: askinternet')
                print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                result = wikipedia.summary(domain, sentences=2)
                askinternet_txt = open(temporaryfiles + 'askinternet.txt','w+')
                askinternet_txt.write(result)
                os.system('gnome-terminal -- python3 ' + internetTTS + 'askinternet__tts.py &')
            except wikipedia.exceptions.PageError:
                print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print(' ')
                print(' ')
                Log_Time()
                print('Does not match any pages or query. Say again!')
                print(' ')
                print(' ')
                print('\t\t\t\tSkill: askinternet')
                print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    else:
        DisError = 'System Failure! Unable to perform ask internet skill sir'
        print('****************************************************************')
        print(' ')
        Log_Time()
        print('***' + DisError + '***')
        print(' ')
        print('****************************************************************')
        speak(DisError)

def open_website(voice_text, accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    reg_ex = re.search('open (.+)', voice_text)
    if reg_ex:
        domain = reg_ex.group(1)
        try:
            url = 'https://www.' + domain + '.com'
            webbrowser.open(url)
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print(' ')
            print(' ')
            Log_Time()
            print('user: ' + voice_text + '\n opening > Function: open_website')
            print(' ')
            print(' ')
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            result = 'Opened sir'
            open_website_txt = open(temporaryfiles + 'open_website.txt','w+')
            open_website_txt.write(result)
            os.system('gnome-terminal -- python3 ' + internetTTS + 'open_website__tts.py &')
        except webbrowser.Error:
            result = 'Facing some error sir'
            open_website_txt = open(temporaryfiles + 'open_website.txt','w+')
            open_website_txt.write(result)
            os.system('gnome-terminal -- python3 ' + internetTTS + 'open_website__tts.py &')
    else:
        DisError = 'System Failure! Unable to perform open website skill sir'
        print('****************************************************************')
        print(' ')
        Log_Time()
        print('***' + DisError + '***')
        print(' ')
        print('****************************************************************')
        speak(DisError)

def location(voice_text, accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    try:
        data = voice_text.split(" ")
        location = ""
        location = location.split(" ")
        for i in range(2, len(data)):
            location.append(data[i])
        str1 = "  ".join(location)
        result = "Hold on sir, I will show you."
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('Hold on sir, I will show you where' + str1 + 'is > Function: location')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        webbrowser.open("https://www.google.nl/maps/place/" + str1)
        location_txt = open(temporaryfiles + 'location.txt','w+')
        location_txt.write(result)
        os.system('gnome-terminal -- python3 ' + internetTTS + 'location__tts.py &')
    except:
        DisError = 'System Failure! Unable to perform location skill sir'
        print('****************************************************************')
        print(' ')
        Log_Time()
        print('***' + DisError + '***')
        print(' ')
        print('****************************************************************')
        speak(DisError)

def netspeed(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    try:
        url = 'http://speedtest.googlefiber.net/'
        webbrowser.open(url)
        result = 'checking net speed > Function: netspeed'
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print(result)
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        netspeed_txt = open(temporaryfiles + 'netspeed.txt','w+')
        netspeed_txt.write(result)
        os.system('gnome-terminal -- python3 ' + internetTTS + 'netspeed__tts.py &')
    except:
        DisError = 'System Failure! Unable to perform netspeed skill sir'
        print('****************************************************************')
        print(' ')
        Log_Time()
        print('***' + DisError + '***')
        print(' ')
        print('****************************************************************')
        speak(DisError)
