cls
# $deities = Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Deities.aspx?ItemName=All"
# $deityList = ($deities.content | Select-String 'href\="Deities.aspx\?ItemName\=(.*?)">' -AllMatches).Matches.Groups | Where-Object Name -eq 1 | Select-Object @{e="Value";l="Deity"}

# $deityList = ($deities.content | Select-String '\<tr( style\=\"background\-color\:\#CCCCCC\;\")?\>([\v\r\f\s]*.*[\v\r\f\s]*)<\/tr>' -AllMatches).Matches

# .?\<td\>\<a href\="Deities\.aspx\?ItemName\=.*?"\>(.*?)\<\/a\>\<\/td\>\<td\>(.*?)\<\/td\>\<td\>(.*?)\<\/td\>\<td\>(.*?)\<\/td\>.?\
# <tr>
# <td><a href="Deities.aspx?ItemName=Hylax">Hylax</a></td><td>Core Deities</td><td>LG</td><td>diplomacy, first contact, friendship, peace</td>
# </tr>

# $races = Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Races.aspx?ItemName=All"
# ($races.content | Select-String 'href\="Races.aspx\?ItemName\=(.*?)">' -AllMatches).Matches.Groups | Where-Object Name -eq 1 | Select-Object @{e="Value";l="Race"} -Unique | ConvertTo-Csv

# $alignment = Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Rules.aspx?ID=1772"
# ($alignment.content | Select-String '\<a href\="Rules\.aspx\?ID\=\d+"\>(.*?)\<\/a\>' -AllMatches).Matches.Groups | Where-Object Name -eq 1 | Select-Object @{e="Value";l="Alignment"} -Unique | ConvertTo-Csv
# 
# $conditions = Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Rules.aspx?ID=165"

$conditionsList = ($conditions.content | Select-String '2 class="title">(?<Title>.*?)<\/h2>(.|\n)*?<i>(?<Source>.*?)<\/i>(.|\n)*?<br \/>(?<Description>.*?)(<h|<\/span)' -AllMatches).Matches

$conditionsListJSON = @"
{
    "Conditions": {}
}
"@ | ConvertFrom-Json
# $tempTitle = ""
# $tempSource = ""
$conditionsList.Groups | Where-Object {($_.Name -eq "Description") -or ($_.Name -eq "Source") -or ($_.Name -eq "Title")} | Foreach-Object {
    if ($_.Name -eq "Title") {
        $tempTitle = "$($_.Value)"
    }
    elseif ($_.Name -eq "Source") {
        $tempSource = "$($_.Value)"
    }
    else {
        $tempJSON = @"
{
    "Source":"$tempSource",
    "Description":"$(($_.Value).replace('"','&quot;'))"
}
"@
        $conditionsListJSON.Conditions | add-member -Name "$tempTitle" -value (Convertfrom-Json $tempJSON) -MemberType NoteProperty  
    }
}
$conditionsListJSON | ConvertTo-Json | Out-File "./json/conditions.json"

# "@ | ConvertFrom-Json
# $conditionsList | ForEach-Object {
#     # Write-Output "$($_.Groups[1]), $($_.Groups[2]), $($_.Groups[3])"
#     $tempJSON = @"
# {
#     "Source":"$($_.Groups[3])",
#     "Description":"$($_.Groups[5])"
# }
# "@
#     $conditionsListJSON.Conditions | add-member -Name "$($_.Groups[1])" -value (Convertfrom-Json $tempJSON) -MemberType NoteProperty
# }