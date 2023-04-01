# Name: themees_scraper.py
# Purpose: Basic function to webscrape Themes
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def main():
    jsonTemplate = {
        "Themes": {}
    }
    listedItems = py_scraper.scraper(f"https://aonsrd.com/Themes.aspx?ItemName=All","ctl00_MainContent_DataListTalentsAll")
    themeList = re.findall('<b><a href="(.*?)"><img .*?> (.*?)<\/a> \(\+1 (.*?)\)<\/b>\: (.*?)<\/span>',str(listedItems))
    # print(themeList)
    for theme in themeList:
        # print(f"https://aonsrd.com/{theme[0]}")
        splitMods = theme[2].replace('+1 ','').replace(',','').replace('or ','').split(' ')
        singleTheme = py_scraper.scraper(f"https://aonsrd.com/{theme[0]}","ctl00_MainContent_DataListTalentsAll_ctl00_LabelName")
        # print(singleTheme[0])
        themeInfo = re.search('<a .*? href=\"(.*?)\" .*?><i>(.*?)<\/i><\/a><br\s?\/>(.*?)<br\s?\/><h2 class=\"title\">(.*?) \(.*?\)<\/h2>(.*?)<br\s?\/><h2 class=\"title\">(.*?) \(.*?\)<\/h2>(.*?)<br\s?\/><h2 class=\"title\">(.*?) \(.*?\)<\/h2>(.*?)<br\s?\/><h2 class=\"title\">(.*?) \(.*?\)<\/h2>(.*?)<br\s?\/><\/span>',str(singleTheme[0]))
        # print(themeInfo[1])
        jsonTemplate['themes'][theme[1]] = {
            "SourceURL": f"{themeInfo[1]}",
            "SourceReference": f"{themeInfo[2]}",
            "Modifier": splitMods,
            "ShortDescription": f"{theme[3]}",
            "Description": f"{themeInfo[3]}",
            "Level1": {
                "Nickname": f"{themeInfo[4]}",
                "Description": f"{themeInfo[5]}"
            },
            "Level6": {
                "Nickname": f"{themeInfo[6]}",
                "Description": f"{themeInfo[7]}"
            },
            "Level12": {
                "Nickname": f"{themeInfo[8]}",
                "Description": f"{themeInfo[9]}"
            },
            "Level18": {
                "Nickname": f"{themeInfo[10]}",
                "Description": f"{themeInfo[11]}"
            }
        }
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