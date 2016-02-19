function Get-WebPageImages($url, $folder) {
Import-Module BitsTransfer
if (-not (Test-Path $folder)) { md $folder }
$ie = New-Object -COMObject InternetExplorer.Application
$ie.Navigate($url)
while ($ie.Busy) { Start-Sleep -Milliseconds 400 }
$sources = $ie.document.getElementsByTagName('img') | Select-Object -ExpandProperty src
$destinations = $sources | ForEach-Object { "$folder\" }
$displayname = $url.Split('/')[-1]
$ie.Quit()
foreach($image in $sources){
    Start-BitsTransfer $image $folder -Prio High
    }
}