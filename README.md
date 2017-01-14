# polyblip
Polyblip is a Bottle notification server for Polycom VoIP phones that shows a Windows notification containing the name of the caller. It intercepts XML messages from the phone and extracts the caller information. It's all rather basic stuff, but it works decently well. Some assembly required.

## What you need
- A Polycom phone configured to send XML packets to your server (tested with Polycom vvx 300 phones)
- [Bottle](http://bottlepy.org/docs/dev/) (for the web server)
- [Wontoncc's `balloontip.py`](https://gist.github.com/wontoncc/1808234) for the notifier (included with a hotfix for repeated message displays)
- Windows, since the dialog box relies on Windows functions. Can easily be made generic with TkInter though.

## How to configure
- You will first need to configure your phone to send messages to your computer:
![phone setup](https://i.imgur.com/c7Nid2r.png)
