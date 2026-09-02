Import-Csv ./literatura.csv | foreach { if($_.Title -eq $_.Publisher){$_.Publisher = "";$_}else{$_} } | ConvertTo-Csv -UseQuotes Always | Set-Content -Encoding utf8BOM -Path ./new_literatura.csv
