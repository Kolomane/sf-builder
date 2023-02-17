# $deities = Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Deities.aspx?ItemName=All"
# ($deities.content | Select-String 'href\="Deities.aspx\?ItemName\=(.*?)">' -AllMatches).Matches.Groups | Where-Object Name -eq 1 | Select-Object @{e="Value";l="Deity"} -Unique

# $races = Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Races.aspx?ItemName=All"
# ($races.content | Select-String 'href\="Races.aspx\?ItemName\=(.*?)">' -AllMatches).Matches.Groups | Where-Object Name -eq 1 | Select-Object @{e="Value";l="Race"} -Unique | ConvertTo-Csv

$alignment = Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Rules.aspx?ID=1772"
($alignment.content | Select-String '\<a href\="Rules\.aspx\?ID\=\d+"\>(.*?)\<\/a\>' -AllMatches).Matches.Groups | Where-Object Name -eq 1 | Select-Object @{e="Value";l="Alignment"} -Unique | ConvertTo-Csv