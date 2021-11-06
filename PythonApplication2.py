import time
import pyautogui
import _thread as thread
import threading

mutex = threading.Lock()

actionOrder = { "chancelor" : "advisor", "advisor" : "processions", "processions" : "maidens", "maidens" : "kingdom", "kingdom" : "chancelor" }

def main():
    time.sleep(10)
    calibrate = pyautogui.locateAllOnScreen("Calibrate.png", confidence=0.95)
    kingdom = pyautogui.locateAllOnScreen("Kingdom.png", confidence=0.95)
    kingdomList = []
    for k in kingdom:
        kingdomList += [k]
    print("calibrate:")
    screenRect = []
    for p in calibrate:
        smallestDiffKingdom = 0
        smallestDiff = 99999
        for k in kingdomList:
            diff = k.left - p.left
            if diff < smallestDiff and diff > 0:
                smallestDiff = diff
                smallestDiffKingdom = k
        screenRect.append({"left" : p.left, "top" : p.top, "width" : smallestDiff + k.height + 2, "height" : (k.top - p.top) + k.height + 2 })
    print(screenRect)
    threadIndex = 0
    for rect in screenRect:
        thread.start_new_thread(run, (rect["left"], rect["top"], rect["width"], rect["height"], threadIndex))
        threadIndex += 1
    while(True):
        pass
    
def run(top, left, width, height, threadIndex):
    print("I am alive " + str(top) + " " + str(left))
    region = (top, left, width, height)
    whereAmI = "courtyard"
    pyautogui.FAILSAFE = False
    startTime = time.time()
    whatNow = "kingdom"
    while (True):
        print (str(threadIndex) + " " + whereAmI + " -> " + whatNow)
        time.sleep(3)
        if whereAmI is "chancelor":
            if whatNow is "chancelor":
                whatNow = chancelor(region, whatNow)
                continue
            else:
                pos = pyautogui.locateOnScreen('Back.png', confidence=(0.7), region=region)
                if pos is not None:
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    whereAmI = "throne room"
                    continue
        if whereAmI is "throne room":
            if whatNow is "chancelor":
                pos = pyautogui.locateOnScreen('Chancelor.png', confidence=(0.7), region=region)
                if pos is not None:
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    whereAmI = "chancelor"
                    continue
            elif whatNow is "advisor":
                pos = pyautogui.locateOnScreen('Advisor.png', confidence=(0.7), region=region)
                if pos is not None:
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    whereAmI = "advisor"
                    continue
            else:
                pos = pyautogui.locateOnScreen('Back.png', confidence=(0.7), region=region)
                if pos is not None:
                    whereAmI = "courtyard"
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    continue
        if whereAmI is "advisor":
            if whatNow is "advisor":
                whatNow = advisor(region, whatNow)
            else:
                pos = pyautogui.locateOnScreen('Back.png', confidence=(0.7), region=region)
                if pos is not None:
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    whereAmI = "throne room"
                    continue
        if whereAmI is "courtyard":
            if whatNow is "chancelor" or whatNow is "advisor":
                pos = pyautogui.locateOnScreen('ThroneRoom.png', confidence=(0.7), region=region)
                if pos is not None:
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    whereAmI = "throne room"
                    continue
            elif whatNow is "processions":
                pos = pyautogui.locateOnScreen('Processions.png', confidence=(0.7), region=region)
                if pos is not None:
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    whereAmI = "procession"
                    continue
            elif whatNow is "maidens":
                pos = pyautogui.locateOnScreen('MaidenChambers.png', confidence=(0.7), region=region)
                if pos is not None:
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    whereAmI = "chambers"
                    continue
            elif whatNow is "kingdom":
                pos = pyautogui.locateOnScreen('Kingdom.png', confidence=(0.7), region=region)
                if pos is not None:
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    whereAmI = "kingdom"
                    continue
                else:
                    whatNow = actionOrder["kingdom"]
        if whereAmI is "procession":
            if whatNow is "processions":
                whatNow = processions(region, whatNow)
            else:
                pos = pyautogui.locateOnScreen('Back.png', confidence=(0.7), region=region)
                if pos is not None:
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    whereAmI = "courtyard"
                    continue
        if whereAmI is "chambers":
            if whatNow is "maidens":
                pos = pyautogui.locateOnScreen('Maidens.png', confidence=(0.7), region=region)
                if pos is not None:
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    whereAmI = "maidens"
                    time.sleep(1)
                    continue
            else:
                pos = pyautogui.locateOnScreen('Back.png', confidence=(0.7), region=region)
                if pos is not None:
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    whereAmI = "courtyard"
                    continue
        if whereAmI is "maidens":
            if whatNow is "maidens":
                whatNow = maidens(region, whatNow, top, left)
            else:
                pos = pyautogui.locateOnScreen('Back.png', confidence=(0.7), region=region)
                if pos is not None:
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    whereAmI = "chambers"
                    continue
        if whereAmI is "kingdom":
            if whatNow is "kingdom":
                whatNow = kingdom(region, whatNow)
            else:
                pos = pyautogui.locateOnScreen('Back.png', confidence=(0.7), region=region)
                if pos is not None:
                    mutex.acquire()
                    pyautogui.click(pos)
                    mutex.release()
                    time.sleep(1)
                    pos = pyautogui.locateOnScreen('Back.png', confidence=(0.7), region=region)
                    if pos is not None:
                        mutex.acquire()
                        pyautogui.click(pos)
                        mutex.release()
                        whereAmI = "courtyard"
                        continue


