# Nov 14 2018
# Filip Durca
# This program asks the user for the name of the files containing the tweets and the keywords, and then outputs the results from each timezone

#imports
import sentiment_analysis

#Variables
timezones = ["Eastern", "Central", "Mountain", "Pacific"]

#Ask the user for the file names
tweetFile = input("What file are the tweets located in? ")
keywordFile = input("What file are the keywords located in? ")

#Get the results
results = sentiment_analysis.compute_tweets(tweetFile, keywordFile)

#Print the results only if file is found
if len(results) > 0:
    for i in range(4):
        print("Timezone:", timezones[i])
        print("Average:", results[i][0]," Number of tweets:", results[i][1])
