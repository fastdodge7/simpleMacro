import keyboard
import mouse
import time
from enum import Enum, auto
import mouse._mouse_event
from macroData import *
import pickle
import pyautogui as pag
from macroData import KeyboardPressMacro, MouseClickRecord, RecordType

def executeKeyboardPress(interval, record : KeyboardPressMacro):
    pag.PAUSE = interval
    pag.keyDown(record.keyName)
    
def executeMouseClick(interval, record : MouseClickRecord):
    pag.PAUSE = interval
    pag.click(record.coord)
    
def proceedOneStep(macroData):
    interval = 0.1
    for idx, record in enumerate(macroData):
        if idx > 0:
            interval = macroData[idx].timestamp - macroData[idx - 1].timestamp
            
        if record.type == RecordType.KEYBOARD_PRESS:
            executeKeyboardPress(interval, record)
            
        elif record.type == RecordType.MOUSE_CLICK:
            executeMouseClick(interval, record)

if __name__ == "__main__":
    path = input("매크로 데이터 파일의 이름을 입력하세요(.macdat 포함) : ")
    iterateNum = int(input("반복 횟수를 입력하세요 : "))
    print("매크로 실행 시작. 마우스를 좌측 상단 끝 꼭짓점으로 옮겨 매크로를 강제 중단시킬 수 있습니다.")
    with open(path, "rb") as bin:
        data = pickle.load(bin)
        
        for run in range(iterateNum):
            proceedOneStep(data)
    
    print("매크로 실행 완료.")
            
    



