import feedparser

# Define the RSS feed URL
rss_url = "https://www.bunnieabc.com/index.xml"

# Parse the RSS feed and extract the latest post
feed = feedparser.parse(rss_url)
latest_post = feed.entries[0]

# Write the link of the latest post to the file
with open('src/latest_post.txt', 'w') as f:
    f.write(latest_post.link)
