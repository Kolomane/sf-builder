# Name: equipment_shields_scraper.py
# Purpose: Basic function to webscrape Equipment/Shields
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def main():
    defaultID = "ctl00_MainContent_DataElement"
    jsonTemplate = {}
    
    jsonTemplate[f"Shields"] = {}
    print(f"=-=-=-=-=-=-=-=-=-=-=-=\nCLASS = SHIELDS")

    thePrint = py_scraper.scraper(f"https://aonsrd.com/Shields.aspx",defaultID)
    print(thePrint)
    theDinner = re.findall('<td><font color="Black"><a href="(?P<SourceID>.*?)">(?:<i>)?<u>(?P<Name>.*?)<\/u>(?:<\/i>)?<\/a><\/font><\/td><td><font color="Black">(?P<Level>.*?)<\/font><\/td><td><font color="Black">(?P<Price>.*?)<\/font><\/td><td><font color="Black">(?P<ShieldBonus>.*?)<\/font><\/td><td><font color="Black">(?P<MaxDex>.*?)<\/font><\/td><td><font color="Black">(?P<ArmorCheckPenalty>.*?)<\/font><\/td><td><font color="Black">(?P<Bulk>.*?)<\/font><\/td><td><font color="Black">(?P<Upgrades>.*?)<\/font><\/td>',str(thePrint))
    print(theDinner)
    for row in theDinner:
        print(row)
        jsonTemplate["Shields"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Level" : f"{row[2]}",
            "Price" : f"{row[3]}",
            "ShieldBonus" : f"{row[4]}",
            "MaxDex" : f"{row[5]}",
            "ArmorCheckPenalty" : f"{row[6]}",
            "Bulk" : f"{row[7]}",
            "Upgrades" : f"{row[8]}",
        }
    output = json.dumps(jsonTemplate)
    print(output)
    with open('json/equipment_shields.json', 'w', encoding='utf-8') as f:
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