# Reddit Bot with Groq AI Integration

This Reddit bot automatically posts content and comments on posts using Groq AI for content generation. It also supports scheduled posting and commenting.

## 📦 Project Structure
```
.
├── .env                 # Environment variables (API keys, credentials)
├── main.py             # Main entry point for the bot
├── scheduler.py        # Scheduler for daily posting and commenting
├── reddit_client.py    # Reddit API integration using PRAW
├── groq_client.py      # Groq AI API integration
├── logger.py           # Logging setup for error handling and debugging
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── .venv               # Virtual environment (optional)
```

---

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone <repo-url>
cd <repo-folder>
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # (Linux/Mac)
.\.venv\Scripts\activate  # (Windows)
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File
Create a `.env` file in the root folder and add the following:
```plaintext
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
USER_AGENT=your_bot_name
GROQ_API_KEY=your_groq_api_key
POST_TIME=16:00
```

### 5. Run the Bot
```bash
python main.py
```

---

## 📦 Features
- **Automated Posting**: Posts content daily at a specified time.
- **Commenting Feature**: Posts comments on the latest posts in a subreddit.
- **Groq AI Integration**: Content and comment generation using Groq AI.
- **Scheduler Integration**: Automated posting and commenting at scheduled times.
- **Error Handling with Logging**: Logs errors and activities for better traceability.

---

## ✅ Customization
- **Change Posting Time:** Modify the `POST_TIME` in the `.env` file.
- **Subreddit Selection:** Change the subreddit name in `reddit_client.py`.
- **Logging Configuration:** Customize the `logger.py` file for more detailed logging.

---