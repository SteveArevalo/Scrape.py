# Scrape.py

Hacker News Web Scraper
This Python script is a web scraper that extracts and displays top stories from the Hacker News website. It uses the requests library to fetch web pages and the BeautifulSoup library to parse and extract information from the HTML content.

Features:
Fetches top stories from the first and second pages of the Hacker News website.
Parses and extracts story titles, links, and the number of votes.
Filters and displays stories with more than 99 votes.
Sorts stories in descending order based on the number of votes.
Getting Started
To run the Hacker News Web Scraper, follow these steps:

Clone the repository to your local machine:
git clone https://github.com/yourusername/hacker-news-web-scraper.git

Navigate to the project directory:
cd hacker-news-web-scraper

Install the required libraries if you haven't already:
pip install requests
pip install beautifulsoup4

Run the script:
python hacker_news_scraper.py

Usage:
Upon running the script, it will fetch and display the top stories from the first and second pages of the Hacker News website. The displayed stories include titles, links, and the number of votes. Stories with more than 99 votes are filtered and sorted in descending order.

Libraries Used:
Requests - Used to make HTTP requests.
Beautiful Soup - Used for parsing and extracting data from HTML content.
Contributing
Contributions to improve the functionality or add new features are welcome. You can fork the repository and submit a pull request to suggest changes.

License:
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute this code as needed.
Enjoy using the Hacker News Web Scraper! If you have any questions or suggestions, please feel free to reach out to the project owner.
