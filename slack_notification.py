import feedparser
import requests

# Define the RSS feed URL and Slack webhook URL
rss_url = "https://www.bunnieabc.com/index.xml"
slack_url = "https://hooks.slack.com/services/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"

# Define the notification message format
message_format = "New post published on {blog_title}:\n<{post_url}|{post_title}>"

# Parse the RSS feed and extract the latest post
feed = feedparser.parse(rss_url)
latest_post = feed.entries[0]

# Construct the notification message
message = message_format.format(blog_title=feed.feed.title, post_title=latest_post.title, post_url=latest_post.link)

# Send the notification to the Slack webhook URL
response = requests.post(slack_url, json={"text": message})

# Check the response status code to ensure the notification was sent successfully
if response.status_code == 200:
    print("Notification sent successfully!")
else:
    print("Error sending notification:", response.status_code)
