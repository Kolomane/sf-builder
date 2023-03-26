import requests, django, re
from bs4 import BeautifulSoup

def main():
    theURL = "https://aonsrd.com/Themes.aspx?ItemName=All"
    theRequest = requests.get(theURL)
    theSoup = BeautifulSoup(theRequest.content, "html.parser")

main()