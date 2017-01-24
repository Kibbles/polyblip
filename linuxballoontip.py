# -- coding: utf-8 --

# ------------------------------------------
# balloontip.py was originally created by wontoncc:
# https://gist.github.com/wontoncc/1808234
# ------------------------------------------
# This version includes a very minor revision to line
# 49, unregistering the class after the window is removed.

#Import the library to use libnotify.
from gi.repository import Notify

class LinuxNotify():
    """LinuxNotify calls the notification system for Linux."""
    def __init__(self, title, msg):
        #Register the application and give the class a name to use.
        Notify.init("Polyblip")
        #Make the notification and show it.
        Notify.Notification.new(title, msg).show()
        #Unregister the application.
        Notify.uninit()


def balloon_tip(title, msg):
    w = LinuxNotify(title, msg)
