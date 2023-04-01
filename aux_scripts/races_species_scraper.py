# Name: themees_scraper.py
# Purpose: Basic function to webscrape Themes
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def main():
    jsonTemplate = {
        "Races": {
            "Core": {},
            "Legacy": {},
            "Other": {}
        }
    }

    theTableIDs = ["ctl00_MainContent_GridViewRacesCore","ctl00_MainContent_GridViewRacesCoreLegacy","ctl00_MainContent_GridViewRacesOther"]
    theRegex = '<td style=\"\S+\"><a href=\"(.*?)\">(<img src=\"\S+\" title=\".*?\" style=\".*?\">)?\s?(.*?)</a></td><td style=\"\S+\">(.*?)</td><td align=\"\S+\" style=\"\S+\">(.*?)</td><td align=\"\S+\" style=\"\S+\">(.*?)</td>'
    theURL = "https://aonsrd.com/Races.aspx?ItemName=All"
    coreRaces = py_scraper.scraper(theURL,)
    coreList = re.findall(theRegex,str(coreRaces))


    legacyRaces = py_scraper.scraper(theURL,)
    legacyList = re.findall(theRegex,str(legacyRaces))

    otherRaces = py_scraper.scraper(theURL,)
    otherList = re.findall(theRegex,str(otherRaces))

    # jsonTemplate[f"{sfClass}"]['Description'] = f"{description.group('desc')}"
    # print(f"JSON Template = {json.dumps(jsonTemplate)}")
    with open('json/themes.json', 'w', encoding='utf-8') as f:
        json.dump(jsonTemplate, f, ensure_ascii=False, indent=4)
main()


############################################################
# Version & Notes ##########################################
############################################################
# Notes
# # RegEx 101: https://regex101.com/

# Version 0.01
# # Date: 03/26/2023
# # Notes: Initial Upload