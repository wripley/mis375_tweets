from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="KgPmaQ4I76nRJTG8G8vEvSao1"
csecret="W5XSIdHwwrS8jarsVn6uGIsJzoLoQRhszPmRnd2tbwWqjrBn4s"
atoken="1499855006-kL23bz7O2BuZ6TNoOnfTLxQbfScQIwuT6zrnYCe"
asecret="3D2t06ugN1bK8d1MS2T2iIVadQSMdAHgLG3bXcMeZl0RQ"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Activision", "Blizzard_Ent", "King_Games", "Skylanders", "Call of Duty", "Starcraft", "Tony Hawk's Pro Skater"])
