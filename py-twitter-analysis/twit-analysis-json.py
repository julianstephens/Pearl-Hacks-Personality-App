from __future__ import print_function
import tweepy
import json
import sys
from watson_developer_cloud import PersonalityInsightsV3
from os.path import join, dirname


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

    return alltweets

def store_tweets(alltweets,file='tweets.json'):
    tweet_list=[]

    for tweet in alltweets:

        tweet_information=dict()

        tweet_information['content']=tweet.text

        tweet_information['contenttype']="text/plain"

        tweet_list.append(tweet_information)

    tweet_data=dict()
    tweet_data["contentItems"] = tweet_list

    file_des=open(file,'w')

    json.dump(tweet_data,file_des,indent=4,sort_keys=True)

    file_des.close()


if __name__ == '__main__':
    alltweets=get_all_tweets(sys.argv[1])

    if len(sys.argv[2])>0:
        store_tweets(alltweets,sys.argv[2])
    else :
        store_tweets(alltweets)



personality_insights = PersonalityInsightsV3(
  version='2017-10-13',
  username='a1e78119-98e6-4c30-a6f2-8529024c5e72',
  password='cdX0Oz3yUD3C'
)

with open(join(dirname(__file__), './watson.json')) as profile_json:
  profile = personality_insights.profile(
    profile_json.read(), content_type='application/json',
    raw_scores=True, consumption_preferences=True)

file_des=open('./profile.json','w')
json.dump(profile, file_des, indent=2)
file_des.close()

data = json.load(open('profile.json'))

print("")
print('\x1b[6;30;42m' + "Big 5 Personality Traits - Percentile:" + '\x1b[0m')
print("")
print("Openness: ", str(round((data["personality"][0]["percentile"]), 2) * 100), "%")
print("Conscientiousness: ", str(round((data["personality"][1]["percentile"]), 2) * 100), "%")
print("Extraversion: ", str(round((data["personality"][2]["percentile"]), 2) * 100), "%")
print("Agreeableness: ", str(round((data["personality"][3]["percentile"]), 2) * 100), "%")
print("Neuroticism: ", str(round((data["personality"][4]["percentile"]), 2) * 100), "%")

print("")
print('\x1b[6;30;42m' + "Environmental Preferences - Percentile:" + '\x1b[0m')
print("")
print("Challenge: ", str(round((data["needs"][0]["percentile"]), 2) * 100), "%")
print("Closeness: ", str(round((data["needs"][1]["percentile"]), 2) * 100), "%")
print("Curiosity: ", str(round((data["needs"][2]["percentile"]), 2) * 100), "%")
print("Excitement: ", str(round((data["needs"][3]["percentile"]), 2) * 100), "%")
print("Ideal: ", str(round((data["needs"][4]["percentile"]), 2) * 100), "%")
print("Liberty: ", str(round((data["needs"][5]["percentile"]), 2) * 100), "%")
print("Love: ", str(round((data["needs"][6]["percentile"]), 2) * 100), "%")
print("Practicality: ", str(round((data["needs"][7]["percentile"]), 2) * 100), "%")
print("Self-expression: ", str(round((data["needs"][8]["percentile"]), 2) * 100), "%")
print("Stability: ", str(round((data["needs"][9]["percentile"]), 2) * 100), "%")
print("Structure: ", str(round((data["needs"][10]["percentile"]), 2) * 100), "%")

print("")