__author__ = 'Timo'

import pytumblr

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