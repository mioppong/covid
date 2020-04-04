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

cmap = cm.get_cmap('Spectral')




URL = 'https://www.worldometers.info/coronavirus/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
columns = ['CountryOther', 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered', 'ActiveCases', 'SeriousCritical','9','10']
df = pd.DataFrame(columns=columns)


table = soup.find('table', attrs={'id':'main_table_countries_today'}).tbody
trs = table.find_all('tr')

for tr in trs:
    tds = tr.find_all(['th','td'])
    row = [td.text.replace('\n', '') for td in tds]
    df = df.append(pd.Series(row,index=columns), ignore_index=True)
 
df = df.head(20)
#plt.plot(df['CountryOther'],df['TotalCases'])
#df['TotalCases'] = df['TotalCases'].astype('float64')
df['TotalCases'] = df['TotalCases'].str.replace(',', '').astype(float)

fig, ax = plt.subplots()

df.plot(x='CountryOther',y='TotalCases',ax=ax,kind='scatter',s=120, linewidth=0, 
        c=range(len(df)), colormap=cmap)
for k, v in df[['CountryOther','TotalCases']].iterrows():
    #print((v['TotalCases']))

    ax.annotate(str(v['CountryOther'] +'-'+ str(v['TotalCases']) ) ,v, xytext=(10,-5), textcoords='offset points',
                family='sans-serif', fontsize=10, color='darkslategrey',rotation=40)

    ax.get_xaxis().set_visible(False)

plt.show()
#fig.canvas.draw()
#mpld3.show()
#-------------------------------------------------------------------------------------------

#authentication needed for twitter
auth = tweepy.OAuthHandler(config.api_key,config.api_secret)
auth.set_access_token(config.access_token,config.token_secret)
api = tweepy.API(auth)
class MyStreamListener(tweepy.StreamListener):
    #this method is called everytime there is a tweet
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