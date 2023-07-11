import requests

# Send the GET request to the API
api_url = "https://api.coingecko.com/api/v3/news"
import requests

def get_formatted_news_data(api_url):
    response = requests.get(api_url)
    data = response.json()
    formatted_data = format_data(data)
    return formatted_data

def format_data(data):
    formatted_data = []
    for item in data['data']:
        formatted_item = {
            'Title': item['title'],
            'Description': item['description'],
            'Author': item['author'],
            'URL': item['url'],
            'Updated At': item['updated_at'],
            'News Site': item['news_site'],
            'Thumbnail': item['thumb_2x']
        }
        formatted_data.append(formatted_item)
    return formatted_data

def display_news_data(news_data):
    for item in news_data:
        print("Title:", item['Title'])
        print("Description:", item['Description'])
        print("Author:", item['Author'])
        print("URL:", item['URL'])
        print("Updated At:", item['Updated At'])
        print("News Site:", item['News Site'])
        print("Thumbnail:", item['Thumbnail'])
        print()

# Send the GET request to the API
api_url = "https://api.coingecko.com/api/v3/news"
formatted_data = get_formatted_news_data(api_url)
display_news_data(formatted_data)
