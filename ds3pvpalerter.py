from mimetypes import init
from re import search
from charset_normalizer import detect
import pyautogui
import keys
import twilio.rest
import time


# Important to get the region to search for because it drastically speeds up the search time.
# The in-game notification will blink off before the program can find it if this is not used.
def get_search_region():
    """Return the appropriate search region based on resolution of monitor."""
    # Will update this with a dictionary mapping different resolutions in the future. Probably.
    # 2560x1440p is the only resolution that works currently.
    # May need to figure out a way to get resolution of game window instead of monitor.
    screen_width, screen_height = pyautogui.size()
    wqhd_region = (675, 965, 600, 10)
    if screen_width == 2560 and screen_height == 1440:
        return wqhd_region

# Searches the given region for the "pvp_notification_bar.png" image in same directory as program.
# This image just matches the top left part of the notification banner's "bar".
# Couldn't find any other messages appearing in this zone with this bar besides PVP events.
# Likely can speed this up by just testing pixels in a line where the banner bar should be based on resolution.
def invasion_detected(search_region):
    """Return true if PVP Event Notification is currently on the screen."""
    val = pyautogui.locateOnScreen(image='pvp_notification_bar.png', region=search_region, grayscale=True, confidence=0.8)
    if val != None:
        print(val)
        return True
    else:
        return False

def send_invasion_alert(client):
    """Send a text message indicating a PVP Event has been detected with the given Twilio rest client object."""
    client.messages.create(
        body="PVP Event Detected!",
        from_=keys.twilio_number,
        to=keys.target_number
    )


if __name__ == "__main__":
    # Print out Just for logging purposes to know it's working and to verify number.
    print(f"Starting DS3 PvP Alerter!\nTarget Number is {keys.target_number}")
    search_region = get_search_region()
    twilio_client = twilio.rest.Client(keys.account_sid, keys.auth_token)
    while True:
        if invasion_detected(search_region):
            # Print out for logging and testing purposes.
            print("PVP Event Detected!")
            send_invasion_alert(twilio_client)
            # Timeout is needed because notification pops up 3 times for many frames.
            # Program will send a huge amount of text messages without this for a single invasion.
            # 60 seconds *should* be short enough to catch a second pvp event, might need to shorten.
            time.sleep(60)
            print("Timeout period over. Searching again.")