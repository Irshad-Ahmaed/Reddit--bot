import logging
import os

# Ensure the logs directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging settings
logging.basicConfig(
    filename='logs/bot_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a reusable logger
logger = logging.getLogger('RedditBotLogger')
