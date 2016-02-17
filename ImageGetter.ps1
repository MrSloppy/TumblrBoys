# Deze imports zijn nodig:
Import-Module BitsTransfer


$browser = New-Object -ComObject InternetExplorer.Application
$browser.visible = $true
# Zorg ervoor dat je bent ingelogd op Facebook via Internet Explorer en dat hij de credentials onthoud!!!!
$browser.Navigate("https://www.facebook.com/jos.heemels/media_set?set=a.3674561308949.2135949.1422421937&type=3&__mref=message_bubble")

While ($browser.Busy) { 
    Start-Sleep -Milliseconds 800 
}
"Done!"

$browser.Document | Get-Member

$folder = "C:\Users\Public\Pictures\webimages\"

$images = $browser.Document.getElementsByTagName("img") | Select-Object -ExpandProperty src

echo $images

foreach( $image in $images){
    Start-BitsTransfer -Source $image -Destination C:\webimages
}