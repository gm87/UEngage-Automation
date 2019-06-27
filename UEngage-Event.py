from pynput import keyboard
from keyboard import press
import easygui
import pyautogui
import time
import pyperclip

def execute():
    press('backspace')
    opponent = easygui.enterbox("Enter opponent: ")
    teams = ["Volleyball", "Men's Soccer", "Women's Soccer"]
    team = easygui.choicebox("What team?", "Choose a team", teams)
    if (team == "Volleyball" or team=="Men's Soccer" or team=="Women's Soccer"):
        date = easygui.enterbox("Enter match date (MM/DD/YY): ")
        start_time_str = easygui.enterbox("Enter start time (HH:MM A or HH:MM P):")
        end_time_str = start_time_str
        hour_str = start_time_str[0]+start_time_str[1]
        hour_int = int(hour_str, 10)
        hour_int = hour_int+2
        end_time_hour = str(hour_int)
        end_time_str = end_time_hour + end_time_str[2:7]
        if (hour_int>12):
            hour_int = hour_int-12
            end_time_str = end_time_str[0:5] + " " + "P"
            end_time_hour = str(hour_int)
            end_time_str = end_time_hour + end_time_str[2:7]

        pyautogui.typewrite(team + " vs " + opponent)
        press('tab')
        press('down')
        time.sleep(.1)
        press('down')
        press('tab')
        pyautogui.typewrite(team + " takes on " + opponent + "!\nCheck in on Purple Reign Rewards to earn points and get rewarded!\nFollow Purple Reign on Twitter and Instagram @PurpleReignAces")
        press('tab')
        press('tab')
        pyautogui.typewrite(date[0] + date[1] + " " + date[3] + date[4] + " " + date[6] + date[7])
        press('tab')
        time.sleep(.1)
        press('enter')
        time.sleep(.1)
        pyautogui.typewrite(start_time_str + "M")
        time.sleep(.1)
        press('tab')
        pyautogui.typewrite(date[0] + date[1] + " " + date[3] + date[4] + " " + date[6] + date[7])
        press('tab')
        time.sleep(.1)
        press('enter')
        time.sleep(.1)
        pyautogui.typewrite(end_time_str + "M")
        press('tab')
        time.sleep(.1)
        press('enter')
        time.sleep(.8)
        press('tab')
        time.sleep(.1)
        press('enter')
        time.sleep(.1)
        press('tab')
        if (team == "Volleyball" or team == "Women's Basketball"):
            pyautogui.typewrite("Meeks Family Fieldhouse")
        elif (team == "Men's Soccer" or team == "Women's Soccer"):
            pyautogui.typewrite("McCutchan Stadium")
        time.sleep(.1)
        press('tab')
        press('esc')
        time.sleep(.8)
        press('tab')
        time.sleep(.1)
        press('tab')
        time.sleep(.1)
        press('down')
        time.sleep(.1)
        press('tab')
        time.sleep(.1)
        press('tab')
        time.sleep(.1)
        press('enter')
        for x in range (9):
            time.sleep(.1)
            press('down')
        for x in range (4):
            time.sleep(.1)
            press('tab')
        time.sleep(.1)
        press('enter')
        # page two starts here
        time.sleep(3)
        for x in range (12):
            time.sleep(.1)
            press('tab')
        press('enter')
        # page 3 starts here
        time.sleep(3)
        for x in range(8):
            time.sleep(.1)
            press('tab')
        time.sleep(.1)
        press('enter')
        for x in range(5):
            time.sleep(.1)
            press('tab')
        time.sleep(.1)
        press('enter')
        time.sleep(.1)
        pyautogui.typewrite("C:\Program Files\EventHotkey")
        time.sleep(.1)
        press('enter')
        for x in range (5):
            time.sleep(.1)
            press('tab')
        time.sleep(.1)
        if (team == "Volleyball"):
            pyautogui.typewrite("volleyball")
        elif (team == "Men's Soccer"):
            pyautogui.typewrite("msoc")
        elif (team == "Women's Soccer"):
            pyautogui.typewrite("wsoc")
        time.sleep(.1)
        press('down')
        time.sleep(.1)
        press('enter')
        time.sleep(.1)
        press('tab')
        time.sleep(.1)
        press('tab')
        time.sleep(.1)
        press('enter')
    else:
        print("Invalid team name")
        exit
    

def on_press(key):
    if key==keyboard.KeyCode(char='`'):
        execute()

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
