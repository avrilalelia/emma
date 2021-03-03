import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyautogui as p
import random
import requests, json
import smtplib
import winsound
import webbrowser
import wolframalpha
from ecapture import ecapture as ec
from win10toast import ToastNotifier

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            perintah = listener.recognize_google(voice)
            perintah = perintah.lower()
            if 'emma' in perintah:
                perintah = perintah.replace('emma', '')
                print(perintah)
    except:
        pass
    return perintah

def timer(reminder, seconds):
    notificator = ToastNotifier()
    notificator.show_toast("Reminder", f"""Alarm will go off in {seconds} Seconds""", duration=20)
    notificator.show_toast(f"Reminder", reminder, duration=20)

    frequency = 2500
    duration = 1000
    winsound.Beep(frequency, duration)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('avrilalelia01@gmail.com', 'password')
    server.sendmail('avrilalelia01@gmail.com', to, content)
    server.close()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        talk("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        talk("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        talk("Hello,Good Evening")
        print("Hello,Good Evening")

def run_emma():
    command = take_command()
    print(command)
    if 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hi emma' in command or 'hello' in command:
        talk('Hello human')
    elif 'what is your name' in command:
        talk('I am Emma')
    elif 'how are you' in command:
        talk('I am fine thank you')
    elif "who made you" in command or "who created you" in command or "who build you" in command:
        talk("I was built by Avril")
        print("I was built by Avril")
    elif 'who are you' in command or 'what can you do' in command:
        talk('I am Emma version 1 point O your personal assistant. I am programmed to do minor tasks like'
              'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
              'In different cities, get top headline news and you can ask me computational or geographical questions too!')
    elif 'favorite' and 'color' in command:
        colors = ['blue', 'red', 'yellow', 'green', 'purple']
        talk('my favorite color is ' + random.choice(colors))
    elif ' how old are you' in command:
        talk('my owner Avril is seventeen years old')
    elif 'thank you' in command:
        talk('You are welcome')
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Curent time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'weather' in command:
        APIKEY = '8d0a5d2eed5524a68fb0b5c49c788d06'  # your API Key here as string
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        # upadting the URL
        city = 'Jakarta'
        URL = BASE_URL + "q=" + city + "&appid=" + APIKEY
        # HTTP request
        response = requests.get(URL)
        # checking the status code of the request
        if response.status_code == 200:
            # getting data in the json format
            data = response.json()
            # getting the main dict block
            main = data['main']
            # getting temperature
            temperature = main['temp'] - 273.15
            temp = f'{temperature:.2f}'
            # getting the humidity
            humidity = main['humidity']
            # getting the pressure
            pressure = main['pressure']
            # weather report
            report = data['weather']
            talk("Temperature is {} celcius".format(temp))
            talk("Humidity is {} percent".format(humidity))
            talk("Current Pressure is {} percent".format(pressure))
            talk("The weather in Jakarta today is {}".format(report[0]['description']))
            print("Temperature is {} celcius".format(temp))
            print("Humidity is {}".format(humidity))
            print("Current Pressure is {}".format(pressure))
            print("The weather in Jakarta today is {}".format(report[0]['description']))
        else:
            # showing the error message
            talk("Error in the HTTP request")
    elif 'put a reminder for' in command:
        reminder = command.replace('put a reminder for', '')
        talk('When I should put the reminder')
        take_command()
        time = command.replace('seconds later', '')
        timer(reminder, time)
    elif 'send email to sister' in command:
        recipient = command.replace('send email to', '')
        talk('What is the content of your email')
        content = take_command()
        penerima = 'aurilfriska@gmail.com'
        sendEmail(penerima, content)
        talk('email has been sent!')
    elif 'open youtube' in command:
        webbrowser.get(chrome_path).open("youtube.com")
    elif 'open google' in command:
        webbrowser.get(chrome_path).open("google.com")
    elif 'news' in command:
        webbrowser.get(chrome_path).open_new_tab("https://news.detik.com/")
        talk('Here are some headlines from Detik,Happy reading')
    elif 'search' in command:
        search = command.replace("search", "")
        url = "https://www.google.com.tr/search?q={}".format(search)
        webbrowser.get(chrome_path).open_new_tab(url)
    elif "camera" in command or "take a photo" in command:
        ec.capture(0, "robo camera", "img.jpg")
    elif 'ask' in command or 'question' in command:
        talk('I can answer to computational and geographical questions  and what question do you want to ask now')
        question = take_command()
        app_id = "Paste your unique ID here "
        client = wolframalpha.Client('XL4ERR-JWK28H626G')
        res = client.query(question)
        answer = next(res.results).text
        talk(answer)
        print(answer)
    elif 'send message' in command:
        number = '+6281283832646'
        talk('What is the context of your text?')
        y = talk_command()
        we.open('https://web.whatsapp.com/send?phone=' + number + '&text=' + y)
        time.sleep(60)
        p.press('enter')
    elif 'Goodbye' in 'command' or 'bye' in command or 'stop' in command:
        talk('Your personal assistant Emma is shutting down, goodbye')
    else:
        talk('please say the command again')

wishMe()
talk('How can I help you?')
while True:
    run_emma()