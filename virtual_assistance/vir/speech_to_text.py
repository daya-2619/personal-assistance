import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        r.adjust_for_ambient_noise(source, duration=1)  # Calibrate to ambient noise
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=3)
    try:
        print("Recognizing...")
        voice_data = r.recognize_google(audio)
        print("You said:", voice_data)
        return voice_data
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return ""

