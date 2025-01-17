import praw
from dotenv import load_dotenv
import os
from logger import logger

load_dotenv()

# Initialize Reddit client with logging
try:
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent=os.getenv("USER_AGENT")
    )
    logger.info("Reddit client initialized successfully.")
except Exception as e:
    logger.error(f"Error initializing Reddit client: {e}")

def post_to_reddit(title, content):
    try:
        subreddit = reddit.subreddit("test")  # Change to your subreddit
        subreddit.submit(title, selftext=content)
        logger.info(f"Post successfully submitted with title: '{title}'")
    except Exception as e:
        logger.error(f"Failed to post to Reddit: {e}")

def comment_on_latest_posts(subreddit_name, comment_content, num_posts=1):
    """Generates and posts comments on the latest posts."""
    try:
        subreddit = reddit.subreddit(subreddit_name)
        for submission in subreddit.new(limit=num_posts):
            submission.reply(comment_content)
            logger.info(f"Commented on post '{submission.title}'")
    except Exception as e:
        logger.error(f"Failed to comment on posts: {e}")