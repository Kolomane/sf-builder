# Name: py_scraper.py
# Purpose: Basic function to webscrape
# Version & Notes: Found at bottom of document
############################################################

import requests
from bs4 import BeautifulSoup

def scraper(url,id):
    # print("Inside SCRAPER")
    # List the URL to scrape
    theURL = f"{url}"
    # Using requests module, get the contents of the webpage
    theRequest = requests.get(theURL)
    # Using BeautifulSoup, parse the webpage
    theSoup = BeautifulSoup(theRequest.content, "html.parser")
    # Get only the relevant content from the webpage
    theContents = theSoup.find_all(id=f"{id}")
    # print("Exiting SCRAPER")
    return(theContents)


############################################################
# Version & Notes ##########################################
############################################################
# Version 0.01
# # Date: 03/26/2023
# # Notes: Initial Upload