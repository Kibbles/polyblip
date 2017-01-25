# -- coding: utf-8 --

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
