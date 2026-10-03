$mapping = @{
    "q2" = "media_1787426352432.png"
    "q4" = "media_1787426497699.png"
    "q5" = "media_1787426604081.png"
    "q6" = "media_1787426687032.png"
    "q7" = "media_1787426813694.png"
    "q9" = "media_1787427023239.png"
    "q24" = "media_1787427286037.png"
    "q31" = "media_1787427366702.png"
    "q32" = "media_1787427434908.png"
    "q33" = "media_1787427533647.png"
    "q34" = "media_1787427631633.png"
    "q37" = "media_1787427674432.png"
    "q42" = "media_1787429764602.png"
    "q43" = "media_1787429855662.png"
    "q52" = "media_1787429928846.png"
}

$sourceDir = "C:\Users\JOASH\.gemini\antigravity-ide\brain\9d39c76d-2c71-4969-8f52-1885f6f7bfde\.user_uploaded"
$dest1 = "C:\Users\JOASH\Desktop\CBC\offline-exam-app\public\assets"
$dest2 = "C:\Users\JOASH\Desktop\CBC\offline-exam-app\electron\app\assets"

foreach ($entry in $mapping.GetEnumerator()) {
    $srcPath = Join-Path $sourceDir $entry.Value
    $destFile = "kjsea_cas_2025_$($entry.Key).png"
    
    $d1Path = Join-Path $dest1 $destFile
    $d2Path = Join-Path $dest2 $destFile
    
    if (Test-Path $srcPath) {
        Copy-Item -Path $srcPath -Destination $d1Path -Force
        Copy-Item -Path $srcPath -Destination $d2Path -Force
        Write-Host "Mapped $($entry.Value) to $destFile"
    } else {
        Write-Host "Source file not found: $($entry.Value)"
    }
}
Write-Host "Mapping complete."
