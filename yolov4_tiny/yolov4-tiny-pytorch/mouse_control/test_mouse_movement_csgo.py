import pyautogui
import os
import time

'''
# 获取当前鼠标位置
print(pyautogui.position())
# 获取当前屏幕的分辨率
print(pyautogui.size())
# 判断某个坐标是否在屏幕上
x=10
y=20
print(pyautogui.onScreen(x, y)) 
'''

'''
# 用num_seconds(秒)将鼠标移动到(x,y)位置
x = 200
y = 100
num_seconds = 1
pyautogui.moveTo(x, y, duration=num_seconds)  

# 用num_seconds(秒)将鼠标从当前位置向右移动xOffset，向下移动yOffset
# 如果duration为0或未指定，则立即移动。
xOffset = 30
yOffset = -50
num_seconds = 0.5
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds) 
'''

'''
# 用num_seconds(秒)将鼠标推动到(x,y)位置
# 鼠标拖动是指按下鼠标左键移动鼠标。
x = 200
y = 100
num_seconds= 1
pyautogui.dragTo(x, y, duration=num_seconds)  

# 用num_seconds(秒)将鼠标从当前位置向右拖动xOffset，向下推动yOffset
xOffset = 30
yOffset = -50
num_seconds = 0.5
pyautogui.dragRel(xOffset, yOffset, duration=num_seconds) 
'''

'''
# 将鼠标移动到(moveToX,moveToY)位置，点击鼠标num_of_clicks次，每次点击间隔secs_between_clicks秒
# button表示单击方式，'left'左键单击，'middle'中键单击，'right'右键单击
moveToX = 500
moveToY = 600
num_of_clicks = 1
secs_between_clicks = 1
pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
'''

'''
moveToX = 10
moveToY = 20
# 右键单击
pyautogui.rightClick(x=moveToX + 50, y=moveToY)
# 中键单击
pyautogui.middleClick(x=moveToX + 50, y=moveToY)
# 左键双击
pyautogui.doubleClick(x=moveToX + 50, y=moveToY)
# 左键三击
pyautogui.tripleClick(x=moveToX + 50, y=moveToY)
'''

'''
# 鼠标移动到(moveToX,moveToY)位置，鼠标左键按下
pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
# 鼠标移动到(moveToX,moveToY)位置，鼠标右键松开（按下右键的情况下）
pyautogui.mouseUp(x=moveToX, y=moveToY, button='right')
# 鼠标在当前位置，按下中键
pyautogui.mouseDown(button='middle')
'''

time.sleep(5)
# while(True):
#     print(pyautogui.position())
#     time.sleep(0.5)
# 获取当前屏幕的分辨率
print(pyautogui.size())

x = 400
y = 100
num_seconds = 1
pyautogui.moveTo(x, y, duration=num_seconds)  