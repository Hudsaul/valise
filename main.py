import tweepy
import re
import webbrowser
import requests
import kivy

from kivy.app import App
from kivy.uix.label import Label


consumer_key = "cx928yggxLIeF76SRmfTm73Ij"
consumer_secret = "zhkFQ0c8yAx9XkuTtroQQCWVu3pSlwODlD8ny4ru4duXb813it"

access_token =  "22557347-fTlVt6OealYOS4Yu763nOXLfUUd8ESyFwtRnUHf2V"
access_token_secret = "DCq0J4GcRuFKiH7TrX1SCgbxRfosP7TjJF4BXuq9K6sI7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

valise = api.get_user('valisertl')

new_tweets = api.user_timeline(screen_name = valise.screen_name,count=3)

tweets = ''

for i in new_tweets:
    tweets = tweets + '\n ' + i.text
urls =  re.findall('https://t.co/\w+', tweets)

objects_formatted = []

for i in range(3):

    objects = []
    r = requests.get(urls[i])
    r.text
    objects_raw = re.findall('"articleBody":(.+)"@context"', r.text)

    objects_decode1 = objects_raw[0].decode('string_escape')

    objects_filtered = re.findall('([\s\d\w.\\\\(\)\[\]]*):\s?\[\[MORE\]\]([\[\]\(\)\s\d\w.\\\]*)',
                         objects_decode1)

    if objects_filtered != []:
        objects_decode2 =  [i.decode('unicode-escape') for i in objects_filtered[0]]

        for i in objects_decode2:
            objects.append(i + '\n')

        objects_formatted.append(objects[0] + objects[1] + '\n')

objects_final = ""

for i in objects_formatted:
    objects_final = objects_final + i

class MyApp(App):

    def build(self):
        return Label(text = objects_final)

MyApp().run()

