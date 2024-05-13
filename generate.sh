#!/bin/bash

mv -v calibre-*.csv old/

calibredb catalog "zmaz-$(date -I).csv"

pwsh -c 'Import-Csv ./"zmaz-$(Get-Date -Format "yyyy-MM-dd").csv" | Select-Object -Property Authors,Title,@{n="Pubdate";e={Get-Date -Date $_.Pubdate -Format "yyyy-MM-dd"};},Publisher,Formats | ConvertTo-Csv | Set-Content -Encoding utf8BOM -Path ./"calibre-$(Get-Date -Format "yyyy-MM-dd").csv"'

mv -v zmaz-*.csv old/
