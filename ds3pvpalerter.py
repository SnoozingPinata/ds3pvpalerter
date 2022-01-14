from mimetypes import init
from charset_normalizer import detect
import pyautogui
import keys
import twilio.rest
import time


def invasion_detected():
    # speed this up by passing regions to check based on screen width and height
    # image is blinking off before program detects, must add region (possibly grayscale) to catch notice in time.
    val = pyautogui.locateOnScreen('being_summoned_trim.png')
    if val != None:
        print(val)
        return True
    else:
        return False

def send_invasion_alert(client):
    client.messages.create(
        body="Invasion Found!!!",
        from_=keys.twilio_number,
        to=keys.target_number
    )


if __name__ == "__main__":
    screen_width, screen_height = pyautogui.size()
    twilio_client = twilio.rest.Client(keys.account_sid, keys.auth_token)
    while True:
        if invasion_detected():
            send_invasion_alert(twilio_client)
            time.sleep(30)