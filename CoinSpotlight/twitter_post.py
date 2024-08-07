import feedparser
import tweepy
import random

# Twitter API credentials
consumer_key = '8gaUrdm20V4176RiMYsOUaZh8'
consumer_secret = 'Tgf0ZmQkr2raSFIohDVJqNcVRmrS9kJ57UfVW0CeZJCldhPID2'
access_token = 'lTjYrKqGDgmJ9MIfO1z8mPfaTvki661rAWm65jdYQfJNC'
access_token_secret = 'lTjYrKqGDgmJ9MIfO1z8mPfaTvki661rAWm65jdYQfJNC'

# Set up Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# List of Twitter mentions
mentions = [
    "TheMoonCarl", "APompliano", "Whale_Alert", "Bitcoin_Archive", "RaoulGMI",
    "woonomic", "scottmelker", "aantonop", "elliotrades", "crypto_birb",
    "Bitcoin", "ethereum", "Ripple", "Cardano", "Binance", "Cointelegraph",
    "CoinDesk", "CryptoCom", "CoinMarketCap", "NFTs",
    "VitalikButerin", "cz_binance", "brian_armstrong", "EthereumCommunity", "Crypto_Twitter"
]

def get_relevant_mentions(post_title):
    post_title_lower = post_title.lower()
    
    if "bitcoin" in post_title_lower:
        relevant_mentions = ["Bitcoin", "Cointelegraph", "CryptoCom", "Binance", "TheMoonCarl"]
    elif "xrp" in post_title_lower:
        relevant_mentions = ["Ripple", "Cointelegraph", "woonomic", "CoinMarketCap", "TheMoonCarl"]
    elif "ethereum" in post_title_lower:
        relevant_mentions = ["ethereum", "VitalikButerin", "EthereumCommunity", "CoinDesk", "aantonop"]
    elif "binance" in post_title_lower:
        relevant_mentions = ["Binance", "cz_binance", "CryptoCom", "Cointelegraph", "TheMoonCarl"]
    elif "coinbase" in post_title_lower:
        relevant_mentions = ["Coinbase", "brian_armstrong", "CoinDesk", "CryptoCom", "TheMoonCarl"]
    else:
        relevant_mentions = random.sample(mentions, 5)
    
    return relevant_mentions

try:
    # RSS feed URL
    rss_url = 'https://coinspotlight.net/feed'

    # Parse RSS feed
    feed = feedparser.parse(rss_url)

    # Get the latest post
    latest_post = feed.entries[0]
    post_title = latest_post.title
    post_link = latest_post.link

    # Get relevant mentions
    selected_mentions = get_relevant_mentions(post_title)
    mentions_str = " ".join([f"@{mention}" for mention in selected_mentions])

    # Post to Twitter with relevant mentions
    tweet = f"New post: {post_title} {post_link} {mentions_str}"
    api.update_status(tweet)
    print("Tweet posted successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
