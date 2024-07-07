import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI


#recognizer=sr.Recognizer()
recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi="3d46cded11074fe5bf89ecffa7ebe72c"

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# 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


# def airpocess(command):
#     client=OpenAI(api_key="your api key")

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#     {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
#     {"role": "user", "content": command}
#     ]
#     )

#     return(completion.choices[0].message.content)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open chrome" in command.lower():
        webbrowser.open("https://chrome.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
    elif "open spotify" in command.lower():
        webbrowser.open("https://spotify.com")
    elif command.lower().startswith("play"):
         song = command.lower().split(" ", 1)[1]
        # playsong(song)
         link = musiclibrary.music[song]
         webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    # else:
    #     output=airpocess(c)
    #     speak(output)





if __name__ == "__main__":
    speak("Hey there! Initializing Charlie")

    while True:

        recognizer = sr.Recognizer()
        print("Recognizing...")
        try:

            with sr.Microphone() as source:
               print("Listening...")
               recognizer.adjust_for_ambient_noise(source, duration=1)
               print("Listening for 'Charlie'...")
               audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
               word = recognizer.recognize_google(audio).lower()

               if word == "charlie":
                  speak("Yes?, How can i help you?")
                  print("Charlie active, listening for your command...")
                  audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                  command = recognizer.recognize_google(audio)
                  print(f"Command: {command}")
            

            process_command(command)


        except Exception as e:
            print("Sorry, I did not understand that")
        
            
  
