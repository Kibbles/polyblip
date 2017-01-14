# polyblip
Polyblip is a notification server for Polycom VoIP phones that shows a Windows notification containing the name of the caller. It intercepts XML messages from the phone and extracts the caller information. It's all rather basic stuff, but it works decently well. Some assembly required.

## What you need
- A Polycom phone configured to send XML packets to your server (tested with Polycom vvx 300 phones)
- Bottle (for the web server)
- Boppreh's fork of `balloontip.py` for the notifier (included with a hotfix for repeated message displays)
- Windows, since the dialog box relies on Windows functions. Can easily be made generic with Tkinter though.

