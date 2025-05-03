import pyautogui
import keyboard
import time

# 操作延迟（每个操作间的间隔）
default_delay = 0.5

# 模拟鼠标点击
def mouse_click(x, y):
    pyautogui.click(x, y)
    time.sleep(default_delay)

# 模拟键盘操作（单个按键）
def keyboard_press(key):
    keyboard.press_and_release(key)
    time.sleep(default_delay)

# 模拟键盘组合键（例如 Ctrl+S）
def keyboard_hotkey(key1, key2):
    keyboard.press_and_release(f"{key1}+{key2}")
    time.sleep(default_delay)

# 执行操作
def perform_action(action):
    action_parts = action.split()
    command = action_parts[0]

    if command == 'mouse_click':
        # 鼠标点击操作，格式：mouse_click x y
        x, y = int(action_parts[1]), int(action_parts[2])
        print(f"执行鼠标点击: ({x}, {y})")
        mouse_click(x, y)

    elif command == 'keyboard_press':
        # 键盘单个按键操作，格式：keyboard_press key
        key = action_parts[1]
        print(f"执行键盘按键: {key}")
        keyboard_press(key)

    elif command == 'keyboard_hotkey':
        # 键盘组合键操作，格式：keyboard_hotkey key1 key2
        key1, key2 = action_parts[1], action_parts[2]
        print(f"执行键盘组合键: {key1} + {key2}")
        keyboard_hotkey(key1, key2)

    else:
        print(f"未知命令: {command}")

# 测试用例：模拟鼠标点击和键盘操作
actions = [
    "mouse_click 129 250",      # 模拟鼠标点击 (129, 250)
    "keyboard_press f1",        # 模拟按下 F1 键
    "keyboard_press r",         # 模拟按下 r 键
    "keyboard_hotkey ctrl s",   # 模拟按下 Ctrl+S
]

for action in actions:
    perform_action(action)

