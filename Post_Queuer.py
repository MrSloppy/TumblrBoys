__author__ = 'Timo'

import pytumblr
import glob

# https://github.com/tumblr/pytumblr        GOOD SHIT RIGHT THERE


# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    #I know....
    'XjZYePrr0GIg6yf9RCnaLl4EGswwMAdQn4GLufxDx9ccS9wjv6',
    '3msUdYmztwXP7eSf0FJ7XKvRiqwWtBE5SvtOLQe97laqQNo7AK',
    'ovtLFGpkNjASKc9eE4A6bT1SF7shUdxIoJLN8Tu1t9m90JxyAu',
    'zVCf3HQ4CTD214ntxM4hcR36OAg8QnU2lTlG2mdvTlJgKXH8XF'
)

# Make the request
print(client.info())
print(client.blog_info("classiccadillacs"))
print(client.blog_info("thickhentaimilfs"))

print(glob.glob("C:\webimages/4chan/e/1808637/*"))
images = glob.glob("C:\webimages/4chan/e/1808637/*")
for i in range(0, len(images)):
    client.create_photo('thickhentaimilfs', state="queue", tags=["thick", "hentai", "milf", "hentai-milf"], data=images[i])