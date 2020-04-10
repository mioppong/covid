
# COVID-19 
There are two files to this project covid.py and covid2.py, covid.py gets the top countries with top cases with the world, and covid2.py gets those top countries, and streams tweets on what people are saying about them. Positive and negative, to see if there are more positie or negativr tweets coming in on a certain country

## Getting Started
* Download files and unzip them
* there shold be 2 files one covid.py and covid2.py and a folder named ENV
* you will need to have virtualenv installed, https://pypi.org/project/virtualenv/
* for running the second file, you will need a twitter account, then receice an api key secret..., then save it in another python file, then import it

## Running program
* go into the project folder
* if virtualenv is installed properly, you should be able to use the command 'source'

```
source ENV/bin/activate
python covid.py
```

* Open another terminal, for the second file

```
source ENV/bin/activate
python covid2.py
```

## Future Work
* I i hope to analyze the tweets coming in, and analyze them for sarcasm just in case for false positive, and vice versa

## Acknowledgments
* twitter api


## Author
* Michael Oppong