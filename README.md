# RSS Feed to Slack Notification
This is a Python script that checks an RSS feed for new posts and sends a notification to a Slack channel if a new post is found. The script is designed to be run on a regular basis (e.g., every 30 minutes) using a workflow file in GitHub Actions.

## Getting Started
To use this script, you will need:

* A Slack account with permissions to create a webhook
* An RSS feed that you want to monitor check with your website.
## Setting up Slack
### To set up a Slack webhook, follow these steps:

In Slack, navigate to the channel where you want to receive the notifications
* Click on the gear icon next to the channel name to open the channel settings
* Click on **"Add an app or integration"**
* Search for **"Incoming WebHooks"** and click on it
* Click on **"Add Configuration"**
* Choose the channel where you want to receive the notifications and click on **"Add Incoming WebHooks Integration"**
* Copy the Webhook URL that is generated (_you will need this later_)
### Setting up the RSS feed
To set up the RSS feed, you will need to find an RSS feed URL for the site you want to monitor. This can usually be found by adding "/feed" or *"/index.xml"* to the end of the site's URL **(e.g., https://www.example.com/feed,https://www.example.com/index.xml)**.

## Running the script
* Clone this repository to your local machine
* Install the required dependencies by running `pip install -r requirements.txt`
* Copy the `.env.example` file to a new file named `.env` and set the **SLACK_WEBHOOK_URL** variable to the Webhook URL you copied earlier remeber make sure the `.gitignore` file is correctly set.
* Run the script using python `src/slack_notification.py`
* The script will check for new posts and send a notification to the Slack channel if a new post is found. The script can be run on a regular basis (e.g., every 30 minutes) using a workflow file in GitHub Actions.

## GitHub Actions Workflow
This repository includes a sample workflow file that can be used to run the script on a regular basis using GitHub Actions. The workflow file is located at **.github/workflows/slack_notification.yml**. By default, the workflow is set up to run every 30 minutes.

### To use the workflow, you will need to:

## Set up the RSS feed and Slack webhook as described above
* Create a fork of this repository
* Set the **SLACK_WEBHOOK_URL** secret in your repository settings to the Webhook URL you copied earlier
* Modify the **rss_url** variable in the **slack_notification.py** script to match the RSS feed you want to monitor
* Modify the **message_format** variable in the **slack_notification.py** script to match the format you want for the notification message
* Modify the frequency of the workflow by editing the cron expression in the **slack_notification.yml** file
## License
This script is released under the **MIT License**.
