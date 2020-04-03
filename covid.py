import tweepy
import config
import pycountry
from pprint import pprint
from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential
import tweepy




def authenticate_client():
    ta_credential = TextAnalyticsApiKeyCredential(config.key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=config.endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

#-------------------------------------------------------------------------------------------

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


countries = list(pycountry.countries)

my_stream_listener = MyStreamListener()

#my_stream = tweepy.Stream(auth, listener=my_stream_listener)
#my_stream.filter(track=countries,is_async=True)

print(len(countries))

    
