import requests
import creds


# Render content from webpage by making a request
request = requests.get(creds.url)

# Get a dictionary with data 
content = request.json()

# Access article titles and description  
for article in content["articles"]:  
    print(article["title"])
    print(article["description"])