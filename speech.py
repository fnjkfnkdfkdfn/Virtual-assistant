import   pyttsx3
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_youtube():
    speak("Opening YouTube...")
    webbrowser.open("https://www.youtube.com")

def open_wikipedia():
    speak("Opening Wikipedia...")
    webbrowser.open("https://www.wikipedia.org")

def open_chrome():
    speak("Opening Chrome...")
    webbrowser.get("chrome").open("https://www.google.com")

def main():
    speak("Hello! my name is peter juniour, your virtual assistant. How can I help you?")
    
    while True:
        command = input("You: ").lower()

        if "hello" in command:
            speak("Hello! How can I assist you?")
        
        elif "open youtube" in command:
            open_youtube()
        
        elif "open wikipedia" in command:
            open_wikipedia()
        
        elif "open chrome" in command:
            open_chrome()
        
        elif "exit" in command:
            speak("Goodbye!")
            break
        
        else:
            speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()