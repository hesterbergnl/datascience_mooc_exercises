
The TMC Extension activates on startup if following conditions are met:
    - The TMC Workspace is open in your Visual Studio Code editor
    - TMC-Readme.txt is found in the TMC Workspace root folder (i.e. Exercises).

---
Workspace:
    The Workspace contains all currently open exercises for each course. 
    You can manage the status of the exercises via the TMC extension.

    NB! 
    Please manage, i.e. close, open and download, exercises only via the TMC extension or by using our premade commands. 
    Moving/deleting/renaming folders manually currently breaks the TMC extensions state.
    Files and folders can only be created under the exercise folders, all other will be automatically deleted.
---

These commands can be executed for the TMC exercise that is currently open and active in the VSCode editor.

Commands (VSCode command hotkey: CTRL + SHIFT + P):
    TMC - Menu
    TMC - Run tests
    TMC - Submit solution
    TMC - Reset exercise
    TMC - Close exercise
    TMC - Paste exercise

    TMC - Menu (hotkey: CTRL + SHIFT + A):
        A list of all available commands can also be found under the TMC Menu.

    TMC - Run tests (hotkey: CTRL + SHIFT + T):
        Run exercise tests on your computer.

    TMC - Submit solution
        Send the exercise to the TMC server for testing and grading.

    TMC - Paste exercise
        Send the TMC exercise code to the TMC Pastebin.

    TMC - Reset exercise
        Send the exercise files to the TMC server (for backup) and delete all the exercise files on your computer. 
        Downloads the exercise template from the TMC Server and opens it to the TMC Workspace.

    TMC - Close exercise (hotkey: CTRL + SHIFT + C)
        Closes the exercise folder from the TMC workspace.

    TMC - Get exercise submissions
        You can download old submissions by choosing 'Download old submissions' from the TMC Menu.
    
TMC Extension settings
    You can open the TMC extension settings by pressing the TMC icon on the left sidebar and choose 'Settings' in the TestMyCode extension menu.

    TMC Data
    This is the location where all TMC extension data is saved.  
    Changing the location will create a 'tmcdata' folder to your chosen location and move all the TMC data to the new location.