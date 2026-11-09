# API advanced

Python functions that query the [Reddit API](https://www.reddit.com/dev/api/)
for information about subreddits.

## Files

| File | Description |
| ---- | ----------- |
| `0-subs.py` | Returns the number of subscribers of a subreddit |
| `1-top_ten.py` | Prints the titles of the first 10 hot posts of a subreddit |
| `2-recurse.py` | Recursively returns the titles of all hot posts of a subreddit |
| `3-count.py` | Recursively counts keywords in the titles of all hot posts |

## Notes

- Every request sets a custom `User-Agent`, as Reddit requires.
- Redirects are not followed, so an invalid subreddit (which Reddit
  redirects to a search page) is detected instead of being treated as valid.
- Tasks 2 and 3 use the `after` value from Reddit's pagination to fetch the
  next page by calling the function again, instead of using a loop.

## Requirements

- Python 3
- `requests`
