# Name: equipment_artifacts_scraper.py
# Purpose: Basic function to webscrape Equipment/Artifacts
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def main():
    defaultID = "ctl00_MainContent_GridView_Artifacts"
    jsonTemplate = {}
    
    jsonTemplate[f"Artifacts"] = {}
    thePrint = py_scraper.scraper(f"https://aonsrd.com/Artifacts.aspx?ItemName=All",defaultID)
    theDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?P<Name>.*?)<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Source>.*?)(?:<\/font>)?<\/td>',str(thePrint))
    for row in theDinner:
        jsonTemplate["Artifacts"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Source" : f"{row[2]}",
        }
    with open('json/equipment_artifacts.json', 'w', encoding='utf-8') as f:
        json.dump(jsonTemplate, f, ensure_ascii=False, indent=4)
main()


############################################################
# Version & Notes ##########################################
############################################################
# Notes
# # RegEx 101: https://regex101.com/

# Version 0.01
# # Date: 04/08/2023
# # Notes: Initial Upload