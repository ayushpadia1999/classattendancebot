import pyautogui
import webbrowser
import time
import os

def attendclass(url,time_hour,duration = 1,print_waitTime=True):
    wait_time = 10
    if time_hour not in range(0,25):
        print("Invalid time format")
    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour*3600 + 660)
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    if currhr == 0:
        currhr = 24

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    if lefttm <= 0:
        lefttm = 86400+lefttm
    sleeptm = lefttm-wait_time
    if print_waitTime :
        print(f"In {sleeptm} seconds meet.google.com will open and after {wait_time} seconds meeting will be joined")
    time.sleep(sleeptm)
    webbrowser.open(url, new=1)
    time.sleep(10)
    pyautogui.click(1761, 180)
    time.sleep(10)
    x, y = pyautogui.locateCenterOnScreen('kiit.png',confidence = 0.5 , grayscale =True)
    pyautogui.click(x, y)
    time.sleep(10)
    pyautogui.hotkey('ctrl', 'e')
    pyautogui.hotkey('ctrl', 'd')
    pyautogui.click(1346, 659)
    time.sleep(duration*3600)
    width,height = pyautogui.size()
    pyautogui.click(width/2,height/2)
    xy = None 
    while xy is None:
        xy=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'end.png'),grayscale=True)
    pyautogui.click(xy)


def attendclasszoom(url,time_hour,class_time = 1,print_waitTime=True):
    wait_time = 10
    if time_hour not in range(0,25):
        print("Invalid time format")
    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour*3600 + 1320)
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    if currhr == 0:
        currhr = 24

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    if lefttm <= 0:
        lefttm = 86400+lefttm
    sleeptm = lefttm-wait_time
    if print_waitTime :
        print(f"In {sleeptm} seconds meet.google.com will open and after {wait_time} seconds meeting will be joined")
    time.sleep(sleeptm)
    webbrowser.open(url, new=1)
    time.sleep(1)
    xy=None
    while xy is None:
        xy=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'launch.png'),grayscale=True)
    pyautogui.click(xy)
    time.sleep(1)
    xy1 =None
    while xy1 is None:
        xy1=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'joinaudio.png'),grayscale=True)    
    pyautogui.click(xy1)
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('alt', 'f')

    # xy = None 
    # while xy is None:
    #     xy=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'end.png'),grayscale=True)
    # pyautogui.click(xy)

if __name__ == '__main__':
    attendclasszoom('https://us04web.zoom.us/j/78187835202?pwd=R1p4Z0ovdnpqVEdHQktJWHg1K3JvZz09' ,23) 
