from game import Game
from misc import pp, pbot, pbutton
import irc.bot
import irc.strings

import time

class Bot(irc.bot.SingleServerIRCBot):
    def __init__(self, config):
        irc.bot.SingleServerIRCBot.__init__(self, [(config['irc']['server'], 6667, config['account']['password'])], config['account']['username'].lower(), config['account']['username'].lower())
        self.channel = ("#%s"  % config['account']['username'].lower())
        self.config = config
        self.game = Game()

    def on_welcome(self, c, e):
        pp(self.channel)
        c.join(self.channel)

    def on_privmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection

        #send command to the bot
        self.game.push_button(nick, cmd)
