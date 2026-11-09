#!/usr/bin/python3
"""Recursively count keywords in the titles of all hot posts of a subreddit."""
import requests

base = "https://www.reddit.com"
headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/nissi15)"}


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the keywords found in all hot post titles.

    Each call fetches one page of posts, adds the keyword counts for its
    titles to counts, then calls itself with the "after" value to fetch the
    next page. When there are no more pages, the results are printed.
    """
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = "{}/r/{}/hot.json".format(base, subreddit)
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data")
    for post in data.get("children"):
        title_words = post.get("data").get("title").lower().split()
        for word in counts:
            counts[word] += title_words.count(word)

    next_page = data.get("after")
    if next_page is not None:
        count_words(subreddit, word_list, next_page, counts)
        return

    lower_list = []
    for word in word_list:
        lower_list.append(word.lower())

    results = []
    for word in counts:
        total = counts.get(word) * lower_list.count(word)
        if total > 0:
            results.append((word, total))

    results.sort(key=lambda item: (-item[1], item[0]))
    for word, total in results:
        print("{}: {}".format(word, total))
