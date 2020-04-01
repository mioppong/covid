import tweepy


#authentication needed for twitter
auth = tweepy.OAuthHandler(config.api_key,config.api_secret)
auth.set_access_token(config.access_token,config.token_secret)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    #this method is called everytime there is a tweet
    #basically everytime we see a hashtag, increment each hashtag counter by 1

    def on_status(self,status):
        pass
                       
        
    def on_error(self, status_code):
        if status_code == 420:
            print("ERRORRRRR")
            return False

print("yo")