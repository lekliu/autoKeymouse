import pyautogui
import time
import keyboard  # 用于捕捉键盘事件

# 执行鼠标点击操作
def mouse_click(x, y, default_delay):
    print(f"执行鼠标点击: ({x}, {y})")
    pyautogui.click(x, y)
    time.sleep(default_delay)

# 执行键盘按键操作
def keyboard_press(key, default_delay):
    print(f"执行键盘按键: {key}")
    keyboard.press_and_release(key)
    time.sleep(default_delay)

# 执行键盘组合键操作（例如 Ctrl+S）
def keyboard_hotkey(key1, key2, default_delay):
    print(f"执行键盘组合键: {key1} + {key2}")
    keyboard.press_and_release(f"{key1}+{key2}")
    time.sleep(default_delay)

# 执行每个命令
def perform_action(action, default_delay):
    action_parts = action.split()
    command = action_parts[0]

    if command == 'mouse_click':
        # 鼠标点击操作，格式：mouse_click x y
        x, y = int(action_parts[1]), int(action_parts[2])
        mouse_click(x, y, default_delay)

    elif command == 'keyboard_press':
        # 键盘单个按键操作，格式：keyboard_press key
        key = action_parts[1]
        keyboard_press(key, default_delay)

    elif command == 'keyboard_hotkey':
        # 键盘组合键操作，格式：keyboard_hotkey key1 key2
        key1, key2 = action_parts[1], action_parts[2]
        keyboard_hotkey(key1, key2, default_delay)

    elif command == 'delay':
        # 停顿操作，格式：delay
        print(f"执行延迟: {default_delay}秒")
        time.sleep(default_delay)

    else:
        print(f"未知命令: {command}")

def read_actions_from_file(file_path):
    with open(file_path, 'r') as file:
        actions = file.readlines()
    return [action.strip() for action in actions if action.strip()]

def get_current_mouse_position():
    # 获取当前鼠标的位置
    x, y = pyautogui.position()
    print(f"当前鼠标位置: ({x}, {y})")
    return x, y

def main():
    repeat_count = 1  # 默认执行一次
    actions = []
    default_delay = 0.1  # 默认每条命令执行后的短暂停顿
    round_delay = 1  # 默认一轮操作执行完后的长暂停顿

    # 读取配置文件
    file_path = "actions.txt"
    lines = read_actions_from_file(file_path)

    # 解析repeat、default_delay、round_delay配置
    for line in lines:
        if line.startswith('repeat'):
            repeat_count = int(line.split()[1].strip())
        elif line.startswith('default_delay'):
            default_delay = float(line.split()[1].strip())
        elif line.startswith('round_delay'):
            round_delay = float(line.split()[1].strip())
        else:
            actions.append(line)

    # 执行操作
    print("开始执行操作...")

    for _ in range(repeat_count):
        for action in actions:
            perform_action(action, default_delay)

            # 每条命令执行后进行统一延迟
            time.sleep(default_delay)

        # 每轮操作执行完后，进行长暂停
        print(f"一轮操作执行完毕，暂停 {round_delay} 秒...")
        time.sleep(round_delay)

    # 操作执行完毕后，开始捕捉键盘事件
    print("操作执行完毕，开始捕捉键盘事件。按空格键查看当前鼠标位置，按ESC键退出。")

    # 开始执行键盘监听循环
    while False:
        if keyboard.is_pressed('space'):
            # 按下空格键时打印鼠标位置
            get_current_mouse_position()
            time.sleep(0.5)  # 防止多次打印

        if keyboard.is_pressed('esc'):
            print("检测到ESC键，程序退出。")
            break

if __name__ == "__main__":
    main()
    # 当前鼠标位置: (3315, 449)
    # 当前鼠标位置: (4680, 482)
    # 当前鼠标位置: (3192, 1226)
    # 当前鼠标位置: (4677, 1215)

