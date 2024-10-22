import speech_recognition as sr
import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speech_to_text():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        text = "Say Something"
        text_to_speech(text)
        print("Say something")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        output_text = r.recognize_g(audio)
        print(f"You said {output_text}")

    except sr.UnknownValueError:
        print("Could not understand please say again")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
speech_to_text()