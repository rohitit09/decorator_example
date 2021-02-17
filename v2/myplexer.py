#!/usr/bin/env python3
import os
import sys
import cmd2
from cmd2 import ansi

class Myplexer(cmd2.Cmd):
    avail_func={}
    def __init__(self):
        super().__init__(use_ipython=True)
        self._set_prompt()
        self.intro = 'Welcome to input shell'
        
    def route(self, command):
            def wrap(args):
                self.avail_func[command]=args
                return args	
            return wrap

    def _set_prompt(self):
        """Set prompt so it displays the current working directory."""
        self.cwd = os.getcwd()
        self.name=">"
        self.prompt = ansi.style('{}>'.format(self.name), fg='cyan')

    def do_help(self,line):
        print("Command are hi,sayhito and count")

    def do_exit(self,line):
        print(self.avail_func['exit']())

    def do_pwd(self,line):
        print(os.getcwd())

    @cmd2.with_argument_list
    def do_count(self,argument_list):
        print(self.avail_func['count'](*argument_list))

    def do_hi(self,line):
        print(self.avail_func['hi']())

    def do_sayhito(self,line):
        print(self.avail_func['sayhito $name'](line))

    @classmethod
    def run(cls):
        return sys.exit(cls().cmdloop())

if __name__ == '__main__':
    c = Myplexer()
    sys.exit(c.cmdloop())





