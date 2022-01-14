# ds3pvpalerter
Sends a text message to your cell alerting you of pvp events in dark souls 3.
(This project is still in a very early stage and requires some technical knowledge to install/setup.)

Installation:
    Install python 3.10 and the following packages:
        pyautogui
        twilio-python

How to use:
    Create a twilio trial account here: https://www.twilio.com/
    Add a trial phone number to your account.
    Create a file named "keys.py" in the folder these files are in.
    Open the "keys.py" file you created and copy the following 4 lines into it:
        account_sid = ''
        auth_token = ''
        twilio_number = ''
        target_number = ''
    Remove any indentation in the keys.py file.
    Find your account sid, auth token, and twilio number within your twilio account page.
    Copy each of these strings into the keys.py file between the single quotationi marks (').
    Enter your target number (with country code) into the target_number field in keys.py.
    Verify the monitor you are playing Dark Souls 3 on is your Operating System's "main" monitor.
    Run ds3pvpalerter.py on your second monitor.
    You will see log messages when events occur including a message when the program has started.