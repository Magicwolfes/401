# Sierra Maldonado worked with Geneva, Justin H, and Nick A
# Automatic OS Updates
# https://pureinfotech.com/install-windows-10-update-powershell/
# https://www.nakivo.com/blog/automate-windows-updates-using-powershell-short-overview/

Install-Module PSWindowsUpdate
Get-WindowsUpdate -AcceptAll -Install -AutoReboot

Write-Host "Updates are completed" 