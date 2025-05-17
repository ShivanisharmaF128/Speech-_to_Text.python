import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")  
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for noise

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)  # Set limits
            voice_data = r.recognize_google(audio)  # Convert speech to text
            print("You said:", voice_data)
            return voice_data  # Return the recognized text
        
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio. Please try again.")
            return None  # Return None instead of an error
        
        except sr.RequestError:
            print("Could not connect to the speech recognition service.")
            return None  # Return None instead of an error

# **Calling the function**
text = speech_to_text()  
if text:
    print(f"Recognized Text: {text}")  

