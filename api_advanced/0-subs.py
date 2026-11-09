#!/usr/bin/python3
"""Query the Reddit API for the number of subscribers of a subreddit."""
import requests

base = "https://www.reddit.com"
headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/nissi15)"}


def number_of_subscribers(subreddit):
    """Return the total number of subscribers of a subreddit, or 0."""
    url = "{}/r/{}/about.json".format(base, subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        return data.get("subscribers")
    else:
        return 0
