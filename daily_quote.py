import random
from datetime import date


quotes = [
    # Create a list of quotes 
    "I don't know if I told you this, but I'm allergic to bad vibes.",
    "Sorry. I just got nervous thinking about you out there... Digging... And what you might find...",
    "I'm going to try using my muscles to scare away the germs.",
    "I had to work once. It was the worst!",
    "Since I can't cook, I just played Super Chef RPG IV for 24 hours...",
    "Hmmm... There really isn't any news to speak of today.",
    "But we don't do things because they are easy, hm? We do them because they are profitable!"
]

def get_quote_of_the_day(quotes):
    todays_quote = random.choice(quotes)
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /home/hcheng25/windows_home/03-data-structures-hcheng25/daily_quote.py >> /home/hcheng25/windows_home/03-data-structures-hcheng25/daily_quote.txt