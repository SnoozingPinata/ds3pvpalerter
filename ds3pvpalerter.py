from mimetypes import init
from charset_normalizer import detect
import pyautogui
import keys
import twilio.rest
# twilio.rest.client


def invasion_detected():
    while True:
        try: 
            # speed this up by passing regions to check based on screen width and height
            invading_image = pyautogui.locateOnScreen('invading.png', grayscale=True, region=(0,0,400,400))
        except pyautogui.ImageNotFoundException:
            break
    return True

def send_invasion_alert(client):
    client.messages.create(
        body="Invasion Found!!!",
        from_=keys.twilio_number,
        to=keys.target_number
    )


if __name__ == "__main__":
    client = twilio.rest.Client(keys.account_sid, keys.auth_token)
    if invasion_detected():
        print("True")
        #send_invasion_alert(client)
    else:
        print("False")