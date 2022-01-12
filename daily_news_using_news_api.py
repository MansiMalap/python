import requests
import json
#import pywin32


def speak(str):
      from win32com.client import Dispatch
      speak=Dispatch ("SAPI.SpVoice")
      speak.Speak(str)

if __name__=='__main__':
    speak("Lets start with Todays top 7 headlines");
    newss= requests.get("https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=")#please user your api key
    #print(newss.text)
    news_parsed= json.loads(newss.text)
    #print(news_parsed["articles"])
    read=  news_parsed['articles']
    for count,today_news in enumerate(read):
    
        print(today_news['title'])
        speak(today_news['title'])
        
        if(count==6):
            speak("Done for today." )
            break
        speak("The next headline is..")
    speak("Thank You so much for your attension")
