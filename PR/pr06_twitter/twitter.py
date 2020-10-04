"""Twitter."""
import re


class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets


def find_fastest_growing(tweets: list) -> Tweet:
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    >Tweet1 is 32.5 hours old and has 64 retweets.
    >Tweet2 is 3.12 hours old and has 30 retweets.
    >64/32.5 is smaller than 30/3.12 -> tweet2 is the faster growing tweet.

    :param tweets: Input list of tweets.
    :return: Fastest growing tweet.
    """
    holder = 0
    for tweet in tweets:
        new = tweet.retweets / tweet.time
        if new > holder:
            holder = new
            hot = tweet
    return hot


def sort_by_popularity(tweets: list) -> list:
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet is the more popular one.
    >Tweet1 has 10 retweets.
    >Tweet2 has 30 retweets.
    >30 is bigger than 10 -> tweet2 is the more popular one.

    :param tweets: Input list of tweets.
    :return: List of tweets by popularity
    """
    tweets.sort(key=lambda x: x.time)
    tweets.sort(key=lambda x: x.retweets, reverse=True)
    return tweets


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain given hashtag.

    :param tweets: Input list of tweets.
    :param hashtag: Hashtag to filter by.
    :return: Filtered list of tweets.
    """
    filtered = []
    for tweet in tweets:
        if hashtag in tweet.content:
            filtered.append(tweet)
    return filtered


def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    >Tweet1 has 21 retweets and has common hashtag.
    >Tweet2 has 19 retweets and has common hashtag.
    >The popularity of that hashtag is 19 + 21 = 40.

    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """
    hashtags = {}
    sorted_hashtags = []
    flipped = {}
    bruh = []
    for tweet in tweets:
        text = tweet.content
        pattern = r"#\w+"
        match = re.search(pattern, text)
        if match:
            if match.group() in hashtags:
                hashtags[match.group()] += tweet.retweets
            else:
                hashtags[match.group()] = tweet.retweets
    for key, value in hashtags.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    for k, v in flipped.items():
        v.sort()
    sorted_hashtags = sorted(flipped.items(), key=lambda x: x[0], reverse=True)
    print(sorted_hashtags)
    for value in sorted_hashtags:
        for hashtag in value[1]:
            bruh.append(hashtag)
    return bruh
