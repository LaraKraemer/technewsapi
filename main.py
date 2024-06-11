import requests
import creds
from send_email import send_email


# Render content from webpage by making a request
request = requests.get(creds.url)

# Get a dictionary with data 
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:5]:
    if article["title"] is not None:
        body = ("Subject: Today's tech news" + "\n"
                + (body + article["title"]
                + "\n" + article["description"]
                + "\n" + article["url"] + 2*"\n"))


body = body.encode("utf-8")
send_email(message=body)