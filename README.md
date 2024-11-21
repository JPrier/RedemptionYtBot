# RedemptionYtBot

A bot to download new videos uploaded by given channels onto youtube, edits them, and then uploads them to a new channel

## Setup

### Step 1: Get Youtube API Keys

1. Navigate to [Google's Credential Creation Dashboard](https://console.cloud.google.com/apis/credentials)
2. Create an OAuth2 key -- Used for uploading videos
3. Create an API key -- Used for requesting data like video uploads from a channel

### Step 2: Create an AWS account and Setup local development

**AWS**
1. Navigate to [AWS Console](https://console.aws.amazon.com/console/home) and create a new account for this service

**Local**
1. Install [python and pip](), and [pipenv](https://pipenv.pypa.io/en/latest/)
2. Install [cdk]() and [npm]()

### Step 3: Deploy

1. `npm run cdk-deploy`
