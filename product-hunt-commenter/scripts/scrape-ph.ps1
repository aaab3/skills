param(
    [Parameter(Mandatory = $true)]
    [string]$Slug,
    [ValidateSet("ph", "hunted", "both")]
    [string]$Source = "hunted"
)

$key = $env:FIRECRAWL_API_KEY
if (-not $key) {
    Write-Error "FIRECRAWL_API_KEY is not set. Example: `$env:FIRECRAWL_API_KEY='fc-...'"
    exit 1
}

$urls = switch ($Source) {
    "ph"     { @("https://www.producthunt.com/products/$Slug") }
    "hunted" { @("https://hunted.space/product/$Slug") }
    "both"   { @(
            "https://www.producthunt.com/products/$Slug",
            "https://hunted.space/product/$Slug"
        ) }
}

$headers = @{
    Authorization  = "Bearer $key"
    "Content-Type" = "application/json"
}

$outDir = Join-Path $PSScriptRoot "..\workspace\scrapes"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

foreach ($url in $urls) {
    $tag = if ($url -match "hunted") { "hunted" } else { "ph" }
    $body = @{
        url             = $url
        formats         = @("markdown")
        waitFor         = 8000
        timeout         = 90000
        onlyMainContent = ($tag -eq "ph")
    } | ConvertTo-Json -Depth 5

    Write-Host "Scraping $url ..."
    try {
        $resp = Invoke-RestMethod -Uri "https://api.firecrawl.dev/v2/scrape" -Method POST `
            -Headers $headers -Body $body -TimeoutSec 120
        $md = $resp.data.markdown
        $outFile = Join-Path $outDir "${Slug}-${tag}-$(Get-Date -Format 'yyyy-MM-dd').md"
        $md | Out-File -FilePath $outFile -Encoding utf8
        Write-Host "OK $($md.Length) chars -> $outFile"
    }
    catch {
        Write-Warning "FAIL $url : $($_.Exception.Message)"
    }
    Start-Sleep -Seconds 2
}
