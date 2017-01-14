# polyblip
Polyblip is a Bottle notification server for Polycom VoIP phones that shows a Windows notification containing the name of the caller. It intercepts XML messages from the phone and extracts the caller information. Some assembly required.

## What you need
- A Polycom phone configured to send XML packets to your server (tested with Polycom vvx 300 phones)
- [Bottle](http://bottlepy.org/docs/dev/) (for the web server)
- [Wontoncc's `balloontip.py`](https://gist.github.com/wontoncc/1808234) for the notifier (which is included, with a hotfix for repeated message displays)
- Windows, since the dialog box relies on Windows functions. Can easily be made generic with TkInter though.

## How to configure
- You will first need to configure your phone to send messages to your computer by enabling the "Incoming Call" telephony notification on the phone's web portal. We're using Polycom vvx 300 phones; other models may or may not work (though I imagine the XML response messages are fairly standard)

![phone setup](https://i.imgur.com/c7Nid2r.png)

- Then you need to define your receiving computer's IP address and port in a file called `ip.conf`. The syntax for this file is a single line featuring `ip:port` (e.g. `127.0.0.1:1337`). You can use almost port you want; Bottle isn't very picky.

- Start your server using `call_alert.py`. If everything worked, you now have a listening bottle server. Have someone call you, and you'll get their name in a popup bubble. It also logs all received calls to `call.log`.

## Planned features
- Native cross-platform support. This one's a bit of a doozy since not all OS platforms support notifications, and having a big ugly dialog box with an "OK" button is awful.
