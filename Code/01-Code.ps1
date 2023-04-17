# Automatic OS Updates
# https://pureinfotech.com/install-windows-10-update-powershell/

Install-Module PSWindowsUpdate
Get-WindowsUpdate -AcceptAll -Install -AutoReboot

Write-Host "Updates are completed" 