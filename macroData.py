from enum import Enum
import time

class RecordType(Enum):
    MOUSE_MOVE = 1
    MOUSE_CLICK = 2
    MOUSE_DRAG = 3
    KEYBOARD_PRESS = 4
    KEYBOARD_WORD = 5


class MacroRecord:
    def __init__(self, type : RecordType, timestamp):
        self.type = type
        self.timestamp = timestamp
        
    def __lt__(self, other):
        return self.timestamp < other.timestamp
    
    def __le__(self, other):
        return self.timestamp <= other.timestamp
      
        
        
class MouseRecord(MacroRecord):
    def __init__(self, type : RecordType, timestamp):
        super().__init__(type, timestamp)
        
        
class MouseMoveRecord(MouseRecord):
    def __init__(self, timestamp, coord):
        super().__init__(RecordType.MOUSE_MOVE, timestamp)
        self.coord = coord
        
        
class MouseClickRecord(MouseRecord):
    def __init__(self, timestamp, coord, button):
        super().__init__(RecordType.MOUSE_CLICK, timestamp)
        self.coord = coord
        self.button = button
    
    def __repr__(self):
        return f"Mouse Click -> Button : {self.button} / Coordinate : {self.coord} / Time : {self.timestamp}"
        
        
class MouseDragRecord(MouseRecord):
    def __init__(self, timestamp, beforeCoord, afterCoord):
        super().__init__(RecordType.MOUSE_DRAG, timestamp)
        self.beforeCoord = beforeCoord
        self.afterCoord = afterCoord


class KeyboardMacro(MacroRecord):
    def __init__(self, type : RecordType, timestamp):
        super().__init__(type, timestamp)
        
        
class KeyboardPressMacro(KeyboardMacro):
    def __init__(self, timestamp, keyCode, keyName, mode):
        super().__init__(RecordType.KEYBOARD_PRESS, timestamp)
        self.keyCode = keyCode
        self.keyName = keyName
        self.mode = mode
        
    def __repr__(self):
        return f"Keyboard Press -> Key Name : {self.keyName} / Key Code : {self.keyCode} / Mode : {self.mode} / Time : {self.timestamp}"
        
        
class KeyboardWordMacro(KeyboardMacro):
    def __init__(self, timestamp, inputString):
        super().__init__(RecordType.KEYBOARD_WORD, timestamp)
        self.inputString = inputString