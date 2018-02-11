import tweepy
import csv
import cgi


formData = cgi.FieldStorage()
handle = formData.getValue('twitterHandle')

#Twitter API credentials
consumer_key = "dbSAIyGFIVmCQTckXSP0QpyHk"
consumer_secret = "1KfzU1srmAgb1yzaNZFwfStFVczmQj1aIG8CoWwQFTrgjF9w4m"
access_key = "810846719529385984-lzuk5LHjboOmEaaeJvopS2TaUtgs6zy"
access_secret = "KZYkYZdkbmLvUy3W2hM0PIbPrceyhlGXoBBd0n96h1YSH"


def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)

        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        alltweets.extend(new_tweets)

        oldest = alltweets[-1].id - 1


    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

    pass


if __name__ == '__main__':
    get_all_tweets(handle)