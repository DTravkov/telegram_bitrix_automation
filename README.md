# Telegram Bot for Bitrix24 Leads Interaction

## Overview
This project introduces a Python Telegram bot designed to interact with leads in Bitrix24. The bot facilitates communication and management of leads directly through Telegram.

## Prerequisites

Before setting up the bot, ensure you have:
- Registered an official Telegram bot via [BotFather](https://t.me/botfather)
- Obtained the bot token from BotFather
- A Bitrix24 webhook URL with sufficient privileges for CRM and tasks methods
- Activate Leads tab in the CRM panel of your Bitrix24

## Installation & Setup

### 1. Clone the Repository
```
git clone <repository-url>
cd <project-directory>
```

### 2. Install UV Package Manager
Install the UV package manager for Python by following the instructions at:  
https://github.com/astral-sh/uv

### 3. Install Dependencies
Open the project folder in your terminal and run:
```
uv sync
```
This will create a `.venv` directory in the project root.

### 4. Configure Environment Variables
Navigate to the `.venv` folder and create an `envar.env` file:
```
cd .venv
touch envar.env
```

Open `envar.env` and populate it with the following variables:
```
BITRIX_URL=URL.TO.YOUR.WEBHOOK
TELEGRAM_API_KEY=TELEGRAM.BOT.TOKEN
CITY_TZ_NAME=PYTZ.PACKAGE.TIMEZONE
```

### 5. Environment Variables Explained

- **BITRIX_URL**: Your Bitrix24 webhook URL (ensure it has CRM and tasks permissions)
- **TELEGRAM_API_KEY**: The token obtained from BotFather for your Telegram bot
- **CITY_TZ_NAME**: Timezone in `pytz` package format (e.g., `'America/New_York'`). This synchronizes time-related functionality in Bitrix with your local timezone.(idk if its needed,but still...)

### 6. Run the Bot
Execute the main script to start the bot:
```
python main.py
```

## Usage
Once the bot is running, send the `/get_leads` command to your registered Telegram bot to test the functionality.

## Notes
- Ensure your Bitrix24 webhook has appropriate permissions for CRM operations and task management
- The timezone string must be a valid `pytz` timezone identifier
- All dependencies are managed automatically by UV during the `uv sync` command

## Troubleshooting
- If `.venv` doesn't appear after `uv sync`, verify you're in the correct project directory
- Ensure all environment variables in `envar.env` are correctly set and formatted
- Check that your Bitrix24 webhook URL is accessible and has the required permissions

## Further possible improvements for the project :
- Drop in some additional error handling / data checks
- Set up logging system
- Improve flexibility of data fetching
- Wrap each file up with descriptive comments


