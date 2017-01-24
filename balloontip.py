# -- coding: utf-8 --

# ------------------------------------------
# balloontip.py was originally created by wontoncc:
# https://gist.github.com/wontoncc/1808234
# ------------------------------------------
# This version includes a very minor revision to line
# 49, unregistering the class after the window is removed.



class WindowsBalloonTip:
    def __init__(self, title, msg):
        #Import libraries
        from win32api import *
        from win32gui import *
        import win32con
        import sys, os
        import struct
        import time

        message_map = {
            win32con.WM_DESTROY: self.OnDestroy,
        }
        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = message_map  # could also specify a wndproc.
        classAtom = RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow(classAtom, "Taskbar", style,
                                 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
                                 0, 0, hinst, None)
        UpdateWindow(self.hwnd)
        iconPathName = os.path.abspath(os.path.join(sys.path[0], "balloontip.ico"))
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
            hicon = LoadImage(hinst, iconPathName,
                              win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
            hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "tooltip")
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(NIM_MODIFY,
                         (self.hwnd, 0, NIF_INFO, win32con.WM_USER + 20,
                          hicon, "Balloon  tooltip", title, 200, msg))
        # self.show_balloon(title, msg)
        time.sleep(5)
        DestroyWindow(self.hwnd)
        UnregisterClass(classAtom, hinst)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)  # Terminate the app.




class LinuxNotify():
    """LinuxNotify calls the notification system for Linux."""
    def __init__(self, title, msg):
        #Import the library to use libnotify.
        from gi.repository import Notify

        #Register the application and give the class a name to use.
        Notify.init("Polyblip")
        #Make the notification and show it.
        Notify.Notification.new(title, msg).show()
        #Unregister the application.
        Notify.uninit()


def balloon_tip(title, msg):
    w = WindowsBalloonTip(msg, title)
