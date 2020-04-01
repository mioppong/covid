import tweepy
import config
import pycountry
from pprint import pprint

#authentication needed for twitter
auth = tweepy.OAuthHandler(config.api_key,config.api_secret)
auth.set_access_token(config.access_token,config.token_secret)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    #this method is called everytime there is a tweet
    #basically everytime we see a hashtag, increment each hashtag counter by 1

    def on_status(self,status):
        pass
        #print(status.text)

                       
        
    def on_error(self, status_code):
        if status_code == 420:
            print("ERRORRRRR")
            return False


countries = ['Canada','Italy']

my_stream_listener = MyStreamListener()

#my_stream = tweepy.Stream(auth, listener=my_stream_listener)
#my_stream.filter(track=countries,is_async=True)


for x in (list(pycountry.countries)):
    print(x.name)

    
