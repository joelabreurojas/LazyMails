# LazyMails

A telegram bot written in Python to send automated emails to remind a lazy teacher that his class exists.

## Usage

**1). Create a virtual environment:**
* `python -m venv env`

**2). Activate the virtual environment:**
* `env\Scripts\activate` or `source env\Scripts\activate`

**3). Install the necessary packages:**
* `pip install -r requirements.txt`

**4). Create a .env file for the bot**
* `BOT_TOKEN=<YOUR_BOT_TOKEN>`
* `BOT_USERNAME=<YOUR_BOT_USERNAME>`

* `MAIL_USERNAME=<YOUR_EMAIL>`
* `MAIL_PASSWORD=<YOUR_EMAIL_TOKEN>`
* `MAIL_SERVER=<YOUR_SERVER>`
* `MAIL_PORT=<YOUR_PORT>`

**5). Run:**
* `python run.py` or `python -m lazymails`
