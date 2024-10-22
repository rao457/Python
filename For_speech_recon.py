from fnmatch  import fnmatch
application = {
    "chrome" : "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "notepad" : "notepad.exe",
        "Grand Theft Auto V" : "C:\\Program Files (x86)\\Grand Theft Auto V\\GTAVLauncher.exe",
        "Visual Studio Code" : "D:\\PS\\Microsoft VS Code\\Code.exe",
        "Docker Desktop" : "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe",
}
Heard = ''
listened = "Hey jarvis, open chrome for me."
for key in application.keys():
    if key in listened:
        Heard += key
print(f"Heard: {Heard}")
