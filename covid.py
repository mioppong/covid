import config
import pycountry
import matplotlib.pyplot as plt
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

filename = 'data.pkl'
df.to_pickle(filename)

plt.legend()
plt.show()


