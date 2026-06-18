param(
    [string]$GitHubUsername = "1Honglizhang",
    [string]$RepoName = "excel-learning-path"
)

Write-Host "=========================================="
Write-Host "  Excel Learning Path - Git Push Script"
Write-Host "=========================================="
Write-Host ""

# 检查Git是否安装
try {
    git --version | Out-Null
    Write-Host "[OK] Git is installed" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Git is not installed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Git first:"
    Write-Host "1. Download from: https://git-scm.com/download/win"
    Write-Host "2. Run the installer with default options"
    Write-Host "3. Restart PowerShell"
    Write-Host ""
    exit 1
}

# 检查是否在正确的目录
if (-not (Test-Path ".git")) {
    Write-Host "[INFO] Initializing Git repository..." -ForegroundColor Yellow
    git init
} else {
    Write-Host "[OK] Git repository already initialized" -ForegroundColor Green
}

# 检查远程仓库配置
$remoteUrl = "https://github.com/$GitHubUsername/$RepoName.git"
$existingRemote = git remote get-url origin 2>$null

if ($existingRemote -ne $remoteUrl) {
    Write-Host "[INFO] Adding remote repository: $remoteUrl" -ForegroundColor Yellow
    git remote remove origin 2>$null
    git remote add origin $remoteUrl
} else {
    Write-Host "[OK] Remote repository already configured" -ForegroundColor Green
}

# 添加所有文件
Write-Host "[INFO] Adding all files..." -ForegroundColor Yellow
git add .

# 检查是否有更改
$status = git status --porcelain
if ($status -eq "") {
    Write-Host "[INFO] No changes to commit" -ForegroundColor Yellow
} else {
    # 提交更改
    $commitMessage = "Initial commit: Excel learning path from basic to professional"
    Write-Host "[INFO] Committing changes..." -ForegroundColor Yellow
    git commit -m $commitMessage
}

# 设置主分支
Write-Host "[INFO] Setting main branch..." -ForegroundColor Yellow
git branch -M main

# 推送到远程仓库
Write-Host "[INFO] Pushing to GitHub..." -ForegroundColor Yellow
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "[SUCCESS] Repository pushed to GitHub!" -ForegroundColor Green
    Write-Host "URL: https://github.com/$GitHubUsername/$RepoName"
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "[ERROR] Push failed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Common issues and solutions:"
    Write-Host "1. Repository doesn't exist on GitHub"
    Write-Host "   - Go to https://github.com/new"
    Write-Host "   - Create repo named: $RepoName"
    Write-Host "   - Do NOT add README, .gitignore, or license"
    Write-Host ""
    Write-Host "2. Authentication failed"
    Write-Host "   - Use GitHub CLI: gh auth login"
    Write-Host "   - Or use Personal Access Token: https://github.com/settings/tokens"
    Write-Host "   - Token needs: repo, workflow scopes"
    Write-Host ""
    Write-Host "3. Remote rejected"
    Write-Host "   - Try: git pull --rebase origin main"
    Write-Host "   - Then: git push -u origin main"
    Write-Host ""
    exit 1
}
