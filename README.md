# polyblip
Polyblip is a notification server for Polycom VoIP phones that shows a Windows notification containing the name of the caller. It intercepts XML messages from the phone and extracts the caller information.

## What you need
- Bottle (for the web server)
- Boppreh's fork of `balloontip.py` for the notifier
- A Polycom phone configured to send XML packets to your server

