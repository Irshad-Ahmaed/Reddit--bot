import schedule
import time
from datetime import datetime
from groq_client import generate_groq_content, generate_comment
from reddit_client import post_to_reddit, comment_on_latest_posts
from dotenv import load_dotenv
import os
from logger import logger

# Load environment variables
load_dotenv()

POST_TIME = os.getenv("POST_TIME")
COMMENT_TIME = os.getenv("COMMENT_TIME")

def scheduled_post():
    title = f"Daily Post - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    content = generate_groq_content()
    post_to_reddit(title, content)

def scheduled_comment():
    comment_content = generate_comment()
    comment_on_latest_posts(subreddit_name="test", comment_content=comment_content)

def start_scheduler():
    try:
        schedule.every().day.at(POST_TIME).do(scheduled_post)
        schedule.every().day.at(COMMENT_TIME).do(scheduled_comment)
        logger.info(f"Scheduler started! Posting daily at {POST_TIME}.")
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except Exception as e:
        logger.error(f"Error starting the scheduler: {e}")
