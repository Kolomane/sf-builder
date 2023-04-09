# Name: afflictions_curses_scraper.py
# Purpose: Basic function to webscrape Afflictions/Curses
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def afflictionsBuilder(jsonTemplate,regex,listType):
    for match in regex:
        print(f"MATCH = {match}")
        if listType == "Curses":
            jsonTemplate[listType].update({
                f"{match[1]}": {
                    "SourceURL": f"{match[2]}",
                    "SourcePage": f"{match[3]}",
                    "Type": f"{match[4]}",
                    "Save": f"{match[5]}",
                    "Effect": f"{match[6]}",
                    "Cure": f"{match[7]}"
                }
            })
        if listType == "Diseases":
            jsonTemplate[listType].update({
                f"{match[1]}": {
                    "SourceURL": f"{match[2]}",
                    "SourcePage": f"{match[3]}",
                    "Type": f"{match[4]}",
                    "Save": f"{match[5]}",
                    "Track": f"{match[6]}",
                    "Frequency": f"{match[7]}",
                    "Effect": f"{match[8]}",
                    "Cure": f"{match[9]}"
                }
            })
    

def main():
    jsonTemplate = {
        "Curses": {},
        "Diseases": {},
        "Drugs": {},
        "Poisons": {}
    }

    theTableIDs = ["ctl00_MainContent_DataListAfflictions_ctl00_LabelName"]
    theCursesRegex = ' class=\"title\"><a .*?href=\"(.*?)\".*?>(.*?)<\/a><\/h2><b>Source<\/b> <a .*?href=\"(.*?)\".*?><i>(.*?)<\/i><\/a><br\s?\/><b>Type<\/b> (.*?) <b>Save<\/b> (.*?)<br\s?\/><b>Effect<\/b> (.*?)<br\s?\/><b>Cure<\/b> (.*?)<'
    theCursesURL = "https://aonsrd.com/Afflictions.aspx?Category=Curse"
    afflictionsCurses = py_scraper.scraper(theCursesURL,theTableIDs[0])
    cursesList = re.findall(theCursesRegex,str(afflictionsCurses))
    afflictionsBuilder(jsonTemplate,cursesList,"Curses")

    theDiseasesRegex = ' class=\"title\"><a .*?href=\"(.*?)\".*?>(.*?)<\/a><\/h2><b>Source<\/b> <a .*?href=\"(.*?)\".*?><i>(.*?)<\/i><\/a><br\s?\/><b>Type<\/b> (.*?) <b>Save<\/b> (.*?)<br\s?\/><b>Track<\/b> (.*?) <b>Frequency<\/b> (.*?)<br\s?\/>(<b>Effect<\/b>\s?(.*?)<br\s?\/>)?<b>Cure<\/b> (.*?)<(h2|\/span)'
    theDiseasesURL = "https://aonsrd.com/Afflictions.aspx?Category=Disease"
    afflictionsDiseases = py_scraper.scraper(theDiseasesURL,theTableIDs[0])
    diseaseList = re.findall(theDiseasesRegex,str(afflictionsDiseases[0]))
    afflictionsBuilder(jsonTemplate,diseaseList,"Diseases")

    theDrugsRegex = ' class=\"title\"><a .*?href=\"(.*?)\".*?>(.*?)<\/a><\/h2><b>Source<\/b> <a .*?href=\"(.*?)\".*?><i>(.*?)<\/i><\/a><br\s?\/><b>Level<\/b> (.*?) <b>Price<\/b> (.*?)<br\s?\/><b>Type<\/b> (.*?) <b>Save<\/b> (.*?) <b>Addiction<\/b> (.*?)<br\s?\/><b>Track<\/b> (.*?) <b>Effect<\/b> (.*?)<(h2|\/span)'
    theDrugsURL = "https://aonsrd.com/Afflictions.aspx?Category=Drug"
    # afflictionsDrugs = py_scraper.scraper(theDrugsURL,theTableIDs[0])
    # drugsList = re.findall(theDrugsRegex,str(afflictionsDrugs[0]))
    # print(drugsList)

    thePoisonsRegex = ' class=\"title\"><a .*?href=\"(.*?)\".*?>(.*?)<\/a><\/h2><b>Source<\/b> <a .*?href=\"(.*?)\".*?><i>(.*?)<\/i><\/a><br\s?\/><b>Level<\/b> (.*?) <b>Price<\/b> (.*?)<br\s?\/><b>Type<\/b> (.*?) <b>Save<\/b> (.*?)<b>Track<\/b> (.*?) <b>Frequency<\/b> (.*?)<br\s?\/><b>Effect<\/b> (.*?)<br\s?\/><b>Cure<\/b> (.*?)<(h2|\/span)'
    thePoisonsURL = "https://aonsrd.com/Afflictions.aspx?Category=Poison"
    # afflictionsPoisons = py_scraper.scraper(thePoisonsURL,theTableIDs[0])
    # poisonsList = re.findall(thePoisonsRegex,str(afflictionsPoisons[0]))
    # print(poisonsList)

    # jsonTemplate[f"{sfClass}"]['Description'] = f"{description.group('desc')}"
    print(f"JSON Template = {json.dumps(jsonTemplate)}")
    # with open('json/races_species.json', 'w', encoding='utf-8') as f:
    #     json.dump(jsonTemplate, f, ensure_ascii=False, indent=4)
main()


############################################################
# Version & Notes ##########################################
############################################################
# Notes
# # RegEx 101: https://regex101.com/

# Version 0.01
# # Date: 04/06/2023
# # Notes: Initial Upload