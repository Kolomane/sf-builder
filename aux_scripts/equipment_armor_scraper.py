# Name: equipment_armor_scraper.py
# Purpose: Basic function to webscrape Equipment/Armor
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def main():
    lightID = "ctl00_MainContent_GridViewArmor"
    heavyID = "ctl00_MainContent_GridViewArmor"
    poweredID = "ctl00_MainContent_GridViewPoweredArmor"
    upgradeID = "ctl00_MainContent_GridViewArmorUpgrades"
    jsonTemplate = {}
    
    jsonTemplate[f"Armor"] = {}

    jsonTemplate[f"Armor"][f"Light Armor"] = {}

    print(f"=-=-=-=-=-=-=-=-=-=-=-=\nCLASS = LIGHT ARMOR")
    theLightPrint = py_scraper.scraper(f"https://aonsrd.com/Armor.aspx?Category=Light",lightID)
    #print(theLightPrint)
    theLightDinner = re.findall('<td><font color="Black"><a href="(?P<SourceURL>.*?)"><img src=".*?" style="margin:3px 3px 0px 3px;" title="SFS Legal"\/> (?P<Name>.*?)<\/a><\/font><\/td><td><font color="Black">(?P<Level>.*?)<\/font><\/td><td><font color="Black">(?P<Price>.*?)<\/font><\/td><td><font color="Black">(?P<EACBonus>.*?)<\/font><\/td><td><font color="Black">(?P<KACBonus>.*?)<\/font><\/td><td><font color="Black">(?P<MaxDexBonus>.*?)<\/font><\/td><td><font color="Black">(?P<ArmorCheckPenalty>.*?)<\/font><\/td><td><font color="Black">(?P<SpeedAdjustment>.*?)<\/font><\/td><td><font color="Black">(?P<UpgradeSlots>.*?)<\/font><\/td><td><font color="Black">(?P<Bulk>.*?)<\/font><\/td>',str(theLightPrint))
    #print(theLightDinner)
    for row in theLightDinner:
        jsonTemplate["Armor"]["Light Armor"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Level" : f"{row[2]}",
            "Price" : f"{row[3]}",
            "EACBonus" : f"{row[4]}",
            "KACBonus" : f"{row[5]}",
            "MaxDexBonus" : f"{row[6]}",
            "ArmorCheckPenalty" : f"{row[7]}",
            "SpeedAdjustment" : f"{row[8]}",
            "UpgradeSlots" : f"{row[9]}",
            "Bulk" : f"{row[10]}"
        }
    
    jsonTemplate[f"Armor"][f"Heavy Armor"] = {}

    print(f"=-=-=-=-=-=-=-=-=-=-=-=\nCLASS = HEAVY ARMOR")
    theHeavyPrint = py_scraper.scraper(f"https://aonsrd.com/Armor.aspx?Category=Heavy",heavyID)
    print(theHeavyPrint)
    theHeavyDinner = re.findall('<td><a href="(?P<SourceURL>.*?)"><img src=".*?" style="margin:3px 3px 0px 3px;" title="SFS Legal"\/> (?P<Name>.*?)<\/a><\/td><td>(?P<Level>.*?)<\/td><td>(?P<Price>.*?)<\/td><td>(?P<EACBonus>.*?)<\/td><td>(?P<KACBonus>.*?)<\/td><td>(?P<MaxDexBonus>.*?)<\/td><td>(?P<ArmorCheckPenalty>.*?)<\/td><td>(?P<SpeedAdjustment>.*?)<\/td><td>(?P<UpgradeSlots>.*?)<\/td><td>(?P<Bulk>.*?)<\/td>',str(theHeavyPrint))
    print(theHeavyDinner)
    for row in theHeavyDinner:
        jsonTemplate["Armor"]["Heavy Armor"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Level" : f"{row[2]}",
            "Price" : f"{row[3]}",
            "EACBonus" : f"{row[4]}",
            "KACBonus" : f"{row[5]}",
            "MaxDexBonus" : f"{row[6]}",
            "ArmorCheckPenalty" : f"{row[7]}",
            "SpeedAdjustment" : f"{row[8]}",
            "UpgradeSlots" : f"{row[9]}",
            "Bulk" : f"{row[10]}"
        }

    jsonTemplate[f"Armor"][f"Powered Armor"] = {}

    print(f"=-=-=-=-=-=-=-=-=-=-=-=\nCLASS = POWERED ARMOR")
    thePoweredPrint = py_scraper.scraper(f"https://aonsrd.com/PoweredArmor.aspx?ItemName=All",poweredID)
    print(thePoweredPrint)
    thePoweredDinner = re.findall('<td><a href="(?P<SourceURL>.*?)"><img src=".*?" *.?> (?P<Name>.*?)<\/a><\/td><td>(?P<Level>.*?)<\/td><td>(?P<Price>.*?)<\/td>',str(thePoweredPrint))
    print(thePoweredDinner)
    for row in thePoweredDinner:
        jsonTemplate["Armor"]["Powered Armor"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Level" : f"{row[2]}",
            "Price" : f"{row[3]}"
        }

    jsonTemplate[f"Armor"][f"Armor Upgrades"] = {}

    print(f"=-=-=-=-=-=-=-=-=-=-=-=\nCLASS = ARMOR UPGRADES")
    theUpgradePrint = py_scraper.scraper(f"https://aonsrd.com/ArmorUpgrades.aspx?ItemName=All&Family=None",upgradeID)
    #print(theUpgradePrint)
    theUpgradeDinner = re.findall('<td><a href="(?P<SourceURL>.*?)">(?:<img src=".*?".*?"> )?(?P<Name>.*?)<\/a><\/td><td>(?P<Level>.*?)<\/td><td>(?P<Price>.*?)<\/td><td>(?P<Slots>.*?)<\/td><td>(?P<ArmorType>.*?)<\/td><td>(?P<Capacity>.*?)<\/td><td>(?P<Usage>.*?)<\/td><td>(?P<Bulk>.*?)<\/td>',str(theUpgradePrint))
    #print(theUpgradeDinner)
    for row in theUpgradeDinner:
        jsonTemplate["Armor"]["Armor Upgrades"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Level" : f"{row[2]}",
            "Price" : f"{row[3]}",
            "Slots" : f"{row[4]}",
            "ArmorType" : f"{row[5]}",
            "Capacity" : f"{row[6]}",
            "Usage" : f"{row[7]}",
            "Bulk" : f"{row[8]}"
        }
    output = json.dumps(jsonTemplate)
    print(output)
    with open('json/equipment_armor.json', 'w', encoding='utf-8') as f:
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