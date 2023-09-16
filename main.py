
import googletrans
import speech_recognition
import gtts
import playsound



print(googletrans.LANGUAGES)

recognizer = speech_recognition.Recognizer()
translator = googletrans.Translator()
primaryLanguage = input("\nYour language: ")
translateLanguage = input("Translate Language: ")



try:
    with speech_recognition.Microphone() as source:
        print("Listening..")
        listen = recognizer.listen(source)
        convertText = recognizer.recognize_google(listen, language=primaryLanguage)
        print(convertText)
except:
    pass


translate = translator.translate(convertText, dest=translateLanguage)
print(translate.text) # type: ignore
speak = gtts.gTTS(translate.text, lang=translateLanguage) # type: ignore
speak.save('speak.mp3')
playsound.playsound('speak.mp3')


