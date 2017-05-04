import tweepy

from user_keys import keys
 
SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['CONSUMER_KEY']
CONSUMER_SECRET = keys['CONSUMER_SECRET']
ACCESS_KEY = keys['ACCESS_KEY']
ACCESS_SECRET = keys['ACCESS_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print "Getting all tweets..."

# Get all tweets for the account
# API is limited to 350 requests/hour per token
# so for testing purposes we do 10 at a time

timeline = api.user_timeline(count = 2500)

print "Found: %d" % (len(timeline))
print "Removing..."
print "Check https://volshebnik.xyz if you want to do it too :)"

# Delete tweets one by one
for t in timeline:
    api.destroy_status(t.id)

print "Twitter timeline removed!"
    
    
