import speech_recognition as sr
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Alexia: Listening...")
        audio=r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(f"master:{query}")
            return query
        except:
            print("try Again")

## Print(command()) ##uncomment this to test the function ###Run the code and speak anything and it will be printed on the screen    