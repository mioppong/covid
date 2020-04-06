import config
import tweepy
from textblob import TextBlob
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd




df = pd.read_pickle('data.pkl')

#----------IN THIS SECTION I AM GOING TO STREAM TWEETS,
#----------POSITIVE AND NEGATIVE FROM THE COUNTRIES WITH THE TOP CASES
df_sentiment_columns = ['positive_tweets','negative_tweets']
df_sentiment = pd.DataFrame()
#columns=df_sentiment_columns
df_sentiment['Country'] = df['CountryOther'].head(20)
df_sentiment['positive'] = 1*'0'
df_sentiment['positive'] = df_sentiment['positive'].astype('int')
df_sentiment['negative'] = 1*'0'
df_sentiment['negative'] = df_sentiment['positive'].astype('int')



#print(df_sentiment)
#----------authentication needed for twitter
auth = tweepy.OAuthHandler(config.api_key,config.api_secret)
auth.set_access_token(config.access_token,config.token_secret)
api = tweepy.API(auth)
class MyStreamListener(tweepy.StreamListener):
    #this method is called everytime there is a tweet'
    #basically everytime we see a hashtag, increment each hashtag counter by 1

    blob = ""
    def on_status(self,status):
        self.blob = TextBlob(status.text)

        #streamed_dict[x] += self.blob.sentiment.polarity
        for x in list(df_sentiment['Country']):
            if x in status.text:
                if (self.blob.sentiment.polarity) > 0:
                    
                    for i, row in df_sentiment.iterrows():
                        if row['Country'] == x:
                            df_sentiment.at[i,'positive'] += 1
             

                else:
                    for i, row in df_sentiment.iterrows():
                        if row['Country'] == x:
                            df_sentiment.at[i,'negative'] += 1
              
        
    def on_error(self, status_code):
        if status_code == 420:
            print("ERRORRRRR")
            return False


figs  = plt.figure()
figs.suptitle('+ve and -ve tweets Top coutries with corona', fontsize=14, fontweight='bold')
ax1 = figs.add_subplot()
ax1.get_xaxis().set_visible(False)
cmap = cm.get_cmap('Spectral')


def animate(i):
    ax1.cla()
   
    for k, v in df_sentiment[['Country','positive']].iterrows():
        ax1.annotate(str(v['Country'] ) ,v ,xytext=(10,-5), textcoords='offset points',family='sans-serif', fontsize=8,rotation=50)

    ax1.scatter(list(df_sentiment['Country']),list(df_sentiment['positive']),label='positive',zorder=1)

    for k, v in df_sentiment[['Country','negative']].iterrows():
        ax1.annotate(str(v['Country']) ,v ,xytext=(10,-5), textcoords='offset points',family='sans-serif', fontsize=8,rotation=50)

    ax1.scatter(list(df_sentiment['Country']),list(df_sentiment['negative']),label='negative',zorder=2)
    plt.legend(loc='upper right')


my_stream_listener = MyStreamListener()

countries = list(df_sentiment['Country'])
my_stream = tweepy.Stream(auth, listener=my_stream_listener)
my_stream.filter(track=countries,is_async=True)

#basically after a certain amount of seconds, update my graph
ani = animation.FuncAnimation(figs, animate, interval=500)
plt.show()
animate(5)
