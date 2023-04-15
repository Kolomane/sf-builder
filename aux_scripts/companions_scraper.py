import requests, json, re
from bs4 import BeautifulSoup

def main():
    print("Starting Main")
    theURL = "https://aonsrd.com/Companions.aspx"
    theRequest = requests.get(theURL)
    theSoup = BeautifulSoup(theRequest.content, "html.parser")
    tableList = []
    tempContentList = []
    recursiveLink = []
    numOfColumns = 5
    tempJson = {
        "Creature_Companions": {}
    }
    for thead in theSoup.table.find_all('th'):
        tableList.append(thead.text)
    for cell in theSoup.table.find_all('td'):
        tempContentList.append(cell.text)
        if cell.a:
            recursiveLink.append(f"https://aonsrd.com/{cell.a['href']}")
    tupleTheContent = [iter(tempContentList)] * numOfColumns
    listTheTuple = list(zip(*tupleTheContent))

    urlCounter = 0
    loopyTempJson = {}
    for item in listTheTuple:
        loopyTempJson[f"{item[0]}"] = {}
        theTempURL = recursiveLink[urlCounter]
        theTempRequest = requests.get(theTempURL)
        theTempSoup = BeautifulSoup(theTempRequest.content, "html.parser")
        for htmlItem in theTempSoup.find('span', {'id': 'ctl00_MainContent_DetailedOutput'}).children:
            if (str(htmlItem.text) != "") and (str(htmlItem) != ""):
                if 'paizo.com' in str(htmlItem):
                    loopyTempJson[f"{item[0]}"]['Source'] = {
                        "URL": f"{htmlItem['href']}",
                        "Reference": f"{htmlItem.text}"
                    }
                elif '<' in str(htmlItem):
                    tempKey = f"{htmlItem.text}"
                    if tempKey == "Source":
                        tempKey = "Description"
                else:
                    tempValue = f"{htmlItem.text}"
                    if re.findall('(Senses|Save|Attack|Space|Reach|Modifier)',tempKey):
                        tempValue = tempValue.split(',')
                    loopyTempJson[f"{item[0]}"].update({tempKey: tempValue})
        for header in range(len(tableList)):
            if (header != 0) and (header != 4):
                loopyTempJson[f"{item[0]}"].update({f"{tableList[header]}": f"{item[header]}"})
            elif (header == 4):
                loopyTempJson[f"{item[0]}"].update({f"{tableList[header]}": (item[header].replace('Su,','Su:').replace('Ex,','Ex:').replace(';',',').split(','))})
        tempJson["Creature_Companions"] = loopyTempJson
        urlCounter += 1
        # print(tempJson)
        # print(loopyTempJson)
    print("Ending Main")
    print(recursiveLink)
    # print(json.dumps(tempJson))
    with open('json/companions.json', 'w', encoding='utf-8') as f:
        json.dump(tempJson, f, ensure_ascii=False, indent=4)

main()