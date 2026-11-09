#!/usr/bin/python3
"""Recursively query the Reddit API for the titles of all hot posts."""
import requests

base = "https://www.reddit.com"
headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/nissi15)"}


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of the titles of all hot posts of a subreddit, or None.

    Each call fetches one page of posts, adds their titles to hot_list,
    then calls itself with the "after" value to fetch the next page.
    """
    if after is None:
        hot_list = []

    url = "{}/r/{}/hot.json".format(base, subreddit)
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    for post in data.get("children"):
        hot_list.append(post.get("data").get("title"))

    next_page = data.get("after")
    if next_page is None:
        return hot_list
    return recurse(subreddit, hot_list, next_page)
