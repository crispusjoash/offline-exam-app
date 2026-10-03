# 1. Git Push
Write-Host "--- Git Backup ---"
git add src/ public/ electron/
git commit -m "Updates to KJSEA Creative Arts and Sports Section B & bug fixes"
git push origin main

# 2. Build Web
Write-Host "--- Building Web Assets ---"
npm run build

# 3. Android Build
Write-Host "--- Syncing and Building Android APK ---"
npx cap sync android
Set-Location android
.\gradlew assembleDebug
Set-Location ..

# 4. Windows Build
Write-Host "--- Building Windows EXE ---"
Set-Location electron
npm run pack
Set-Location ..

Write-Host "--- Build Process Complete ---"
