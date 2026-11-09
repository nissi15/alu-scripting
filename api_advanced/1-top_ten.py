#!/usr/bin/python3
"""Query the Reddit API for the first 10 hot posts of a subreddit."""
import requests

base = "https://www.reddit.com"
headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/nissi15)"}


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    url = "{}/r/{}/hot.json".format(base, subreddit)
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
    else:
        print(None)
