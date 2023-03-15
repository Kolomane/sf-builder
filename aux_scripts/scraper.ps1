cls
# $races = Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Races.aspx?ItemName=All"
# ($races.content | Select-String 'href\="Races.aspx\?ItemName\=(.*?)">' -AllMatches).Matches.Groups | Where-Object Name -eq 1 | Select-Object @{e="Value";l="Race"} -Unique | ConvertTo-Csv

#########################################
# ALIGNMENT SCRAPER
# $alignment = Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Rules.aspx?ID=1772"
# ($alignment.content | Select-String '\<a href\="Rules\.aspx\?ID\=\d+"\>(.*?)\<\/a\>' -AllMatches).Matches.Groups | Where-Object Name -eq 1 | Select-Object @{e="Value";l="Alignment"} -Unique | ConvertTo-Csv 

#########################################
# CONDITIONS SCRAPER
# $conditions = Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Rules.aspx?ID=165"
# $conditionsList = ($conditions.content | Select-String '2 class="title">(?<Title>.*?)<\/h2>(.|\n)*?<i>(?<Source>.*?)<\/i>(.|\n)*?<br \/>(?<Description>.*?)(<h|<\/span)' -AllMatches).Matches
# $conditionsListJSON = @"
# {
#     "Conditions": {}
# }
# "@ | ConvertFrom-Json
# $conditionsList.Groups | Where-Object {($_.Name -eq "Description") -or ($_.Name -eq "Source") -or ($_.Name -eq "Title")} | Foreach-Object {
#     if ($_.Name -eq "Title") {
#         $tempTitle = "$($_.Value)"
#     }
#     elseif ($_.Name -eq "Source") {
#         $tempSource = "$($_.Value)"
#     }
#     else {
#         $tempJSON = @"
# {
#     "Source":"$tempSource",
#     "Description":"$(($_.Value).replace('"','&quot;'))"
# }
# "@
#         $conditionsListJSON.Conditions | add-member -Name "$tempTitle" -value (Convertfrom-Json $tempJSON) -MemberType NoteProperty  
#     }
# }
# $conditionsListJSON | ConvertTo-Json | Out-File "./json/conditions.json"

#########################################
# DIETIES SCRAPER
# $deities = Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Deities.aspx?ItemName=All"
# $deitiesList = ($deities.content | Select-String 'href="Deities\.aspx\?ItemName=(?<Name>\S+)">.*?<td>(?<Pantheon>.*?)<\/td><td>(?<Alignment>\w+)<\/td><td>(?<Portfolios>.*?)<\/td>' -AllMatches).Matches
# $deitiesListJSON = @"
# {
#     "Deities": {}
# }
# "@ | ConvertFrom-Json
# $deitiesList.Groups | Where-Object {($_.Name -eq "Name") -or ($_.Name -eq "Pantheon") -or ($_.Name -eq "Alignment") -or ($_.Name -eq "Portfolios")} | Foreach-Object {
#     if ($_.Name -eq "Name") {
#         $tempName = "$($_.Value)"
#         Write-Output "Working on $tempName"
#         $getDeity = (Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Deities.aspx?ItemName=$tempName").content
#         $deityInfo = $getDeity | Select-String '.*class="title">(?<subName>.*?)<\/h2>.*?<a href="(?<URL>\S+)" target.*?<i>(?<Source>.*?)<\/i>.*?Centers of Worship<\/b> (?<CentersOfWorship>.*?)<br \/><b>Symbol<\/b> (?<Symbol>.*?)<br \/><b>Alternative Theme Knowledge<\/b> (?<AlternativeThemeKnowledge>.*?)<br \/><b>Favored Weapon<\/b> (?<FavoredWeapon>.*?)<br \/><b>Edicts<\/b> (?<Edicts>.*?)<br \/><b>Anathema<\/b> (?<Anathema>.*?)<br \/><b>Blessings<\/b> (?<Blessings>.*?)<br \/><b>Curses<\/b> (?<Curses>.*?)<br \/><br \/>(?<About>.*?)<\/span' -AllMatches
#         Write-Output " - Scraped additional info..."
#     }
#     elseif ($_.Name -eq "Pantheon") {
#         $tempPantheon = "$($_.Value)"
#         Write-Output " - Pantheon = $tempPantheon"
#     }
#     elseif ($_.Name -eq "Alignment") {
#         $tempAlignment = "$($_.Value)"
#         Write-Output " - Alignment = $tempAlignment"
#     }
#     else {
#         $tempDescription = "$($_.Value)"
#         if ($tempDescription -ne $null) {
#             $tempDescription = $tempDescription.replace('"','&quot;').replace('<i>','').replace('</i>','').replace('<br />',' ')
#         }
#         try {
#             $tempJSON = @"
#             {
#                 "SubName":"$($deityInfo.Matches.Groups[1].Value)",
#                 "URL":"$($deityInfo.Matches.Groups[2].Value)",
#                 "Source":"$($deityInfo.Matches.Groups[3].Value)",
#                 "Pantheon":"$tempPantheon",
#                 "Alignment":"$tempAlignment",
#                 "Description":"$tempDescription",
#                 "CentersOfWorship":"$(($deityInfo.Matches.Groups[4].Value).replace('<i>','').replace('</i>','').replace('<br />',' '))",
#                 "Symbol":"$($deityInfo.Matches.Groups[5].Value)",
#                 "AlternativeThemeKnowledge":"$($deityInfo.Matches.Groups[6].Value)",
#                 "FavoredWeapon":"$($deityInfo.Matches.Groups[7].Value)",
#                 "Edicts":"$($deityInfo.Matches.Groups[8].Value)",
#                 "Anathema":"$($deityInfo.Matches.Groups[9].Value)",
#                 "Blessings":"$($deityInfo.Matches.Groups[10].Value)",
#                 "Curses":"$($deityInfo.Matches.Groups[11].Value)",
#                 "About":"$(($deityInfo.Matches.Groups[12].Value).replace('"','&quot;').replace('<i>','').replace('</i>','').replace('<br />',' '))"
#             }
# "@ 
#         }
#         catch {
#             $deityInfo = $getDeity | Select-String '.*<a href="(?<URL>\S+)" target.*?<i>(?<Source>.*?)<\/i><\/a><br \/>(?<subName>.*?)<br \/><br \/>(?<About>.*?)<\/span'
#             $tempJSON = @"
#         {
#             "SubName":"$($deityInfo.Matches.Groups[3].Value)",
#             "URL":"$($deityInfo.Matches.Groups[1].Value)",
#             "Source":"$($deityInfo.Matches.Groups[2].Value)",
#             "Pantheon":"$tempPantheon",
#             "Alignment":"$tempAlignment",
#             "Description":"$tempDescription",
#             "About":"$(($deityInfo.Matches.Groups[4].Value).replace('"','&quot;').replace('<i>','').replace('</i>','').replace('<br />',' '))"
#         }
# "@
#         }
#         # Write-Output " - tempJSON = $tempJSON"
#         Write-Output " - - Adding JSON"
#         $deitiesListJSON.Deities | add-member -Name "$tempName" -value (Convertfrom-Json $tempJSON) -MemberType NoteProperty
#         Write-Output " - Finished adding JSON"  
#     }
# }
# $deitiesListJSON | ConvertTo-Json | Out-File "./json/deities.json"

