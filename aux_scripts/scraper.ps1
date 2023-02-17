$deities = Invoke-WebRequest -Method Get -Uri "https://aonsrd.com/Deities.aspx?ItemName=All"
Write-Output "{
    `"Deity`": ["
($deities.content | Select-String 'href\="Deities.aspx\?ItemName\=(.*?)">' -AllMatches).Matches.Groups | Where-Object Name -eq 1 | Select-Object @{e="Value";l="Deity"} -Unique | ForEach-Object {
    if ($_.Deity -ne "All") {
        Write-Output ","
    }
    Write-Output "`"$($_.Deity)`""
}
Write-Output "]}"