from mimetypes import init
from re import search
from charset_normalizer import detect
import pyautogui
import keys
import twilio.rest
import time

def get_search_region():
    screen_width, screen_height = pyautogui.size()
    wqhd_region = (675, 965, 600, 10)
    if screen_width == 2560 and screen_height == 1440:
        return wqhd_region

def invasion_detected(search_region):
    val = pyautogui.locateOnScreen(image='pvp_notification_bar.png', region=search_region, grayscale=True)
    if val != None:
        print(val)
        return True
    else:
        return False

def send_invasion_alert(client):
    client.messages.create(
        body="PVP Event Started!",
        from_=keys.twilio_number,
        to=keys.target_number
    )


if __name__ == "__main__":
    search_region = get_search_region()
    twilio_client = twilio.rest.Client(keys.account_sid, keys.auth_token)
    while True:
        if invasion_detected(search_region):
            send_invasion_alert(twilio_client)
            time.sleep(45)