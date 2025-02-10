import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
INCREASE_PERCENTAGE = 0.4
DECREASE_PERCENTAGE = -5
STOCK = input("Enter a stock:\n")
COMPANY_NAME = "Tesla Inc"
API_KEY = os.environ.get('STOCK_API_KEY')
PARAMETERS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': API_KEY,
}
PARAM = {
    'qInTitle': COMPANY_NAME,
    'apikey': os.environ.get('API_KEY'),
}
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
END_POINT = 'https://www.alphavantage.co/query?'
ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(END_POINT, PARAMETERS)
data = stock_response.json()
print(data)
daily_data = data["Time Series (Daily)"]
list_daily_data = list(daily_data.items())
yesterday_price = list_daily_data[0][1]['4. close']
day_before_price = list_daily_data[1][1]['4. close']
# price increase
percentage_difference = ((float(yesterday_price) - float(day_before_price)) / float(day_before_price)) * 100

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_response = requests.get(NEWS_ENDPOINT, PARAM)
news_data = news_response.json()
list_of_articles = news_data['articles']
news = list_of_articles[0:3]


def send_message(index, emoji):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        from_=os.environ.get('from'),
        body=f"""
            {STOCK}: {emoji}{round(percentage_difference, 2)}%
            \nHeadline: {news[index]['title']}. 
            \nBrief: {news[index]['description']}.{news[index]['url']}
            """,
        to=os.environ.get('to')
    )


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
if percentage_difference >= INCREASE_PERCENTAGE:
    for i in range(0, 3):
        send_message(index=i, emoji='🟩')
elif DECREASE_PERCENTAGE <= percentage_difference < 0:
    for i in range(0, 3):
        send_message(index=i, emoji='🔻')
elif DECREASE_PERCENTAGE < 0:
    for i in range(0, 3):
        send_message(index=i, emoji='🔻')


def send_message():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        from_=os.environ.get('from'),
        body="Hello to you too!",
        to=os.environ.get('to')
    )

