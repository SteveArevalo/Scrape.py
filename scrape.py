# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pprint

# Send HTTP requests to retrieve the HTML content of two pages from the Hacker News website
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

# Select elements with class 'titleline' followed by 'a' within the first page
links = soup.select('.titleline > a')

# Select elements with class 'titleline' followed by 'a' within the second page
links2 = soup.select('.titleline > a')

# Select elements with class 'subtext' within the first page
subtext = soup.select('.subtext')

# Select elements with class 'subtext' within the second page
subtext2 = soup.select('.subtext')

# Combine the selected links and subtext from both pages
mega_links = links + links2
mega_subtext = subtext + subtext2

# Define a function to sort a list of stories by the number of votes in descending order
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

# Define a function to create a custom list of Hacker News stories with titles, links, and votes
def create_custom_hn(mega_links, mega_subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

# Pretty print the list of custom Hacker News stories with titles, links, and votes
pprint.pprint(create_custom_hn(links, subtext))
