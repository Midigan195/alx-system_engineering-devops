#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'linux:0x16.api:v1.0.0 (by /u/midigan)'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=user_agent)
    results = response.json()

    results = results.get('data').get('subscribers')
    if results is not None:
        return results
    else:
        return 0
