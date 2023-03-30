# Name: classes_scraper.py
# Purpose: Basic function to webscrape Classes
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def main():
    # print("Inside MAIN")
    # All of the webpages have this as the <span> id for content
    defaultID = "ctl00_MainContent_GridViewAliens"
    # Create an empty JSON object
    jsonTemplate = {}
    
    # Add class to JSON
    jsonTemplate[f"Aliens"] = {}
    print(f"=-=-=-=-=-=-=-=-=-=-=-=\nCLASS = Aliens")
    # Scrape the website
    thePrint = py_scraper.scraper(f"https://aonsrd.com/Aliens.aspx?Letter=All",defaultID)
    theDinner = re.findall('<td><a href="(?P<SourceURL>.*?)">(?P<AlienName>.*?)<\/a><\/td><td>(?P<CR>.*?)<\/td><td>(?P<Type>.*?)<\/td><td>(?P<Environment>.*?)<\/td>',str(thePrint))
    print(theDinner)
    for row in theDinner:
        print(row)
        jsonTemplate["Aliens"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "CR" : f"{row[2]}",
            "Type" : f"{row[3]}",
            "Environment" : f"{row[4]}"
        }
    output = json.dumps(jsonTemplate)
    print(output)
    with open('json/aliens.json', 'w', encoding='utf-8') as f:
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