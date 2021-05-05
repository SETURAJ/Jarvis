import wolframalpha
import pyttsx3
import speech_recognition as sr
import speech

client = wolframalpha.Client('U9VJAK-GKQ55Y47JQ')
while True:
    query = str(input('Query:'))
    res = client.query(query)
    output = next(res.results).text
    print(output)
    speech.say(output)
