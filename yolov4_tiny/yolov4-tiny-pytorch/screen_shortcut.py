import win32gui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import sys
import qimage2ndarray

# 需要获取窗口的句柄
def get_all_hwnd(hwnd,mouse):
    hwnd_title = dict()
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})

# win32gui.EnumWindows(get_all_hwnd, 0)
 
# for h,t in hwnd_title.items():
#   if t is not "":
#     print(h, t)

'''
def QImageToCvMat(incomingImage):
    #   Converts a QImage into an opencv MAT format 

    incomingImage = incomingImage.convertToFormat(PyQt5.QtGui.QImage.Format.Format_RGB32)

    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.bits()
    ptr.setsize(height * width * 4)
    arr = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))
    return arr
'''
def screen_shortcut():
    win32gui.EnumWindows(get_all_hwnd, 0)
    hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    # print(type(img)) # <class 'PyQt5.QtGui.QImage'>
    rgb_img = qimage2ndarray.rgb_view(img)
    return rgb_img
    # plt.imshow(rgb_img)
    # plt.show()
    # ye! I did it!
# screen_shortcut()