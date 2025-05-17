#🎙️ Speech-to-Text App Using Python

A simple and efficient Speech-to-Text (STT) application built with Python and the SpeechRecognition library. This project captures live microphone input and converts spoken words into written text using Google's speech recognition API.

---

## 📌 Objective
To demonstrate how to convert spoken language into text using Python, enabling voice-driven applications, accessibility tools, and voice commands.

---

## 📝 Overview
-🎧 Captures audio input from your microphone.
-🧠 Uses the speech_recognition library to convert speech into text.
-🌐 Requires internet access for Google's speech recognition API.
-⚠️ Handles ambient noise and errors gracefully.
-🚀 Beginner-friendly, ideal for learning voice input processing.

---
## Code
```sh
python --version
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


```
---
## 📜 Code Explanation
-**sr.Recognizer()** creates a recognizer instance to process audio.
-**sr.Microphone()** sets up the microphone input stream.
-**adjust_for_ambient_noise()** calibrates the recognizer for surrounding noise.
-**r.listen()** listens to the microphone input within specified timeout and phrase limits.
-**recognize_google()** sends audio data to Google's API for transcription.
-Handles errors such as unintelligible audio **(UnknownValueError)** and connection issues (RequestError).

---

## 📢 Conclusion

This project introduces speech recognition concepts using Python and is a stepping stone to developing voice-controlled apps, transcription tools, and hands-free interfaces.
If you like this project, please ⭐ star the repository! 😊

---
### 🤝 Contribution
Contributions are always welcome!
If you want to improve the UI or add new features, follow these steps:

- Fork this repository 📌
- Make necessary changes 🛠️
- Create a pull request 🔄

----


## 👨‍💻 Author

  Shivani Sharma
  
📌 Passionate about Python, Data Science, and GUI Development.

🌐 Connectact : shivanisharmaf128@gail.com 
