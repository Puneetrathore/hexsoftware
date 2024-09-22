import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import os

# Initialize the speech recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Could not request results from Google.") 
            return ""

def respond(command):
    if 'play' in command:
        song = command.replace('play', '').strip()
        speak(f"Playing {song}")
        kit.playonyt(song)
    elif 'time' in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif 'open' in command:
        app = command.replace('open', '').strip()
        speak(f"Opening {app}")
        os.system(f'start {app}')  # Adjust for Linux or Mac if necessary
    elif 'stop' in command:
        speak("Goodbye!")
        return False
    else:
        speak("I am not sure how to respond to that.")
    return True

def main():
    speak("Hello! I am your voice assistant.")
    while True:
        command = listen()
        if not respond(command):
            break

if __name__ == "__main__":
    main()