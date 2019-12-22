import tweepy

CONSUMER_KEY="your consumer key here" 
CONSUMER_SECRET="your consumer secret here"
ACCESS_TOKEN="your access token here"
ACCESS_TOKEN_SECRET="your access token secret here"


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Creation of the actual interface, using authentication
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
# collect tweets on #query
query=input("\t\tenter the query on which tweets is to be collected:")
c=input("\t\tenter the number of tweets collected:")
print("\t\tsearching"+c+"tweets on #"+query)
result=tweepy.Cursor(api.search,q=query,count=c,
                      		lang="en",rpp=100).items()
for tweet in result:
    print (tweet.created_at, tweet.text)
