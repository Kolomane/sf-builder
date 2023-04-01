# Name: feats_skill_scraper.py
# Purpose: Basic function to webscrape Feats/Skill Focus (Charter)
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def main():
    defaultID = "ctl00_MainContent_GridView6"
    jsonTemplate = {}
    
    jsonTemplate[f"Skill_Feats"] = {}
    print(f"=-=-=-=-=-=-=-=-=-=-=-=\nCLASS = SKILL FEATS")

    thePrint = py_scraper.scraper(f"https://aonsrd.com/Feats.aspx?Category=Skill%20Focus",defaultID)
    print(thePrint)
    theDinner = re.findall('<td><font color="Black"><a href="(?P<SourceURL>.*?)">(?P<FeatName>.*?) \((?P<Focus>.*?) Focus\)<\/a><\/font><\/td><td><font color="Black">(?P<Prerequisites>.*?)<\/font><\/td><td><font color="Black">(?P<Description>.*?)<\/font><\/td>',str(thePrint))
    print(theDinner)
    for row in theDinner:
        print(row)
        jsonTemplate["Skill_Feats"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Focus" : f"{row[2]}",
            "Prerequisites" : f"{row[3]}",
            "Description" : f"{row[4]}"
        }
    output = json.dumps(jsonTemplate)
    print(output)
    with open('json/feats_skill.json', 'w', encoding='utf-8') as f:
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