import requests
from bs4 import BeautifulSoup

page = requests.get("https://realpython.com/python-gil/")

# Function to remove tags
def remove_tags(html):

    # parse html content
    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['script', 'img', 'a', 'figure', "form", "head"]):
        # Remove tags
        data.decompose()

    # return data by retrieving the tag content
    return (soup)


# Print the extracted data
print(remove_tags(page.content))