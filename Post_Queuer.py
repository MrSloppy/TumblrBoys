__author__ = 'Timo'

import pytumblr
import glob

# https://github.com/tumblr/pytumblr        GOOD SHIT RIGHT THERE

consumer_key = input("What is your consumer key?")
consumer_secret = input("What is your consumer secret?")
OAUTH_token = input("What is your OAUTH token?")
OAUTH_secret = input("What is your OATH secret?")

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    #I know....
    consumer_key,           # Consumer Key
    consumer_secret,        # Consumer Secret
    OAUTH_token,            # OAUTH token
    OAUTH_secret            # OAUTH Secret
)

# Make the request
print(client.info())
print(client.blog_info("classiccadillacs"))
print(client.blog_info("thickhentaimilfs"))

print(glob.glob("C:\webimages/4chan/e/1808637/*"))
images = glob.glob("C:\webimages/4chan/e/1808637/*")
for i in range(0, len(images)):
    client.create_photo('thickhentaimilfs', state="queue", tags=["thick", "hentai", "milf", "hentai-milf"], data=images[i])
