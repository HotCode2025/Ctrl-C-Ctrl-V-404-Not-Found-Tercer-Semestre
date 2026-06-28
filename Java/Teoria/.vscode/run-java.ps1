param(
    [Parameter(Mandatory = $true)][string]$FullFilePath
)

$FullFilePath = $FullFilePath.Trim()
while ($FullFilePath.Length -gt 0 -and ($FullFilePath[0] -eq '"' -or $FullFilePath[0] -eq "'")) {
    $FullFilePath = $FullFilePath.Substring(1)
}
while ($FullFilePath.Length -gt 0 -and ($FullFilePath[-1] -eq '"' -or $FullFilePath[-1] -eq "'")) {
    $FullFilePath = $FullFilePath.Substring(0, $FullFilePath.Length - 1)
}

$sourceDir = [System.IO.Path]::GetDirectoryName($FullFilePath)
$fileName = [System.IO.Path]::GetFileName($FullFilePath)
$className = [System.IO.Path]::GetFileNameWithoutExtension($fileName)

Set-Location -LiteralPath $sourceDir
$package = Split-Path -Leaf (Get-Location).Path
Set-Location ..
javac -encoding UTF-8 "$package/$fileName"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
java "${package}.${className}"
