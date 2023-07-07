import json
import os
from django.contrib.staticfiles.storage import staticfiles_storage
import requests
import urllib3.exceptions

from bs4 import BeautifulSoup
from urllib.parse import urlparse


class WebScraper:
    def __init__(self, url):
        self.url = url
    
    def scrape(self):
        response = requests.get(self.url)
        # Perform scraping logic here and return the scraped data
        
        # Example: Saving scraped data to a file
        with open('data.txt', 'w') as file:
            file.write(response.text)
        
        return response.text

    def scrape_links(self):
    # Making a GET request
        r = requests.get(self.url)

        # Parsing the HTML
        soup = BeautifulSoup(r.content, 'html.parser')

        # Find all links in the page
        for link in soup.find_all('a'):
            href = link.get('href')

            if href and not any(x in href for x in self.SPECIAL_CHAR):
                if not href.startswith('http'):
                    href = self.url + '/' + href
                if href.startswith('http'):
                    self.links.append(href)

    def scrape_text_from_url(self, url):
        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'html.parser')

        # Extract all text from the page and split into paragraphs
        all_text = soup.get_text().replace('\n', '').replace('\t', '').replace('\r','').strip()
        all_text = all_text.encode('ascii', 'ignore').decode()

        return all_text

    def scrape_all_text_from_links(self):
        self.main_url_text = self.scrape_text_from_url(self.url)

        self.link_text_dict['main_url'] = {'text': self.main_url_text}

        # Loop through all links
        for link in self.links:
            # Making a GET request
            r = requests.get(link)

            # Parsing the HTML
            soup = BeautifulSoup(r.content, 'html.parser')

            # Extract all text from the page and split into paragraphs
            all_text = soup.get_text().replace('\n', '').replace('\t', '').replace('\r','').strip()
            all_text = all_text.encode('ascii', 'ignore').decode()
            # Add the link and text to the dictionary
            parsed_url = urlparse(link)
            key_name = parsed_url.path
            self.link_text_dict[key_name] = {'text': f'{all_text}'}

    def save_to_json(self, file_name):
        self.scrape_links()
        self.scrape_all_text_from_links()

        # Create the folder if it doesn't exist
        folder = os.path.join(os.getcwd(), 'scrapped_json', 'json')
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Write the dictionary to a txt file
        file_path = os.path.join(os.getcwd(), 'scrapped_json','json', file_name)
        with open(file_path, 'w') as f:
            for key, value in self.link_text_dict.items():
                f.write(f"{key}\n")
                f.write(f"{value['text']}\n\n")

        print(f"Link text saved to {file_name} file.")



