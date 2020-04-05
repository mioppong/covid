import tweepy
import config
import pycountry
from pprint import pprint
import tweepy
import matplotlib.pyplot as plt, mpld3
from textblob import TextBlob
from bs4 import BeautifulSoup
import pandas as pd
import requests
from matplotlib import cm


#----------SCRAPING ON WEBSITE BELOW TO FIND TOP COUNTRIES DEALING WITH CORONA
URL = 'https://www.worldometers.info/coronavirus/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
columns = ['CountryOther', 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered', 'ActiveCases', 'SeriousCritical','9','10','11','12']
df = pd.DataFrame(columns=columns)


table = soup.find('table', attrs={'id':'main_table_countries_today'}).tbody
trs = table.find_all('tr')

for tr in trs:
    tds = tr.find_all(['th','td'])
    row = [td.text.replace('\n', '') for td in tds]
    df = df.append(pd.Series(row,index=columns), ignore_index=True)


#----------ABOUT TO PLOT THE TOP CORONA CASES VS DEATHS ON A LOGARITHMITIC SCALE
df = df[['CountryOther', 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered', 'ActiveCases', 'SeriousCritical']]
df = df.drop([0])
df = df.head(20)
annoying_characters = ',+'
df['TotalCases'] = df['TotalCases'].str.replace(annoying_characters, '').astype(float)
df['TotalDeaths'] = df['TotalDeaths'].str.replace(annoying_characters, '').astype(float)

#print(df.head(10))


fig, ax = plt.subplots()
cmap = cm.get_cmap('Spectral')

df.plot(x='CountryOther',y='TotalCases',ax=ax,kind='bar',log=True,zorder=1)
for k, v in df[['CountryOther','TotalCases']].iterrows():
    ax.annotate(str(v['CountryOther'] +'-'+ str(v['TotalCases']) ) ,v, xytext=(10,-5), textcoords='offset points',family='sans-serif', fontsize=8,rotation=50)

ax.get_xaxis().set_visible(False)

df.plot(x='CountryOther',y='TotalDeaths',ax=ax,kind='scatter', linewidth=0, c=range(len(df)), colormap=cmap,zorder=2,label='TotalDeaths')
for k, v in df[['CountryOther','TotalDeaths']].iterrows():
    ax.annotate(str(v['CountryOther'] +'-'+ str(v['TotalDeaths']) ) ,v, xytext=(10,-5), textcoords='offset points',family='sans-serif', fontsize=8,rotation=50)


#-------------------------------------------------------------------------------------------


#----------IN THIS SECTION I AM GOING TO STREAM TWEETS,
#----------POSITIVE AND NEGATIVE FROM THE COUNTRIES WITH THE TOP CASES
df_sentiment_columns = ['positive_tweets','negative_tweets']
df_sentiment = pd.DataFrame()
#columns=df_sentiment_columns
df_sentiment['Country'] = df['CountryOther'].head(10)
df_sentiment['positive'] = 1*'0'
df_sentiment['positive'] = df_sentiment['positive'].astype('int')
df_sentiment['negative'] = 1*'0'
df_sentiment['negative'] = df_sentiment['positive'].astype('int')



print(df_sentiment)
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
        streamed_dict[x] += self.blob.sentiment.polarity
        document = list(status.text)
        response = client.analyze_sentiment(inputs=document)[0]
        tweet = TextBlob
        for x in countries:
            if x in status.text:
                print(x)

                print(response.sentiment)
        
    def on_error(self, status_code):
        if status_code == 420:
            print("ERRORRRRR")
            return False

#----------CONTAINS A LIST OF ALL THE COUNTRIES IN THE WORLD
countries = []
for x in list(pycountry.countries):
    countries.append(x.name)
#----------CONTAINS A LIST OF ALL THE COUNTRIES IN THE WORLD

my_stream_listener = MyStreamListener()

#my_stream = tweepy.Stream(auth, listener=my_stream_listener)
#my_stream.filter(track=countries,is_async=True)


#y_vals = list(range(0,len(countries)))    
#plt.plot(countries,y_vals,mec='w',mew=5,ms=20)




#plt.show()
#mpld3.show()


#def later():

      #  def animate(i):
       # ax1.cla()
       # plt.tight_layout()
       # ax1.set_ylabel("y axis",fontsize=0.5)
       # ax1.plot(list(streamed_dict.values()),list(streamed_dict.keys()))

    #my_stream_listener = MyStreamListener()

    #---------- we just get first and last name 
    #----------of player and store it in players
    #with open("prediction.txt") as f:
     #   for text in f:
      #      player_name,dont,care = text.partition('\n')
       #     players.append(player_name)

    #my_stream = tweepy.Stream(auth, listener=my_stream_listener)
    #my_stream.filter(track=players,is_async=True)

    #basically after 500ms, update my graph
    #ani = animation.FuncAnimation(fig, animate, interval=100)
    #plt.show()
    #animate(2)
    # 
#plt.legend()
#plt.show()