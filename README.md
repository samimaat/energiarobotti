# Energiarobotti
Energiarobotti ("Energy robot") is a Twitter bot that shares energy saving tips.

The bot in action over on Twitter: [@energiarobotti](https://twitter.com/energiarobotti). (Starting on 10th of October 2022.)

## How did I do it?

I plan to release blog posts detailing how I did the bot on my website [samimaatta.fi](https://samimaatta.fi). I used extensively [Aaron Jack's Twitter bot building video](https://youtu.be/83o6rU5XArs). It is a bit outdated already, but the general ideas hold. Hardest parts are getting the Twitter developer account and Google's APIs to work. 😂

## Caveat about the code

The submitted repo is only the backbones of the code. It includes dummy values for keys and tokens to access Twitter's and Google's APIs. Change those to your own and you have a working Python script, which tweets random tweets from your Google Sheets.

## Technologies

Python scripts with Twitter and Google APIs. The script now live in Google Cloud and is run by Google Scheduler. Google Sheets is used to store the tweets and sources.

## Source of tweets

Source of tweets is the Google Sheets [energiansaastovinkkeja](https://docs.google.com/spreadsheets/d/1Pmzry74c2fWzGF3VC-BzCBOQfViTZIoKbXPqa0DLymg/edit?usp=sharing).
