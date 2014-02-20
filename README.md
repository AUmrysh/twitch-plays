Twitch Plays
============

Clone of [Twitch Plays Pokemon](http://twitch.tv/twitch_plays_pokemon).



Installation
============

You're going to need to have [pywin32](http://sourceforge.net/projects/pywin32/) installed.

Move `config/config_dist.py` to `config/config.py`, and replace the username/password there with your Twitch username and [OAuth token](http://www.twitchapps.com/tmi/). Feel free to modify the start throttle here aswell.

set up for QWOP, load the flash game and this should run fine in linux.

After you've set that up, open up your terminal and type `chmod +x serve.py` then type `./serve.py`. If your username/password is wrong you will be notified.

Whilst the script is running make sure you have your QWOP game is in focus as your primary window. If you click onto another window, the script won't work. If you're not able to stay focused on one window as you need to do other things with your computer, you could try running all of this from within a virtual machine.

I would use SSH to run this in screen, personally.
