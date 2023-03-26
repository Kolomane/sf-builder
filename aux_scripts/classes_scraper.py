# Name: classes_scraper.py
# Purpose: Basic function to webscrape Classes
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def main():
    # print("Inside MAIN")
    # Lazy - manually adding each Class type to a Python List, so we can loop on it
    theList = ["Biohacker","Envoy","Evolutionist","Mechanic","Mystic","Nanocyte","Operative","Precog","Solarian","Soldier","Technomancer","Vanguard","Witchwarper"]
    # All of the webpages have this as the <span> id for content
    defaultID = "ctl00_MainContent_DataListClasses_ctl00_LabelName"
    # Create an empty JSON object
    jsonTemplate = {}
    
    # Looping on each item in the list
    for sfClass in theList:
        # Add class to JSON
        jsonTemplate[f"{sfClass}"] = {}
        print(f"=-=-=-=-=-=-=-=-=-=-=-=\nCLASS = {sfClass}")
        # Scrape the website
        thePrint = py_scraper.scraper(f"https://aonsrd.com/Classes.aspx?ItemName={sfClass}",defaultID)
        # print(thePrint)
        # Search for Sources (unique RegEx to CLASSES)
        sources = re.search('<b>Source<\/b> <a.*?href="(?P<link>\S+)".*?"><i>(?P<ref>.*?)<\/i><\/a><br\/>',str(thePrint))
        print(f"link = {sources.group('link')}")
        print(f"reference = {sources.group('ref')}")
        # Search for Description (unique RegEx to CLASSES)
        description = re.search('<\/i><\/a><br\/>(?P<desc>.*?)<br\/><br\/><b>Hit Points',str(thePrint))
        print(f"description = {description.groups('desc')}")
        # Add everything above to the JSON under it's respective CLass with new key/value pairs
        jsonTemplate[f"{sfClass}"]['SourceURL'] = f"{sources.group('link')}"
        jsonTemplate[f"{sfClass}"]['SourceReference'] = f"{sources.group('ref')}"
        jsonTemplate[f"{sfClass}"]['Description'] = f"{description.group('desc')}"
    # print(f"JSON Template = {json.dumps(jsonTemplate)}")
    # Write the JSON output to the json folder
    with open('json/classes.json', 'w', encoding='utf-8') as f:
        json.dump(jsonTemplate, f, ensure_ascii=False, indent=4)
    # print("Exiting MAIN")
main()


############################################################
# Version & Notes ##########################################
############################################################
# Notes
# # RegEx 101: https://regex101.com/

# Version 0.01
# # Date: 03/26/2023
# # Notes: Initial Upload