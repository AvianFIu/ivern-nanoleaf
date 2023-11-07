from nanoleafapi import Nanoleaf, RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, PINK, PURPLE, WHITE
import requests

#initialize nanoleaf var
nl = Nanoleaf("192.168.0.90")

currentColor = "temp"

#league client data
json_link = "https://127.0.0.1:2999/liveclientdata/allgamedata"

#checking the league client data and changing colors under certain changes
while True:
    isDaisyOut = requests.get(json_link, verify=False).json()["activePlayer"]["abilities"]["R"]["id"]

    #currentMana = requests.get(json_link, verify=False).json()["activePlayer"]["championStats"]["resourceValue"]

    #want to find a way to use mana to determine when I casted the shield
    #if currentMana < 1016:
        #if currentColor != "pink":
           # nl.set_color(PINK)
            #nl.set_brightness(50)
           # currentColor = "pink"

    #if iverns ult data is named "IvernRRecast" we know daisy is out
    if isDaisyOut == "IvernRRecast":
        print(isDaisyOut)

        if currentColor != "green":
            nl.set_color(GREEN)
            nl.set_brightness(50)
            currentColor = "green"
    #default color
    else:
        if currentColor != "blue":
            nl.set_color(BLUE)
            nl.set_brightness(50)
            currentColor = "blue"