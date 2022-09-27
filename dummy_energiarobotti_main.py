from twitter import *
import gspread
from random import *

# Twitter API keys and tokens as strings (these are dummy strings, does not work).
consumer_key = "string 1"
consumer_secret = "string 2"
token = "string 3"
token_secret = "string 4"

# grspread to access the Google Service account's credentials from a separate file.
gc = gspread.service_account("g_credentials.json")

# Open a sheet from a spreadsheet in one go.
wks = gc.open("energiansaastovinkkeja").sheet1

# Check the amount of rows in the tweets column.
col_len = len(wks.col_values(1))

# Randomize the selection of tweets with rand using number of tweets (col_len).
# Start from row 2, since the first row is a header.
rand = str(randint(2, col_len))

# Reference the specific cell from the first column (A) and row (rand). Turn it into a tweet (string).
tweet = wks.acell("A" + rand).value

# twitter to access the bot account with credentials
t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret)
)

# Tweet the tweet.
t.statuses.update(
    status=tweet
)
