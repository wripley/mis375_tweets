import tweepy
import csv
import re

auth = tweepy.auth.OAuthHandler('KgPmaQ4I76nRJTG8G8vEvSao1', 'W5XSIdHwwrS8jarsVn6uGIsJzoLoQRhszPmRnd2tbwWqjrBn4s')
auth.set_access_token('1499855006-kL23bz7O2BuZ6TNoOnfTLxQbfScQIwuT6zrnYCe', '3D2t06ugN1bK8d1MS2T2iIVadQSMdAHgLG3bXcMeZl0RQ')

api = tweepy.API(auth)
# Open/Create a file to append data
csvFile = open('Warcraft2.csv', 'a')
# Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q="@Warcraft",
                           since="2016-04-03",
                           until="2016-04-15",
                           lang="en").items():
    try:
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    except:
        print("SS")
csvFile.close()
