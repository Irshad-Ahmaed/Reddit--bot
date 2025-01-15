from groq_client import generate_groq_content
from reddit_client import post_to_reddit

# Test Title and Content Generation
title = "Test Post - Checking Bot Functionality"
content = generate_groq_content()

# Print content to verify locally
print(f"Generated Content: {content}")

# Post to Reddit
post_to_reddit(title, content)
print("✅ Test post has been submitted!")
