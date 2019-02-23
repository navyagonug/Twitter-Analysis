#Importing the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
#These are the Consumer API keys and Access token along with access token secret
access_token = "1094764434743091200-ufXgCjWlZoouKgFhGRxkJkAky6RPQx"
access_token_secret = "pTMNkCg238dQyq8OMix8iFtIzLLJR4wjQYqesNbEVcZAx"
consumer_key = "3W54Vk58CRzii8MJsizc9Fy2T"
consumer_secret = "hDX3pyz7LfRMIeMrIMovdrcXGjyUGaLcoQF2jtdfNxgmEBaaLd"


#This is listener class that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        saveFile = open('/Users/Navya Gonuguntla/Desktop/PB/Twitter_Data.json','a')
        saveFile.write(data)
        saveFile.write('\n')
        saveFile.close()
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: These keywords includes celebrity names such as 'Brad Pitt','Ellen Degeneres'
    stream.filter(track=['Angeline Jolie','Brad Pitt','Kim Kardashian','Rajnikanth','Jennifer Lawrence','Jennifer Aniston','Ellen Degeneres','Portia Derossi','Sharukh Khan','SRK','Salman Khan','Jackie Chan','Will Smith','Jennifer Lopez','Jet Li','Yang Yang','Priyanka Chopra','Deepika Padukone','Kareena Kapoor','Jhonny Depp'])