#########################################
# THEMES SCRAPER
# https://aonsrd.com/Themes.aspx?ItemName=All
$themes = (Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Themes.aspx?ItemName=All").content
$themesList = ($themes | Select-String '<span.*?> (?<themeName>.*?)<\/a> \(\+(?<themeModNumber>\d) (?<themeMod>.*?)\)<\/b>: (?<shortDescription>.*?)<\/span>' -AllMatches).Matches.Groups
$themesListJSON = @"
{
    "Themes": {}
}
"@ | ConvertFrom-Json
$themesList | Where-Object {($_.Name -eq "themeName") -or ($_.Name -eq "themeModNUmber") -or ($_.Name -eq "themeMod") -or ($_.Name -eq "shortDescription")} | ForEach-Object {
    if ($_.Name -eq "themeName") {
        $tempThemeName = "$($_.Value)"
        Write-Output "Working on $tempThemeName"
        $getTheme = (Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Themes.aspx?ItemName=$tempName").content
        $themeInfo = ($getTheme | Select-String '' -AllMatches).Matches
    }
    elseif ($_.Name -eq "themeModNumber") {
        $tempThemeModNumber = "$($_.Value)"
    }
    elseif ($_.Name -eq "themeMod") {
        $tempThemeMod = "$(($_.Value).replace(', or',',').replace(' or',',').replace(' ',',').replace('+1','').replace(',,',','))"
        # if ($tempThemeMod -match '.*?,.*?') {
        #     $tempThemeMod = $tempThemeMod.split(',')
        # }
    }
    else {
        $tempJSON = @"
{
    "ModifierNumber": "$tempThemeModNumber",
    "Modifier": [$tempThemeMod],
    "ShortDescription": "$($_.Value)"
    "LongDescription": "",
    "Levels": {
        "1": {
            "Name": "",
            "Description": ""
        },
        "6": {
            "Name": "",
            "Description": ""
        },
        "12": {
            "Name": "",
            "Description": ""
        },
        "18": {
            "Name": "",
            "Description": ""
        }
    }
}
"@
    }
}
$themesListJSON | ConvertTo-Json | Out-File "./json/themes.json"

#########################################
# CORRUPTIONS SCRAPER
# https://aonsrd.com/Corruptions.aspx?ItemName=All
# $corruptions = (Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Corruptions.aspx?ItemName=All").content
# $corruptionsList = ($corruptions | Select-String '.*<a href="(?<URL>\S+)">(?<Name>.*?)<\/a><\/h2>.*?<a href="(?<SourceURL>\S+)".*?<i>(?<Source>.*?)<\/i><\/a><br \/>(?<About>.*?)<h3.*?Type<\/b> (?<Type>.*?)<b>Save<\/b> (?<Save>.*?)<br \/><b>Frequency<\/b> (?<Frequency>.*?)<br \/><b>Cure<\/b> (?<Cure>.*?)<br \/>' -AllMatches).Matches.Groups
# $corruptionsListJSON = @"
# {
#     "Corruptions": {}
# }
# "@ | ConvertFrom-Json
# $corruptionsList | Where-Object { ($_.Name -eq "URL") -or ($_.Name -eq "Source") -or ($_.Name -eq "SourceURL") -or ($_.Name -eq "Name") -or ($_.Name -eq "About") -or ($_.Name -eq "Type") -or ($_.Name -eq "Save") -or ($_.Name -eq "Frequency") -or ($_.Name -eq "Cure") } | ForEach-Object {
#     if ($_.Name -eq "URL") {
#         $tempURL = "$($_.Value)"
#         Write-Output "Working on $tempURL"
#         $getCorruption = (Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/$tempURL").content
#         $corruptionInfo = ($getCorruption | Select-String '(.*?Progression<\/h2>(?<Progression>.*?)<h2 class="title">.*?Manifes.ations<\/h2>)?(?<Manifestations><h3 class="framing">(?<Name>.*?)<\/h3><b>Source<\/b> <a href="(?<SourceURL>\S+?)".*?><i>(?<Source>.*?)<\/i><\/a><br \/>(?<Description>.*?)<br \/>(<b>Prerequisites:<\/b> (?<PreReq>.*?)<br \/>)?<b>Gift:<\/b> (?<Gift>.*?)<br \/><b>Stain:<\/b> (?<Stain>.*?)<br \/>)' -AllMatches).Matches
#     }
#     elseif ($_.Name -eq "Source") {
#         $tempSource = "$($_.Value)"
#     }
#     elseif ($_.Name -eq "SourceURL") {
#         $tempSourceURL = "$($_.Value)"
#     }
#     elseif ($_.Name -eq "Name") {
#         $tempName = "$($_.Value)"
#     }
#     elseif ($_.Name -eq "About") {
#         $tempAbout = "$($_.Value)"
#     }
#     elseif ($_.Name -eq "Type") {
#         $tempType = "$($_.Value)"
#     }
#     elseif ($_.Name -eq "Save") {
#         $tempSave = "$($_.Value)"
#     }
#     elseif ($_.Name -eq "Frequency") {
#         $tempFrequency = "$($_.Value)"
#     }
#     else {
#         $tempCure = $_.Value -replace '<.*?>', ''
#         $tempJSON = @"
# {
#     "Source":"$tempSource",
#     "SourceURL":"$tempSourceURL",
#     "About":"$tempAbout",
#     "Type":"$tempType",
#     "Save":"$tempSave",
#     "Frequency":"$tempFrequency",
#     "Cure":"$tempCure",
#     "Progression":"$(($corruptionInfo.Groups | Where-object {$_.Name -eq "Progression"} | Select-Object -First 1 Value).Value -replace '<.*?>', '')",
#     "Manifestations": {}
# }
# "@
#         # Write-Output "tempName = $tempName | tempJSON = $tempJSON"
#         $corruptionsListJSON.Corruptions | add-member -Name "$tempName" -value (Convertfrom-Json $tempJSON) -MemberType NoteProperty

#         $corruptionInfo.Groups | Where-object { ($_.Name -eq "Name") -or ($_.Name -eq "SourceURL") -or ($_.Name -eq "Source") -or ($_.Name -eq "Description") -or ($_.Name -eq "PreReq") -or ($_.Name -eq "Gift") -or ($_.Name -eq "Stain") } | ForEach-Object {
#             if ($_.Name -eq "Name") {
#                 $tempManiName = "$($_.Value)"
#             }
#             elseif ($_.Name -eq "SourceURL") {
#                 $tempManiSourceURL = "$($_.Value)"
#             }
#             elseif ($_.Name -eq "Source") {
#                 $tempManiSource = "$($_.Value)"
#             }
#             elseif ($_.Name -eq "Description") {
#                 $tempManiDescription = "$($_.Value)"
#             }
#             elseif ($_.Name -eq "PreReq") {
#                 $tempManiPreReq = "$($_.Value)"
#             }
#             elseif ($_.Name -eq "Gift") {
#                 $tempManiGift = "$($_.Value -replace '<.*?>', '')"
#             }
#             else {
#                 [String]$tempManiJSON = "
# {
#     `"Source`":`"$tempManiSource`",
#     `"SourceURL`":`"$tempManiSourceURL`",
#     `"Description`":`"$tempManiDescription`",
#     `"Prerequisites`":`"$tempManiPreReq`",
#     `"Gift`":`"$tempManiGift`",
#     `"Stain`":`"$($_.Value -replace '<.*?>', '')`"
# }"
#                 $corruptionsListJSON.Corruptions.$tempName.Manifestations | add-member -Name "$tempManiName" -value ($tempManiJSON) -MemberType NoteProperty
#             }
#         }
#     }
# }
# $corruptionsListJSON | ConvertTo-Json | Out-File "./json/corruptions.json"