import PySimpleGUI as sg


layout = [
    [sg.Text('Twilio Account SID'), sg.InputText()],     
    [sg.Text('Twilio Account Authorizaton Token'), sg.InputText()],
    [sg.Text('Twilio Account Sending Phone Number'), sg.InputText()],
    [sg.Text('Alert Phone Number'), sg.InputText()],
    [sg.Text('Timeout Period in Seconds'), sg.InputText()],
    [sg.Button('Update')]
]      

window = sg.Window('Dark Souls 3 PVP Alerter', layout)    

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()



# GUI design:
    # user inputs
        # all 4 twilio settings
            # account_sid
            # auth_token
            # twilio_number
            # target_number
        # program settings
            # ds3 window/monitor resolution
            # timeout period
    # display
        # current values for all settings
        # log showing events and times for them
        # (maybe) something to verify which monitor is main one