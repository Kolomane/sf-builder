# Name: spells_scraper.py
# Purpose: Basic function to webscrape Spells
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def main():
    # print("Inside MAIN")
    # All of the webpages have this as the <span> id for content
    defaultID = "ctl00_MainContent_DataListClasses_ctl00_LabelName"
    # Create an empty JSON object
    jsonTemplate = {}
    spellList = []
    spellScrape = py_scraper.scraper("view-source:https://aonsrd.com/Spells.aspx?Class=All","ctl00_MainContent_DataListTalentsAll")
    
    # Looping on each item in the list
    for sfSpell in theList:
        # Add class to JSON
        jsonTemplate[f"{sfSpell}"] = {}
        print(f"=-=-=-=-=-=-=-=-=-=-=-=\nSPEL = {sfSpell}")
        # Scrape the website
        thePrint = py_scraper.scraper(f"https://aonsrd.com/Classes.aspx?ItemName={sfSpell}",defaultID)
        # print(thePrint)
        # Search for Sources (unique RegEx to CLASSES)
        sources = re.search('<b>Source<\/b> <a.*?href="(?P<link>\S+)".*?"><i>(?P<ref>.*?)<\/i><\/a><br\/>',str(thePrint))
        print(f"link = {sources.group('link')}")
        print(f"reference = {sources.group('ref')}")
        # Search for Description (unique RegEx to CLASSES)
        description = re.search('<\/i><\/a><br\/>(?P<desc>.*?)<br\/><br\/><b>Hit Points',str(thePrint))
        print(f"description = {description.groups('desc')}")
        # Add everything above to the JSON under it's respective CLass with new key/value pairs
        jsonTemplate[f"{sfSpell}"]['SourceURL'] = f"{sources.group('link')}"
        jsonTemplate[f"{sfSpell}"]['SourceReference'] = f"{sources.group('ref')}"
        jsonTemplate[f"{sfSpell}"]['Description'] = f"{description.group('desc')}"
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
# # Date: 03/27/2023
# # Notes: Initial Upload