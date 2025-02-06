Add-Type -AssemblyName System.Windows.Forms

# Open folder selection dialog
$folderBrowser = New-Object System.Windows.Forms.FolderBrowserDialog
if ($folderBrowser.ShowDialog() -eq "OK") {
    $folderPath = $folderBrowser.SelectedPath

    # Get all files in the selected folder
    Get-ChildItem -Path $folderPath -File | ForEach-Object {
        $oldName = $_.Name
        $newName = $oldName -replace "^icons8_", "" -replace "_", "-" | ForEach-Object { $_.ToLower() }

        # Rename only if the new name is different
        if ($oldName -ne $newName) {
            $newPath = Join-Path $folderPath $newName
            Rename-Item -Path $_.FullName -NewName $newName
            Write-Host "Renamed: $oldName -> $newName"
        }
    }
} else {
    Write-Host "Folder selection was canceled."
}
