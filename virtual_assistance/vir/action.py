import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather 

def action(data):
    user_data = data.lower()

    if "what is your name " in user_data :
        text_to_speech.text_to_speech("my name is Gen")
        
        
    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("hello , How can I help you...!!")
        
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("good morning sir, How can I help you...!!")
        
    elif "time now " in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time)+"Hour :" , (str)(current_time.minute)+"Minute"
        text_to_speech.text_to_speech(Time)
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir , shutting down the system")
        
    elif " play music" in user_data:
        webbrowser.open("https://jiosavan.com/")
        text_to_speech.text_to_speech("playing music")
    elif "weather" in user_data:
            ans=weather.Weather()
            text_to_speech.text_to_speech(ans)
            

    else :
        text_to_speech.text_to_speech("I'm not able to understand")    
        