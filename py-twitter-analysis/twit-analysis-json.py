import tweepy #https://github.com/tweepy/tweepy
import json
import sys

#Twitter API credentials
consumer_key = "dbSAIyGFIVmCQTckXSP0QpyHk"
consumer_secret = "1KfzU1srmAgb1yzaNZFwfStFVczmQj1aIG8CoWwQFTrgjF9w4m"
access_key = "810846719529385984-lzuk5LHjboOmEaaeJvopS2TaUtgs6zy"
access_secret = "KZYkYZdkbmLvUy3W2hM0PIbPrceyhlGXoBBd0n96h1YSH"


def get_all_tweets(screen_name):

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    new_tweets = api.user_timeline(screen_name = screen_name,count=199)


    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0:

        new_tweets = api.user_timeline(screen_name = screen_name,count=199,max_id=oldest)

        alltweets.extend(new_tweets)

        oldest = alltweets[-1].id - 1

    # print total tweets fetched from given screen name
    print ("Total tweets downloaded from %s are %s" % (screen_name,len(alltweets)))

    return alltweets

def fetch_tweets(screen_names):

    # initialize the list to hold all tweets from all users
    alltweets=[]

    # get all tweets for each screen name
    for  screen_name in screen_names:
        alltweets.extend(get_all_tweets(screen_name))

    return alltweets

def store_tweets(alltweets,file='tweets.json'):

    # a list of all formatted tweets
    tweet_list=[]

    for tweet in alltweets:

        tweet_information=dict()

        tweet_information['text']=tweet.text.encode('utf-8')

        # date and time at which tweet was created
        tweet_information['created_at']=tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")

        # id of this tweet
        tweet_information['id_str']=tweet.id_str

        # add this tweet to the tweet_list
        tweet_list.append(tweet_information)


    # open file desc to output file with write permissions
    file_des=open(file,'w')

    # dump tweets to the file
    json.dump(tweet_list,file_des,indent=4,sort_keys=True)

    # close the file_des
    file_des.close()


if __name__ == '__main__':

    # pass in the username of the account you want to download
    alltweets=get_all_tweets(sys.argv[1])

    # store the data into json file
    if len(sys.argv[2])>0:
        store_tweets(alltweets,sys.argv[2])
    else :
        store_tweets(alltweets)