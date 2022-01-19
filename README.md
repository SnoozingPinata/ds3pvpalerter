# ds3pvpalerter
Sends a text message to your cell phone alerting you of pvp events in dark souls 3.

**This project is still in an early stage and requires some technical knowledge to install/setup.**

# Installation
- Install python 3.10
- Install PyAutoGUI library: `pip install PyAutoGUI==0.9.53`
- Install twilio library: `pip install twilio-python==7.5.0`

# Setup
- Create a twilio trial account here: https://www.twilio.com/
- Add a trial phone number to your account.
- Rename the "keys_template.py" file to "keys.py"
- Find your account sid, auth token, and twilio number within your twilio account page.
- Copy each of these strings into the keys.py file between the single quotationi marks (').
- Enter your target number (with country code) into the target_number field in keys.py.
- Verify the monitor you are playing Dark Souls 3 on is your Operating System's "main" monitor.

# Use
- Run ds3pvpalerter.py on your second monitor.
- You will see log messages when events occur including a message when the program has started.