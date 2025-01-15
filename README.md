# Reddit Bot with Groq AI Integration

This Reddit bot automatically posts content and comments on posts using Groq AI for content generation. It also supports scheduled posting and commenting.

## 🖼️ Screen Shots
[Screenshot](screenshots/s1.png "Post & Comment")
[Screenshot](screenshots/s2.png "Post & Comment")
[Screenshot](screenshots/s3.png "Log comments while posting")

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Irshad-Ahmaed/Reddit--bot.git
cd Reddit--bot
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
