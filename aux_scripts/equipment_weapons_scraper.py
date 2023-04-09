# Name: equipment_weapons_scraper.py
# Purpose: Basic function to webscrape Equipment/Weapons
# Version & Notes: Found at bottom of document
############################################################

import json, re
import py_scraper

def main():
    oneadvancedmeleeID = "ctl00_MainContent_GridViewWeapons1Hand"
    twoadvancedmeleeID = "ctl00_MainContent_GridViewWeapons2Hands"
    amunitionID = "ctl00_MainContent_GridViewWeapons1Hand"
    onebasicmeleeID = "ctl00_MainContent_GridViewWeapons1Hand"
    twobasicmeleeID = "ctl00_MainContent_GridViewWeapons2Hands"
    grenadesID = "ctl00_MainContent_GridViewWeapons1Hand"
    heavyID = "ctl00_MainContent_GridViewWeapons2Hands"
    longarmID = "ctl00_MainContent_GridViewWeapons2Hands"
    smallarmID = "ctl00_MainContent_GridViewWeapons1Hand"
    sniperID = "ctl00_MainContent_GridViewWeapons2Hands"
    solarianID = "ctl00_MainContent_GridViewWeapons1Hand"
    onespecialID = "ctl00_MainContent_GridViewWeapons1Hand"
    twospecialID = "ctl00_MainContent_GridViewWeapons2Hands"
    criteffectsID = "ctl00_MainContent_DataListTalentsAll"
    specialpropertiesID = "ctl00_MainContent_DataListTalentsAll"
    accessoriesID = "ctl00_MainContent_GridViewWeaponAccessories"
    fusionsID = "ctl00_MainContent_GridViewWeaponFusions"


    jsonTemplate = {}
    
    jsonTemplate[f"Weapons"] = {}

    jsonTemplate["Weapons"][f"Advanced_Melee"] = {}

    oneadvancedmeleePrint = py_scraper.scraper(f"https://aonsrd.com/Weapons.aspx?Proficiency=AdvMelee",oneadvancedmeleeID)
    oneadvancedmeleeDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?:<img src=".*?> )?(?:<i>)?(?P<Name>.*?)(?:<\/i>)?<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Category>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Damage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?:<a href=".*?">)?(?P<Critical>.*?)(?:<\/a>)?(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Special>.*?)(?:<\/font>)?<\/td>',str(oneadvancedmeleePrint))
    for row in oneadvancedmeleeDinner:
        jsonTemplate["Weapons"]["Advanced_Melee"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Hands" : f"1",
            "Category" : f"{row[2]}",
            "Level" : f"{row[3]}",
            "Price" : f"{row[4]}",
            "Damage" : f"{row[5]}",
            "Critical" : f"{row[6]}",
            "Bulk" : f"{row[7]}",
            "Special" : f"{row[8]}",
        }

    twoadvancedmeleePrint = py_scraper.scraper(f"https://aonsrd.com/Weapons.aspx?Proficiency=AdvMelee",twoadvancedmeleeID)
    twoadvancedmeleeDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?:<img src=".*?> )?(?:<i>)?(?P<Name>.*?)(?:<\/i>)?<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Category>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Damage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?:<a href=".*?">)?(?P<Critical>.*?)(?:<\/a>)?(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Special>.*?)(?:<\/font>)?<\/td>',str(twoadvancedmeleePrint))
    for row in twoadvancedmeleeDinner:
        jsonTemplate["Weapons"]["Advanced_Melee"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Hands" : f"2",
            "Category" : f"{row[2]}",
            "Level" : f"{row[3]}",
            "Price" : f"{row[4]}",
            "Damage" : f"{row[5]}",
            "Critical" : f"{row[6]}",
            "Bulk" : f"{row[7]}",
            "Special" : f"{row[8]}",
        }
        
    jsonTemplate["Weapons"][f"Amunition"] = {}

    amunitionPrint = py_scraper.scraper(f"https://aonsrd.com/Weapons.aspx?Proficiency=Ammo",amunitionID)
    amunitionDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?:<img src=".*?> )?(?:<i>)?(?P<Name>.*?)(?:<\/i>)?<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Category>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Special>.*?)(?:<\/font>)?<\/td>',str(amunitionPrint))
    for row in amunitionDinner:
        jsonTemplate["Weapons"]["Amunition"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Category" : f"{row[2]}",
            "Level" : f"{row[3]}",
            "Price" : f"{row[4]}",
            "Bulk" : f"{row[5]}",
            "Special" : f"{row[6]}",
        }

    jsonTemplate["Weapons"][f"Basic_Melee"] = {}

    onebasicmeleePrint = py_scraper.scraper(f"https://aonsrd.com/Weapons.aspx?Proficiency=BasicMelee",onebasicmeleeID)
    onebasicmeleeDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?:<img src=".*?> )?(?:<i>)?(?P<Name>.*?)(?:<\/i>)?<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Category>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Damage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?:<a href=".*?">)?(?P<Critical>.*?)(?:<\/a>)?(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Special>.*?)(?:<\/font>)?<\/td>',str(onebasicmeleePrint))
    for row in onebasicmeleeDinner:
        jsonTemplate["Weapons"]["Basic_Melee"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Hands" : f"1",
            "Category" : f"{row[2]}",
            "Level" : f"{row[3]}",
            "Price" : f"{row[4]}",
            "Damage" : f"{row[5]}",
            "Critical" : f"{row[6]}",
            "Bulk" : f"{row[7]}",
            "Special" : f"{row[8]}",
        }

    twobasicmeleePrint = py_scraper.scraper(f"https://aonsrd.com/Weapons.aspx?Proficiency=BasicMelee",twobasicmeleeID)
    twobasicmeleeDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?:<img src=".*?> )?(?:<i>)?(?P<Name>.*?)(?:<\/i>)?<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Category>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Damage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?:<a href=".*?">)?(?P<Critical>.*?)(?:<\/a>)?(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Special>.*?)(?:<\/font>)?<\/td>',str(twobasicmeleePrint))
    for row in twobasicmeleeDinner:
        jsonTemplate["Weapons"]["Basic_Melee"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Hands" : f"2",
            "Category" : f"{row[2]}",
            "Level" : f"{row[3]}",
            "Price" : f"{row[4]}",
            "Damage" : f"{row[5]}",
            "Critical" : f"{row[6]}",
            "Bulk" : f"{row[7]}",
            "Special" : f"{row[8]}",
        }

    jsonTemplate["Weapons"][f"Grenade"] = {}

    grenadesPrint = py_scraper.scraper(f"https://aonsrd.com/Weapons.aspx?Proficiency=Grenade",grenadesID)
    grenadesDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?:<img src=".*?> )?(?:<i>)?(?P<Name>.*?)(?:<\/i>)?<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Range>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Capacity>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Special>.*?)(?:<\/font>)?<\/td>',str(grenadesPrint))
    for row in grenadesDinner:
        jsonTemplate["Weapons"]["Grenade"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Level" : f"{row[2]}",
            "Price" : f"{row[3]}",
            "Range" : f"{row[4]}",
            "Capacity" : f"{row[5]}",
            "Bulk" : f"{row[6]}",
            "Special" : f"{row[7]}",
        }

    jsonTemplate["Weapons"][f"Heavy_Weapon"] = {}

    heavyPrint = py_scraper.scraper(f"https://aonsrd.com/Weapons.aspx?Proficiency=Heavy",heavyID)
    heavyDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?:<img src=".*?> )?(?:<i>)?(?P<Name>.*?)(?:<\/i>)?<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Category>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Damage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Range>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?:<a href=".*?">)?(?P<Critical>.*?)(?:<\/a>)?(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Capacity>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Usage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Special>.*?)(?:<\/font>)?<\/td>',str(heavyPrint))
    for row in heavyDinner:
        jsonTemplate["Weapons"]["Heavy_Weapon"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Hands" : f"2",
            "Category" : f"{row[2]}",
            "Level" : f"{row[3]}",
            "Price" : f"{row[4]}",
            "Damage" : f"{row[5]}",
            "Range" : f"{row[6]}",
            "Critical" : f"{row[7]}",
            "Capacity" : f"{row[8]}",
            "Usage" : f"{row[9]}",
            "Bulk" : f"{row[10]}",
            "Special" : f"{row[11]}",
        }

    jsonTemplate["Weapons"][f"Longarm"] = {}

    longarmPrint = py_scraper.scraper(f"https://aonsrd.com/Weapons.aspx?Proficiency=Longarms",longarmID)
    longarmDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?:<img src=".*?> )?(?:<i>)?(?P<Name>.*?)(?:<\/i>)?<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Category>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Damage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Range>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?:<a href=".*?">)?(?P<Critical>.*?)(?:<\/a>)?(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Capacity>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Usage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Special>.*?)(?:<\/font>)?<\/td>',str(longarmPrint))
    for row in longarmDinner:
        jsonTemplate["Weapons"]["Longarm"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Hands" : f"2",
            "Category" : f"{row[2]}",
            "Level" : f"{row[3]}",
            "Price" : f"{row[4]}",
            "Damage" : f"{row[5]}",
            "Range" : f"{row[6]}",
            "Critical" : f"{row[7]}",
            "Capacity" : f"{row[8]}",
            "Usage" : f"{row[9]}",
            "Bulk" : f"{row[10]}",
            "Special" : f"{row[11]}",
        }

    jsonTemplate["Weapons"][f"Smallarm"] = {}

    smallarmPrint = py_scraper.scraper(f"https://aonsrd.com/Weapons.aspx?Proficiency=SmallArms",smallarmID)
    smallarmDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?:<img src=".*?> )?(?:<i>)?(?P<Name>.*?)(?:<\/i>)?<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Category>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Damage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Range>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?:<a href=".*?">)?(?P<Critical>.*?)(?:<\/a>)?(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Capacity>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Usage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Special>.*?)(?:<\/font>)?<\/td>',str(smallarmPrint))
    for row in smallarmDinner:
        jsonTemplate["Weapons"]["Smallarm"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Hands" : f"1",
            "Category" : f"{row[2]}",
            "Level" : f"{row[3]}",
            "Price" : f"{row[4]}",
            "Damage" : f"{row[5]}",
            "Range" : f"{row[6]}",
            "Critical" : f"{row[7]}",
            "Capacity" : f"{row[8]}",
            "Usage" : f"{row[9]}",
            "Bulk" : f"{row[10]}",
            "Special" : f"{row[11]}",
        }

    jsonTemplate["Weapons"][f"Sniper"] = {}

    sniperPrint = py_scraper.scraper(f"https://aonsrd.com/Weapons.aspx?Proficiency=Sniper",sniperID)
    sniperDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?:<img src=".*?> )?(?:<i>)?(?P<Name>.*?)(?:<\/i>)?<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Category>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Damage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Range>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?:<a href=".*?">)?(?P<Critical>.*?)(?:<\/a>)?(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Capacity>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Usage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Special>.*?)(?:<\/font>)?<\/td>',str(sniperPrint))
    for row in sniperDinner:
        jsonTemplate["Weapons"]["Sniper"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Hands" : f"1",
            "Category" : f"{row[2]}",
            "Level" : f"{row[3]}",
            "Price" : f"{row[4]}",
            "Damage" : f"{row[5]}",
            "Range" : f"{row[6]}",
            "Critical" : f"{row[7]}",
            "Capacity" : f"{row[8]}",
            "Usage" : f"{row[9]}",
            "Bulk" : f"{row[10]}",
            "Special" : f"{row[11]}",
        }

    jsonTemplate["Weapons"][f"Solarian"] = {}

    solarianPrint = py_scraper.scraper(f"https://aonsrd.com/Weapons.aspx?Proficiency=Solarian",solarianID)
    solarianDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?:<img src=".*?> )?(?:<i>)?(?P<Name>.*?)(?:<\/i>)?<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Damage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?:<a href=".*?">)?(?P<Critical>.*?)(?:<\/a>)?(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Special>.*?)(?:<\/font>)?<\/td>',str(solarianPrint))
    for row in solarianDinner:
        jsonTemplate["Weapons"]["Solarian"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Level" : f"{row[2]}",
            "Price" : f"{row[3]}",
            "Damage" : f"{row[4]}",
            "Critical" : f"{row[5]}",
            "Bulk" : f"{row[6]}",
            "Special" : f"{row[7]}",
        }

    jsonTemplate["Weapons"][f"Special"] = {}

    onespecialPrint = py_scraper.scraper(f"https://aonsrd.com/Weapons.aspx?Proficiency=Special",onespecialID)
    onespecialDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?:<img src=".*?> )?(?:<i>)?(?P<Name>.*?)(?:<\/i>)?<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Category>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Damage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Range>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?:<a href=".*?">)?(?P<Critical>.*?)(?:<\/a>)?(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Capacity>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Usage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Special>.*?)(?:<\/font>)?<\/td>',str(onespecialPrint))
    for row in onespecialDinner:
        jsonTemplate["Weapons"]["Special"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Hands" : f"1",
            "Category" : f"{row[2]}",
            "Level" : f"{row[3]}",
            "Price" : f"{row[4]}",
            "Damage" : f"{row[5]}",
            "Range" : f"{row[6]}",
            "Critical" : f"{row[7]}",
            "Capacity" : f"{row[8]}",
            "Usage" : f"{row[9]}",
            "Bulk" : f"{row[10]}",
            "Special" : f"{row[11]}",
        }

    twospecialPrint = py_scraper.scraper(f"https://aonsrd.com/Weapons.aspx?Proficiency=Special",twospecialID)
    twospecialDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)">(?:<img src=".*?> )?(?:<i>)?(?P<Name>.*?)(?:<\/i>)?<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Category>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Damage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Range>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?:<a href=".*?">)?(?P<Critical>.*?)(?:<\/a>)?(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Capacity>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Usage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Special>.*?)(?:<\/font>)?<\/td>',str(twospecialPrint))
    for row in twospecialDinner:
        jsonTemplate["Weapons"]["Special"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Hands" : f"2",
            "Category" : f"{row[2]}",
            "Level" : f"{row[3]}",
            "Price" : f"{row[4]}",
            "Damage" : f"{row[5]}",
            "Range" : f"{row[6]}",
            "Critical" : f"{row[7]}",
            "Capacity" : f"{row[8]}",
            "Usage" : f"{row[9]}",
            "Bulk" : f"{row[10]}",
            "Special" : f"{row[11]}",
        }

    jsonTemplate["Weapons"][f"Critical_Hit_Effects"] = {}

    criteffectsPrint = py_scraper.scraper(f"https://aonsrd.com/WeaponCriticals.aspx?ItemName=All",criteffectsID)
    criteffectsDinner = re.findall('<span id=".*?"><h2 class="title"><a href="(?P<SourceURL>.*?)">(?P<Name>.*?)<\/a><\/h2><b>Source<\/b>.*?<i>.*?<\/i><\/a><br\/>(?P<Description>.*?)<br\/>',str(criteffectsPrint))
    for row in criteffectsDinner:
        jsonTemplate["Weapons"]["Critical_Hit_Effects"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Description" : f"{row[2]}",
        }

    jsonTemplate["Weapons"][f"Special_Properties"] = {}

    specialpropertiesPrint = py_scraper.scraper(f"https://aonsrd.com/WeaponProperties.aspx?ItemName=All",specialpropertiesID)
    specialpropertiesDinner = re.findall('<span id=".*?"><h2 class="title"><a href="(?P<SourceURL>.*?)">(?P<Name>.*?)<\/a><\/h2><b>.*?<\/a><br\/>(?P<Description>.*?)<br\/><br\/><\/span>',str(specialpropertiesPrint))
    for row in specialpropertiesDinner:
        jsonTemplate["Weapons"]["Special_Properties"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Description" : f"{row[2]}",
        }

    jsonTemplate["Weapons"][f"Accessories"] = {}

    accessoriesPrint = py_scraper.scraper(f"https://aonsrd.com/WeaponAccessories.aspx?ItemName=All&Family=None",accessoriesID)
    accessoriesDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)"><img.*?> (?P<Name>.*?)<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Price>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Bulk>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Capacity>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Usage>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<WeaponType>.*?)(?:<\/font>)?<\/td>',str(accessoriesPrint))
    for row in accessoriesDinner:
        jsonTemplate["Weapons"]["Accessories"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Level" : f"{row[2]}",
            "Price" : f"{row[3]}",
            "Bulk" : f"{row[4]}",
            "Capacity" : f"{row[5]}",
            "Usage" : f"{row[6]}",
            "WeaponType" : f"{row[7]}",
        }

    jsonTemplate["Weapons"][f"Fusions"] = {}

    fusionsPrint = py_scraper.scraper(f"https://aonsrd.com/WeaponFusions.aspx?ItemName=All",fusionsID)
    fusionsDinner = re.findall('<td>(?:<font color="Black">)?<a href="(?P<SourceURL>.*?)"><img.*?> (?P<Name>.*?)<\/a>(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Level>.*?)(?:<\/font>)?<\/td><td>(?:<font color="Black">)?(?P<Description>.*?)(?:<\/font>)?<\/td>',str(fusionsPrint))
    for row in fusionsDinner:
        jsonTemplate["Weapons"]["Fusions"][f"{row[1]}"] = {
            "SourceURL" : f"{row[0]}",
            "Level" : f"{row[2]}",
            "Description" : f"{row[3]}",
        }
    with open('json/equipment_weapons.json', 'w', encoding='utf-8') as f:
        json.dump(jsonTemplate, f, ensure_ascii=False, indent=4)
main()


############################################################
# Version & Notes ##########################################
############################################################
# Notes
# # RegEx 101: https://regex101.com/

# Version 0.02
# # Date: 04/08/2023
# # Notes: Completed basic weapons scrape