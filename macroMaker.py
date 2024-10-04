import keyboard
import mouse
import time
from enum import Enum, auto
import mouse._mouse_event
from macroData import *
import pickle
import json

capturedData = []

def printLog(callback):
    def wrappedCallback(event):
        record = callback(event)
        print(record)
        return record
    return wrappedCallback

@printLog
def keyPressCallback(event):
    newKeyPressRecord = KeyboardPressMacro(event.time, event.scan_code, event.name, event.event_type)
    capturedData.append(newKeyPressRecord)
    return newKeyPressRecord

@printLog
def mouseClickCallback(event):
    newMouseClickRecord = MouseClickRecord(event.time, mouse.get_position(), event.button)
    capturedData.append(newMouseClickRecord)
    return newMouseClickRecord
    

if __name__== '__main__':
    print("F4를 눌러 매크로 캡쳐를 시작할 수 있고, F3를 눌러 중지할 수 있습니다.")
    keyboard.wait('F4', suppress=True)
    print("\n매크로 캡쳐를 시작합니다")
    keyTemp = keyboard.on_press(keyPressCallback, suppress=False)
    mouseTemp = mouse.on_click(mouseClickCallback)
    
    keyboard.wait('F3', suppress=True)
    keyboard.unhook_all()
    mouse.unhook_all()
    print("\n매크로 캡쳐를 종료합니다.")
    
    wantToSave = input("매크로 데이터가 생성되었습니다. 파일로 저장하시겠습니까?(Y : 저장 / 그외 : 저장하지 않음) : ")
    if wantToSave == "y" or wantToSave == "Y":
        filename = input("파일 이름을 입력하세요 : ") + ".macdat"
        with open(filename, "w") as data:
            json.dump(capturedData, data)
            #pickle.dump(capturedData, data)
            print(f"{filename}으로 매크로 데이터가 저장되었습니다.")
        
        with open(filename, "r") as data:
            
            print("test : ", json.load(capturedData, data))

    print("프로그램 종료")
    
        
    



