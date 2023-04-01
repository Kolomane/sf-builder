# Name: systems_settlements_scraper.py
# Purpose: Basic function to webscrape Systems & Settlements
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def main():
    defaultID = "ctl00_MainContent_GridView_Systems"
    jsonTemplate = {}
    
    jsonTemplate[f"Systems_Settlements"] = {}
    print(f"=-=-=-=-=-=-=-=-=-=-=-=\nCLASS = SYSTEMS & SETTLEMENTS")

    thePrint = py_scraper.scraper(f"https://aonsrd.com/Systems.aspx?ItemName=All",defaultID)
    print(thePrint)
    theDinner = re.findall('<td><a href="(?P<SourceURL>.*?)">(?P<SystemName>.*?)<\/a><\/td><td>(?P<Location>.*?)<\/td><td>(—<\/td>|<a href="(?P<Settlement1URL>.*?)">(?P<Settlement1>.*?)<\/a>(, <a href="(?P<Settlement2URL>.*?)">(?P<Settlement2>.*?)<\/a>)?<\/td>)',str(thePrint))
    print(theDinner)
    for row in theDinner:
        print(row)
        jsonTemplate["Systems_Settlements"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Location" : f"{row[2]}",
            "Settlement1URL" : f"{row[4]}",
            "Settlement1" : f"{row[5]}",
            "Settlement2URL" : f"{row[7]}",
            "Settlement2" : f"{row[8]}",
        }
    output = json.dumps(jsonTemplate)
    print(output)
    with open('json/systems_settlements.json', 'w', encoding='utf-8') as f:
        json.dump(jsonTemplate, f, ensure_ascii=False, indent=4)
main()


############################################################
# Version & Notes ##########################################
############################################################
# Notes
# # RegEx 101: https://regex101.com/

# Version 0.01
# # Date: 04/01/2023
# # Notes: Initial Upload