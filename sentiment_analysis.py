# Nov 14 2018
# Filip Durca
# This program computes the average sentiment of tweets based on timezone

# This definition takes in user input and calculates the volume of a cube with the given parameters
# @param tweetFile the name of the file containing the tweets
# @param keywordFile the name of the file containing the keywords
# @return a list of tuples containing the average sentiment and the amount of tweets per region
def compute_tweets(tweetFile,keywordFile):
    #Variables
    keyword = {}
    easternTweets = 0
    centralTweets = 0
    mountainTweets = 0
    pacificTweets = 0
    easternSentiment = 0
    centralSentiment = 0
    mountainSentiment = 0
    pacificSentiment = 0

    #test
    test1 = 0

    #Try opening the files
    try:
        tweets = open(tweetFile,"r",encoding="utf‐8")
    except IOError as e:
        print(tweetFile," can not be found")
        return []

    try:
        keywordF = open(keywordFile,"r",encoding="utf‐8")
    except IOError as e:
        print(keywordFile," can not be found")
        return []

    #Create dictionary of the keywords
    for line in keywordF:
        line = line.rsplit()
        textLine = line[0].split(",")
        textLine[1] = int(textLine[1])
        keyword[textLine[0]] = textLine[1]

    # Close the keyword text
    keywordF.close()

    #Go through the tweets
    for line in tweets:

        #Test
        test1 = test1+1

        # Reset variables
        tweet = []
        # Split the line to get the co ordinates and the tweet itself
        textLine = line.rsplit()

        # Co ordinates
        xpoint = removePuncFloat(textLine[0])
        ypoint = removePuncFloat(textLine[1])

        # If the Co-ordinates fit, analyze the text
        if xpoint <= 49.189787 and xpoint >= 24.660845 and ypoint <= -67.444574 and ypoint >= -125.242264:

            #Reset variables
            sentiment = 0
            keywordsInTweet = 0

            #Isolate the Tweet
            for i in range(5, len(textLine)):
                tweet.append(textLine[i])

            #Check if any key words are in the
            for word in tweet:
                tweetWord = removePunc(word)
                tweetWord = tweetWord.lower()
                if tweetWord in keyword:
                    sentiment = sentiment + int(keyword.get(tweetWord))
                    keywordsInTweet += 1

            #Dont add the tweet if it has no key words, or add it to the right timezone
            if sentiment > 0:
                #Get the score
                sentiment = sentiment/keywordsInTweet
                #Eastern
                if ypoint >= -87.518395:
                    easternTweets+=1
                    easternSentiment+=sentiment
                #Central
                elif ypoint >= -101.998892:
                    centralTweets+=1
                    centralSentiment+=sentiment
                #Mountain
                elif ypoint >= -115.236428:
                    mountainTweets+=1
                    mountainSentiment+=sentiment
                #Pacific
                elif ypoint >= -125.242264:
                    pacificTweets+=1
                    pacificSentiment+=sentiment

    # Close the file
    tweets.close()

    #test
    print(easternSentiment)
    print(centralSentiment)
    print(mountainSentiment)
    print(pacificSentiment)

    #Do the final compilation of all the data
    if easternSentiment != 0:
        easternSentiment = easternSentiment/easternTweets
    if centralSentiment != 0:
        centralSentiment = centralSentiment/centralTweets
    if mountainSentiment != 0:
        mountainSentiment = mountainSentiment/mountainTweets
    if pacificSentiment != 0:
        pacificSentiment = pacificSentiment/pacificTweets

    #Create the list of tuples
    eastern = (easternSentiment, easternTweets)
    central = (centralSentiment, centralTweets)
    mountain = (mountainSentiment, mountainTweets)
    pacific = (pacificSentiment, pacificTweets)
    result = [eastern,central,mountain,pacific]

    #Return the list
    return result




# This definition removes punctuation from text
# @param str is the string being cleaned of punctuation
# @return result is the string without punctuation
def removePunc(str):
    #Punctuation Set
    punctuation = "!@#$%^&*()_+-=[].{};:'|,/?><`~"
    result = ""

    #Check every character for punctuation
    for char in str:
        if char not in punctuation and char != '"':
            result = result + char
    return result


# This definition removes punctuation from text
# @param str is the string being cleaned of punctuation
# @return result is the string without punctuation
def removePuncFloat(str):
    #Punctuation Set
    punctuation = "[],"
    result = ""

    #Check every character for punctuation
    for char in str:
        if char not in punctuation:
            result = result + char
    return float(result)
