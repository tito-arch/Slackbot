import feedparser
import requests
import os

# Define the RSS feed URL and Slack webhook URL
rss_url = "https://www.bunnieabc.com/index.xml"
slack_url = os.environ['SLACK_WEBHOOK_URL'] = "https://hooks.slack.com/services/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"


# Define the notification message format
message_format = "New post published on {blog_title}:\n<{post_url}|{post_title}>"

# Parse the RSS feed and extract the latest post
feed = feedparser.parse(rss_url)
latest_post = feed.entries[0]

# Check if the latest post is different from the previous one
with open('latest_post.txt', 'r+') as f:
    previous_post_link = f.read()
    if latest_post.link != previous_post_link:
        # Construct the notification message
        message = message_format.format(blog_title=feed.feed.title, post_title=latest_post.title, post_url=latest_post.link)

        # Send the notification to the Slack webhook URL
        response = requests.post(slack_url, json={"text": message})

        # Check the response status code to ensure the notification was sent successfully
        if response.status_code == 200:
            print("Notification sent successfully!")
            # Write the link of the latest post to the file
            f.seek(0)
            f.write(latest_post.link)
            f.truncate()
        else:
            print("Error sending notification:", response.status_code)
    else:
        print("No new post found.")

#DONE        