def chancelor(region, whatNow):
    NoCollectLeft = False
    NoRecruitLeft = False
    while not NoCollectLeft or not NoRecruitLeft:
        pos = pyautogui.locateOnScreen('Collect.png', confidence=(0.8), region=region)
        if pos is not None:
            posAll = pyautogui.locateOnScreen('CollectAll.png', confidence=(0.7), region=region)
            if posAll is not None:
                mutex.acquire()
                pyautogui.click(posAll)
                mutex.release()
                NoCollectLeft = True
                NoRecruitLeft = True
                continue
            mutex.acquire()
            pyautogui.click(pos)
            mutex.release()
            time.sleep(1)
        else:
            NoCollectLeft = True
        pos = pyautogui.locateOnScreen('Recruit.png', confidence=(0.7), region=region)
        if pos is not None:
            mutex.acquire()
            pyautogui.click(pos)
            mutex.release()
            time.sleep(1)
        else:
            NoRecruitLeft = True
    print("agter loop")
    return actionOrder["chancelor"]

def advisor(region, whatNow):
    checkAnother = True
    while checkAnother:
        time.sleep(1)
        checkAnother = False
        pos = pyautogui.locateOnScreen('Gold.png', confidence=(0.7), region=region)
        if pos is not None:
            mutex.acquire()
            pyautogui.click(pos)
            mutex.release()
            checkAnother = True
            continue
        pos = pyautogui.locateOnScreen('Grain.png', confidence=(0.7), region=region)
        if pos is not None:
            mutex.acquire()
            pyautogui.click(pos)
            mutex.release()
            checkAnother = True
            continue
        pos = pyautogui.locateOnScreen('Soldiers.png', confidence=(0.7), region=region)
        if pos is not None:
            mutex.acquire()
            pyautogui.click(pos)
            mutex.release()
            checkAnother = True
            continue
        pos = pyautogui.locateOnScreen('Tome500.png', confidence=(0.7), region=region)
        if pos is not None:
            mutex.acquire()
            pyautogui.click(pos)
            mutex.release()
            checkAnother = True
            continue
        pos = pyautogui.locateOnScreen('Tome1K.png', confidence=(0.7), region=region)
        if pos is not None:
            mutex.acquire()
            pyautogui.click(pos)
            mutex.release()
            checkAnother = True
            continue
    return actionOrder["advisor"]

def processions(region, whatNow):
    pos = pyautogui.locateOnScreen('Processions2.png', confidence=(0.7), region=region)
    while pos is not None:
        mutex.acquire()
        pyautogui.click(pos)
        mutex.release()
        time.sleep(5)
        pos = pyautogui.locateOnScreen('ProcessionsArrow.png', confidence=(0.7), region=region)
        if pos is not None:
            mutex.acquire()
            pyautogui.click(pos)
            mutex.release()
            continue
        pos = pyautogui.locateOnScreen('Processions2.png', confidence=(0.7), region=region)
    return actionOrder["processions"]

def maidens(region, whatNow, top, left):
    pos = pyautogui.locateOnScreen('RandomVisit.png', confidence=(0.7), region=region)
    while pos is not None:
        mutex.acquire()
        pyautogui.click(pos)
        mutex.release()
        time.sleep(15)
        mutex.acquire()
        pyautogui.click(top + 10, left + 10)
        mutex.release()
        time.sleep(1)
        pos = pyautogui.locateOnScreen('RandomVisit.png', confidence=(0.7), region=region)
    return actionOrder["maidens"]

def kingdom(region, whatNow):
    pos = pyautogui.locateOnScreen('KingdomCarriage.png', confidence=(0.7), region=region)
    while pos is not None:
        mutex.acquire()
        pyautogui.click(pos)
        mutex.release()
        time.sleep(1)
        pos = pyautogui.locateOnScreen('KingdomCarriage.png', confidence=(0.7), region=region)
    pos = pyautogui.locateOnScreen('HumbermoorHighlands.png', confidence=(0.7), region=region)
    if pos is not None:
        mutex.acquire()
        pyautogui.click(pos)
        mutex.release()
        time.sleep(1)
        collect(region)
    return actionOrder["kingdom"]

def collect(region):
    pos = pyautogui.locateOnScreen('Explore.png', confidence=(0.9), region=region)
    if pos is not None:
        mutex.acquire()
        pyautogui.click(pos)
        mutex.release()
        time.sleep(1)
    else:
        return
    pos = pyautogui.locateOnScreen('ClaimAll.png', confidence=(0.8), region=region)
    if pos is not None:
        mutex.acquire()
        pyautogui.click(pos)
        mutex.release()
    claimed = pyautogui.locateAllOnScreen("GrayClaim.png", confidence=(0.9))
    if len(list(claimed)) >= 2:
        pos = pyautogui.locateOnScreen("RefreshQuest.png", confidence=(0.8))
        if pos is not None:
            mutex.acquire()
            pyautogui.click(pos)
            mutex.release()
            time.sleep(1)
    pos = pyautogui.locateAllOnScreen("Send.png", confidence=(0.95))
    for p in pos:
        mutex.acquire()
        pyautogui.click(p)
        mutex.release()
        time.sleep(1)
        pos = pyautogui.locateOnScreen("SendAll.png", confidence=(0.9))
        if pos is not None:
            mutex.acquire()
            pyautogui.click(pos)
            mutex.release()
            time.sleep(1)
        else:
            continue
        pos = pyautogui.locateOnScreen("QuestSend.png", confidence=(0.9))
        if pos is not None:
            mutex.acquire()
            pyautogui.click(pos)
            mutex.release()
            time.sleep(1)
        else:
            continue
        pos = pyautogui.locateOnScreen("QuestConfirm.png", confidence=(0.9))
        if pos is not None:
            mutex.acquire()
            pyautogui.click(pos)
            mutex.release()
            time.sleep(2)

if __name__ == "__main__":
    main()
