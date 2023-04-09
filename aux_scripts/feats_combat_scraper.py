# Name: feats_combat_scraper.py
# Purpose: Basic function to webscrape Feats/Combat
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def main():
    defaultID = "ctl00_MainContent_GridView6"
    jsonTemplate = {}
    
    jsonTemplate[f"Combat_Feats"] = {}
    print(f"=-=-=-=-=-=-=-=-=-=-=-=\nCLASS = COMBAT FEATS")

    thePrint = py_scraper.scraper(f"https://aonsrd.com/Feats.aspx?Category=Combat",defaultID)
    print(thePrint)
    theDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)"><img src=".*?" style="margin:3px 3px 0px 3px;" title="SFS Legal"\/> (?P<FeatName>.*?)<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Prerequisites>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Description>.*?)(?:<\/font>)?',str(thePrint))
    print(theDinner)
    for row in theDinner:
        print(row)
        jsonTemplate["Combat_Feats"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Prerequisites" : f"{row[2]}",
            "Description" : f"{row[3]}",
        }
    output = json.dumps(jsonTemplate)
    print(output)
    with open('json/feats_combat.json', 'w', encoding='utf-8') as f:
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