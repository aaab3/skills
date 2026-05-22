# Push to https://github.com/aaab3/skills via SSH deploy key
# Run: .\push-to-github.ps1
# Force overwrite: .\push-to-github.ps1 -Force

param(
    [switch]$Force
)

Set-Location $PSScriptRoot

$key = Join-Path $PSScriptRoot ".deploy-keys\github-skills-deploy"
if (-not (Test-Path $key)) {
    Write-Host "Missing deploy key: $key" -ForegroundColor Red
    exit 1
}

$env:GIT_SSH_COMMAND = "ssh -i `"$key`" -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
git remote set-url origin git@github.com:aaab3/skills.git

if ($Force) {
    Write-Host "Force pushing to origin main..." -ForegroundColor Yellow
    git push -u origin main --force
} else {
    Write-Host "Pushing to origin main..." -ForegroundColor Cyan
    git push -u origin main
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Push rejected. Try: git pull origin main --rebase; or .\push-to-github.ps1 -Force" -ForegroundColor Yellow
    }
}

if ($LASTEXITCODE -eq 0) {
    Write-Host "Done: https://github.com/aaab3/skills" -ForegroundColor Green
} else {
    exit $LASTEXITCODE
}
