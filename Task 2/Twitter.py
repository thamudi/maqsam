from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = "Hello everyone this is running on empty, food review!"
twitter.update_status(status=message)
print("Tweeted: %s" % message)