import pyautogui
import twilio



if __name__ == "__main__":
    while True:
        try: 
            # speed this up by passing regions to check based on screen width and height
            invading_image = pyautogui.locateOnScreen('invading.png')
        except pyautogui.ImageNotFoundException:
            pass
        print("found?")