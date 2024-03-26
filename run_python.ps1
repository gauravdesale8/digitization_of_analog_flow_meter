while ($true) {
    # Run your Python script
    & python main.py

    # Wait for 5 minutes
    # Write-Host "Waiting for 5 minutes..."
    Start-Sleep -Seconds 30  # 300 seconds = 5 minutes
}