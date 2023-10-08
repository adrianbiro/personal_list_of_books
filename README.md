
# An Personal List of Books

Export calibre as csv:

`calibredb catalog "zmaz-$(date -I).csv"`

```bash
pwsh -c 'Import-Csv ./"zmaz-$(Get-Date -Format "yyyy-MM-dd").csv" | Select-Object -Property Authors,Title,@{n="Pubdate";e={Get-Date -Date $_.Pubdate -Format "yyyy-MM-dd"};},Publisher,Formats | ConvertTo-Csv | Set-Content -Encoding utf8BOM -Path ./"calibre-$(Get-Date -Format "yyyy-MM-dd").csv"'

```

```pwsh
Import-Csv ./"zmaz-$(Get-Date -Format "yyyy-MM-dd").csv" `
    | Select-Object -Property Authors,Title,@{n="Pubdate";e={Get-Date -Date $_.Pubdate -Format "yyyy-MM-dd"};},Publisher,Formats `
    | ConvertTo-Csv `
    | Set-Content -Encoding utf8BOM -Path ./"calibre-$(Get-Date -Format "yyyy-MM-dd").csv"
```
