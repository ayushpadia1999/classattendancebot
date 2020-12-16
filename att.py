import pyautogui
import webbrowser
import time
import os

def attendclass(url,time_hour,duration = 1,print_waitTime=False):
    n = 20
    pyautogui.FAILSAFE =True
    wait_time = 10
    if time_hour not in range(0,25):
        print("Invalid time format")
    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour*3600 )
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    if currhr == 0:
        currhr = 24

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    if lefttm <= -3600:
        lefttm = 86400+lefttm
    sleeptm = max(lefttm-wait_time,0)
    if print_waitTime :
        print(f"In {sleeptm} seconds meet.google.com will open and after {wait_time} seconds meeting will be joined")
    time.sleep(sleeptm)
    webbrowser.open(url)
    time.sleep(5)
    pyautogui.click(1761, 180)
    time.sleep(10)
    x, y = pyautogui.locateCenterOnScreen('kiit.png',confidence = 0.5 , grayscale =True)
    pyautogui.click(x, y)
    time.sleep(10)
    pyautogui.hotkey('ctrl', 'e')
    pyautogui.hotkey('ctrl', 'd')
    pyautogui.click(1346, 659)
    time.sleep(5)
    xy1 = None 
    i=0
    while xy1 is None and i<n:
        i = i+1
        xy1=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'msg.png'),confidence= 0.7 ,grayscale=True)
    pyautogui.click(xy1)
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec
    i=0
    xy2 = None
    while i<(duration*3600 + callsec - ((currhr*3600)+(currmin*60)+(currsec))):
        i = i + 200
        # print(i)
        time.sleep(200)
        xy2 = pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'form.png'),grayscale=False)
        if xy2!=None:
            # print(xy2)
            pyautogui.click(xy2)
        # print(xy2)
    width,height = pyautogui.size()
    pyautogui.click(width/2,height/2)
    xy = None 
    i=0
    while xy is None and i<n:
        i = i+1
        xy=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'end.png'),grayscale=True)
    pyautogui.click(xy)


def attendclasszoom(url,time_hour,duration = 1,passcode = None,print_waitTime=False):
    n = 20
    pyautogui.FAILSAFE =True
    pyautogui.press('win')
    pyautogui.write('zoom')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('alt' , 'f4')
    wait_time = 10
    if time_hour not in range(0,25):
        print("Invalid time format")
    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour*3600)
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    if currhr == 0:
        currhr = 24

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    if lefttm <= -3600:
        lefttm = 86400+lefttm
    sleeptm = max(lefttm-wait_time,0)
    if print_waitTime :
        print(f"In {sleeptm} seconds zoom.com will open and after {wait_time} seconds meeting will be joined")
    time.sleep(sleeptm)
    webbrowser.open(url, new=1)
    time.sleep(1)
    xy=None
    i=0
    while xy is None and i<n:
        i = i+1
        xy=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'launch.png'),grayscale=True)
    pyautogui.click(xy)
    time.sleep(5)
    if passcode!=None:
        pyautogui.write(passcode)
        pyautogui.press('enter')
    xy1 =None
    while xy1 is None:
        xy1=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'join.png'),grayscale=True)  
    pyautogui.click(xy1)
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('alt', 'f4')
    xy2 =None
    i=0
    while xy2 is None and i<n:
        i = i+1
        xy2=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'expand.png'),grayscale=True)
    pyautogui.click(xy2)
    pyautogui.hotkey('alt', 'h')
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec
    print(duration*3600 + callsec - ((currhr*3600)+(currmin*60)+(currsec)))
    xy3 = None
    i = 0
    while i<(duration*3600 + callsec - ((currhr*3600)+(currmin*60)+(currsec))):
        i = i + 200
        print(i)
        time.sleep(200)
        xy3 = pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'formzoom.png'),grayscale=False)
        if xy3!=None:
            pyautogui.click(xy3)
            break

        ## UNTESTED CODE HERE TO ENTER ROLL WHEN ROLL NUMBERS FOUND
        # if len(list(pyautogui.locateAllOnScreen('roll.png'))) > 5:
        #     pyautogui.write('1828061')
        #     pyautogui.hotkey('alt', 'q')
        #     time.sleep(1)
        #     pyautogui.click(x=1015, y=480)
    # time.sleep(duration*3600 + callsec - ((currhr*3600)+(currmin*60)+(currsec)))
    pyautogui.hotkey('alt', 'q')
    time.sleep(1)
    pyautogui.click(x=1015, y=480)

