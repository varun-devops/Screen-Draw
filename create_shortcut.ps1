$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$Home\Desktop\WebtroopsScreen Draw.lnk")
$Shortcut.TargetPath = "pythonw.exe"
$Shortcut.Arguments = "D:\screenDraw\draw.py"
$Shortcut.WorkingDirectory = "D:\screenDraw"
$Shortcut.Description = "WebtroopsScreen Draw Tool"
$Shortcut.IconLocation = "shell32.dll,22"
$Shortcut.HotKey = "CTRL+ALT+W"
$Shortcut.Save()
Write-Host "Shortcut created on your desktop with hotkey CTRL+ALT+W"
Write-Host "You can now press CTRL+ALT+W from anywhere to launch the screen drawing tool"
