import requests, json, re
from bs4 import BeautifulSoup

def main():
    print("Starting Main")
    theURL = "https://aonsrd.com/Companions.aspx"
    theRequest = requests.get(theURL)
    theSoup = BeautifulSoup(theRequest.content, "html.parser")
    tableList = []
    tempContentList = []
    numOfColumns = 5
    tempJson = {
        "Creature_Companions": {}
    }
    for thead in theSoup.table.find_all('th'):
        tableList.append(thead.text)
    for cell in theSoup.table.find_all('td'):
        tempContentList.append(cell.text)
    tupleTheContent = [iter(tempContentList)] * numOfColumns
    listTheTuple = list(zip(*tupleTheContent))

    for item in listTheTuple:
        loopyTempJson = {}
        for header in range(len(tableList)):
            if (header != 0) and (header != 4):
                loopyTempJson.update({f"{tableList[header]}": f"{item[header]}"})
            elif (header == 4):
                loopyTempJson.update({f"{tableList[header]}": (item[header].replace('Su,','Su:').replace('Ex,','Ex:').replace(';',',').split(','))})
        tempJson["Creature_Companions"][f"{item[0]}"] = loopyTempJson
        print(loopyTempJson)
    print("Ending Main")
    print(json.dumps(tempJson))

main()