def attendtnp(time_hour,duration = 1,print_waitTime=True):
    n=10
    wait_time = 10
    if time_hour not in range(0,25):
        print("Invalid time format")
    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour*3600)
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    if currhr == 0:
        currhr = 24

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    if lefttm <= -3600:
        lefttm = 86400+lefttm
    sleeptm = max(lefttm-wait_time,0)
    if print_waitTime :
        print(f"In {sleeptm} seconds zoom.com will open and after {wait_time} seconds meeting will be joined")
    time.sleep(sleeptm)
    webbrowser.open('https://web.whatsapp.com',new = 1)
    time.sleep(5)
    xy5 = None
    while xy5 is None:
        xy5 = pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'searchbarwhatsapp.png'),grayscale=True,confidence = 0.9)  
    pyautogui.click(xy5)
    pyautogui.write("CAAS")
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    xy6 =None
    while xy6 is None:
        xy6=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'whatsappsearch.png'),grayscale=True)  
    pyautogui.click(xy6)
    time.sleep(1)
    pyautogui.write("zoom")
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    x =None
    y= None
    while x is None:
        x , y =pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'whatsappzoomjoin.png'),grayscale=True)  
    pyautogui.click(x,y)

    time.sleep(1)
    xy=None
    i=0
    while xy is None and i<n:
        i = i+1
        xy=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'launch.png'),grayscale=True)
    pyautogui.click(xy)
    xy1 =None
    while xy1 is None:
        xy1=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'join.png'),grayscale=True)  
    pyautogui.click(xy1)
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('alt', 'f4')
    xy2 =None
    i=0
    while xy2 is None and i<n:
        i = i+1
        xy2=pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'expand.png'),grayscale=True)
    pyautogui.click(xy2)
    pyautogui.hotkey('alt', 'h')
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec
    print(duration*3600 + callsec - ((currhr*3600)+(currmin*60)+(currsec)))
    xy3 = None
    i = 0
    while i<(duration*3600 + callsec - ((currhr*3600)+(currmin*60)+(currsec))):
        i = i + 200
        print(i)
        time.sleep(200)
        xy3 = pyautogui.locateCenterOnScreen(os.path.join(os.getcwd(),'formzoom.png'),grayscale=False)
        if xy3!=None:
            pyautogui.click(xy3)
            break

        ## UNTESTED CODE HERE TO ENTER ROLL WHEN ROLL NUMBERS FOUND
        # if len(list(pyautogui.locateAllOnScreen('roll.png'))) > 5:
        #     pyautogui.write('1828061')
        #     pyautogui.hotkey('alt', 'q')
        #     time.sleep(1)
        #     pyautogui.click(x=1015, y=480)
    # time.sleep(duration*3600 + callsec - ((currhr*3600)+(currmin*60)+(currsec)))
    pyautogui.hotkey('alt', 'q')
    time.sleep(1)
    pyautogui.click(x=1015, y=480)


 
if __name__ == '__main__':
    # attendclasszoom('https://us04web.zoom.us/j/77562208299?pwd=Vy9mVkRnT2tCaTQ3YnlJaGVNVWkzUT09' ,16,duration=2 ,passcode= '2QPsnb', print_waitTime=True) 
    #url must contain https: or else script opens Edge/ Explorer
    attendtnp(18.75)

