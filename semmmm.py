
import speech_recognition as sr



from googletrans import Translator


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def takeCommand(p):
    r = sr.Recognizer()
    with sr.Microphone() as source:


        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")

            Query = r.recognize_google(audio,language=p)#, language='hi-In'


            print("the query is printed='", Query, "'")




        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return Query

def trans(query):

    translator = Translator()
    result = translator.translate(query,dest='en', src='auto')
    return result

def htr(query):

    translator = Translator()
    result = translator.translate(query,dest='hi', src='auto')
    return result


lang=int(input("choose the language\n1.Hindi\n2.Malayalam\n3.Marathi\n4.Kannada\n5.Gujarati"))
if lang ==1:
    p='hi-In'
if lang==2:
    p='ml-In'
if lang==4:
    p='kn-In'
if lang==3:
    p='mr-In'
if lang==5:
    p='gu-In'


query=takeCommand(p)


text=trans(query)


t1=htr(query)


print(text)
print(t1)

analyzer = SentimentIntensityAnalyzer()


sentiment_dict = analyzer.polarity_scores(text.text)

print("\nTranslated Sentence=", text,text, "\nDictionary=", sentiment_dict)
if sentiment_dict['compound'] >= 0.05:
    print("It is a Positive Sentence")

elif sentiment_dict['compound'] <= - 0.05:
    print("It is a Negative Sentence")
else:
    print("It is a Neutral Sentence")

