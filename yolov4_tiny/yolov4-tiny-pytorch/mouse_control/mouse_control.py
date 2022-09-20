import pyautogui
import os
import time
import math
pyautogui.FAILSAFE = False
def mouse_move(top, left, bottom, right):
    # print(pyautogui.size()) # Size(width=1920, height=1080) # 16 ： 9
    (width,height) = pyautogui.size()
    std_sencety = 3.5
    my_sencety = 3.5
    h_pov = 68    # CSGO 中的POV视野角度是68
    v_pov = 74
    h_angle_inch = width / h_pov
    v_angle_inch = height / v_pov
    h_deg = h_pov/2
    v_deg = v_pov/2
    h_rad = h_deg * math.pi/180
    v_rad = v_deg * math.pi/180
    h_h = (width/2)/math.tan(h_rad)
    v_h = (height/2)/math.tan(v_rad)
    
    # print(h) # 1423.2585297722308
    # 获取预测框的位置
    # top, left, bottom, right
    # 计算出头部的大概坐标
    head_pos = [((bottom-top)/5 + top),(right+left)/2]
    # 这里注意，坐标的第一个是y,第二个是x
    moveRel = False

    # 移动前选择是否射击
    # 范围可以再精细一点
    # pyautogui.keyDown('shift')
    # pyautogui.keyUp('shift')

    if width/2 > left and width/2 < right and height/2 > top and height/2 < bottom:
        pyautogui.click(clicks=5, interval=0.1)
        # pyautogui.drag(0, 0, 1, button='left') 
    # 计算需要移动的像素
    if (moveRel):
        h_d = head_pos[1] - width/2
        v_d = head_pos[0] - height/2
        h_sita_rad = math.atan(h_d/h_h)
        v_sita_rad = math.atan(v_d/v_h)
        h_sita = h_sita_rad * 180 / math.pi
        v_sita = v_sita_rad * 180 / math.pi

        xOffset = int(h_sita * h_angle_inch)
        yOffset = int(v_sita * v_angle_inch)
        num_seconds = 0.001
        pyautogui.moveRel(xOffset, yOffset, duration=num_seconds) # csgo_in
    else:
        xOffset = head_pos[1]
        yOffset = head_pos[0]
        num_seconds = 0.001
        pyautogui.moveTo(xOffset*(std_sencety/my_sencety), yOffset*(std_sencety/my_sencety), duration=num_seconds)
        
    pyautogui.click(clicks=5, interval=0.1)

# mouse_move(460, 431, 796, 682)