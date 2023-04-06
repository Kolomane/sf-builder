# Name: themes_scraper.py
# Purpose: Basic function to webscrape Themes
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def speciesBuilder(jsonTemplate,regex,listType):
    for match in regex:
        tempMods = {}
        abilityModsOptions = match[3].split(' or ')
        if len(abilityModsOptions) == 2:
            theOptions = re.findall('\((.*?)\)',str(match[3]))
            abilityMods = re.findall('(.\d)\s(\S+)',str(match[3]))
            modOptionCount = 0
            for singleMod in range(len(abilityMods)):
                if singleMod%3 <= 2:
                    try:
                        tempMods[f"{theOptions[modOptionCount]}"]
                    except:
                        tempMods[f"{theOptions[modOptionCount]}"] = {}
                    tempMods[f"{theOptions[modOptionCount]}"].update({f"{abilityMods[singleMod][1].replace(',','')}": f"{abilityMods[singleMod][0]}"})
                    if singleMod == 2:
                        modOptionCount += 1
            print(tempMods)
        else:
            abilityMods = re.findall('(.\d)\s(\S+)',str(match[3]).replace('to any one ability score','Any'))
            tempMods[f"Default"] ={}
            for singleMod in range(len(abilityMods)):
                tempMods[f"Default"].update({f"{abilityMods[singleMod][1].replace(',','')}": f"{abilityMods[singleMod][0]}"})
            print(tempMods)
        jsonTemplate['Races'][listType][f"{match[2]}"] = {
            "SourceURL": f"{match[0]}",
            "AbilityModifiers": tempMods,
            "HitPoints": f"{match[4]}",
            "ShortDescription": f"{match[5]}"
        }
    # print(jsonTemplate)

def main():
    jsonTemplate = {
        "Races": {
            "Core": {},
            "Legacy": {},
            "Other": {}
        }
    }

    theTableIDs = ["ctl00_MainContent_GridViewRacesCore","ctl00_MainContent_GridViewRacesCoreLegacy","ctl00_MainContent_GridViewRacesOther"]
    theRegex = '<td .*?>?<a href=\"(.*?)\">(<img src=\"\S+\" .*?\/>)?\s?(.*?)</a></td><td .*?>(.*?)</td><td .*?>(.*?)</td><td .*?>(.*?)</td>'
    theURL = "https://aonsrd.com/Races.aspx?ItemName=All"
    coreRaces = py_scraper.scraper(theURL,theTableIDs[0])
    coreList = re.findall(theRegex,str(coreRaces).replace('<font color="Black">','').replace('</font>',''))
    speciesBuilder(jsonTemplate,coreList,"Core")

    legacyRaces = py_scraper.scraper(theURL,theTableIDs[1])
    legacyList = re.findall(theRegex,str(legacyRaces))
    speciesBuilder(jsonTemplate,legacyList,"Legacy")

    otherRaces = py_scraper.scraper(theURL,theTableIDs[2])
    otherList = re.findall(theRegex,str(otherRaces))
    speciesBuilder(jsonTemplate,otherList,"Other")

    # jsonTemplate[f"{sfClass}"]['Description'] = f"{description.group('desc')}"
    print(f"JSON Template = {json.dumps(jsonTemplate)}")
    with open('json/races_species.json', 'w', encoding='utf-8') as f:
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