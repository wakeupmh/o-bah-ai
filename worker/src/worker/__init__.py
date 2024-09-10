import speech_recognition as sr
import webbrowser

def main() -> int:
    print("Hello from worker!")
    speech_engine = sr.Recognizer()

    with sr.Microphone() as micro:
        print("Recording...")
        audio = speech_engine.record(micro, duration=5)
        print("Recognizing...")
        text = speech_engine.recognize_google(audio, language="en")
        print(text)
    if text == 'come on':
        print("I am sorry, Sir")
    elif str.lower(text) in ['dididodo', 'di di do do', 'gi gi do do', 'gigi dodo']:
        webbrowser.open("https://www.youtube.com/results?app=desktop&search_query=rbd")
        print("opening RBD")
    else:
        print("Unrecognized Command")
    return 0
