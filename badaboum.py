# -*- coding: UTF-8 -*-
'''
Copyright (c) 2015, Patrick Louis <patrick at iotek.org>

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    1.  The author is informed of the use of his/her code. The author does not
    have to consent to the use; however he/she must be informed.
    2.  If the author wishes to know when his/her code is being used, it the
    duty of the author to provide a current email address at the top of his/her
    code, above or included in the copyright statement.
    3.  The author can opt out of being contacted, by not providing a form of
    contact in the copyright statement.
    4.  If any portion of the author's code is used, credit must be given.
            a. For example, if the author's code is being modified and/or
            redistributed in the form of a closed-source binary program, then
            the end user must still be made somehow aware that the author's
            work has contributed to that program.
            b. If the code is being modified and/or redistributed in the form
            of code to be compiled, then the author's name in the copyright
            statement is sufficient.
    5.  The following copyright statement must be included at the beginning of
    the code, regardless of binary form or source code form.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


'''

import completer
import config_handler
import db_handler
import bomb_handler
import readline
import json


# ---pretty colors--- #
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[1;32m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
CYAN = '\033[1;36m'
COOL = '\033[0;45m'
COOL1 = '\033[1;45m'


class menu(object):
    def __init__(self):
        self.config = config_handler.config_getter()
        self.db = db_handler.db_interaction(self.config)
        self.target = ""
        # ---start completion--- #
        # Functions that take the rest of the input (after '=') as argument
        # and return the next state or nothing (stays in the same state)
        self.commands = {
            'menu': {
                'help': self.menu_help,
                '?': self.menu_help,
                # TODO: update it to work with json
                'config': self.change_config,
                'save': self.change_config,
                'bomb': (lambda s: 'bomb'),
                'db': (lambda s: 'db'),
                'insert': (lambda s: 'insert')
            },
            'db': {
                'help': self.db_help,
                '?': self.db_help,
                'tablename': self.db_tablename,
                'id': self.db_id,
                'url': self.db_url,
                'post': self.db_post,
                'query': self.db_sql,
                'submit': self.submit,
                'bomb': (lambda s: 'bomb'),
                'menu': (lambda s: 'menu'),
                'insert': (lambda s: 'insert')
            },
            'bomb': {
                'help': self.bomb_help,

                '?': self.bomb_help,
                'target': self.bomb_target,
                'bomb': self.bomb_bomb,
                'threads': self.bomb_threads,
                'rotation': self.bomb_rotation,
                'nbtimes': self.bomb_nbtimes,
                'chrono': self.bomb_chrono,
                'db': (lambda s: 'db'),
                'menu': (lambda s: 'menu'),
                'insert': (lambda s: 'insert')
            },
            'insert': {
                'help': self.insert_help,
                '?': self.insert_help,
                'insert': self.insert_file,
                'separator': self.insert_separator,
                'email': self.insert_email,
                'random': self.insert_random,
                'submit': self.submit,
                'db': (lambda s: 'db'),
                'menu': (lambda s: 'menu'),
                'bomb': (lambda s: 'bomb')
            }
        }
        self.default_mode = 'menu'
        self.comp = completer.Completer(self.default_mode, self.commands)
        readline.set_completer_delims(' \t\n;')
        readline.parse_and_bind("tab:complete")
        readline.set_completer(self.comp.complete)

    def menu_help(self, n):
        print """
bomb      : Enter bomb mode (Setup and start flooding an email)
db        : Enter db mode (get infos and execute sql query over the db)
insert    : Enter intert mode (insert new data in the db easily)
config    : Apply changes to the configs
exit      : Exit the program
help/?    : Display this help menu
"""

    def db_help(self, n):
        print """
Keep the order of the column (id,url,post), change them in this way: id=newid
tablename : Display the current table name set in the configs
id        : Displaay the name of the column id
url       : Display the name of the column url
post      : Display the name of the column post
query=sql : Write an sql query and you'll receive the output
            (replace sql with any query)
submit    : Submit changes to the DB (After the execution of a query)
menu      : Go back to the main menu
exit      : Exit the program
help/?    : Display this help menu
"""

    def bomb_help(self, n):
        print """
target=   : The email to attack
bomb      : Start the bombing
threads   : Number of threads running at the same time
rotation  : Number of time each of threads loop through the list
nbtimes   : Number of times to send messages
chrono    : The timeout
menu      : Go back to the main menu
exit      : Exit the program
help/?    : Display this help menu
"""

    def insert_help(self, n):
        print """
file      : Display the name of the file with the new data to add
            (= to change it)
separator : Display the separator between url and post (= to change it)
email     : Display the current email separator (= to change it)
random    : Display the current random separator (= to change it)
insert    : Insert the new data with the current configs (from the file)
submit    : Commit the insertion in the db
menu      : Go back to the main menu
exit      : Exit the program
help/?    : Display this help menu
"""

    def set_config(self, conf, value):
        if value and value != "":
            self.config._config[conf] = value
        print self.config._config[conf]

    def db_tablename(self, n_table): self.set_config('table_name', n_table)

    def db_id(self, n_id): self.set_config('id', n_id)

    def db_url(self, n_url): self.set_config('url', n_url)

    def db_post(self, n_post): self.set_config('post', n_post)

    def bomb_threads(self, n_threads): self.set_config('threads', n_threads)

    def bomb_rotation(self, n_rotation): self.set_config(
        'rotation', n_rotation)

    def bomb_nbtimes(self, n_times): self.set_config('nbtimes', n_times)

    def bomb_chrono(self, n_chrono): self.set_config('chrono', n_chrono)

    def insert_file(self, n_file): self.set_config('new_links', n_file)

    def insert_separator(self, n_sep): self.set_config(
        'delimiter_separator', n_sep)

    def insert_email(self, n_e): self.set_config('delimiter_email', n_e)

    def insert_random(self, n_r): self.set_config('delimiter_random', n_r)

    def submit(self, n): self.db.commit()

    def db_sql(self, query):
        try:
            print self.db.execute(query)
        except Exception, e:
            print e

    # TODO
    def change_config(self, n):
        json_encoder = json.JSONEncoder(indent=4)
        open("config.json", 'w').write(
            json_encoder.encode(self.config._config))

    def bomb_target(self, n_target):
        if n_target != "":
            self.target = n_target
        print self.target

    def bomb_bomb(self, rest):
        if '@' not in self.target:
            print "wrong email"
        else:
            bomb = bomb_handler.baboum(self.target, self.config, self.db)
            bomb.start_thread()

    def main_menu(self):
        while True:
            option = raw_input(
                OKGREEN+self.comp.mode+" "+self.config.prompt()+ENDC+" ")
            option = option.strip()  # First stripping babe
            if option in ['exit', 'quit', 'q']:
                break
            splitted_command = option.partition('=')
            c, r = splitted_command[0].strip(), splitted_command[2].strip()
            if c in filter(
                    lambda x: x != self.comp.mode,
                    self.commands[self.comp.mode].keys()):
                next_mode = self.commands[self.comp.mode][c](r)
                if next_mode in self.commands.keys():
                    self.comp.mode = next_mode


# ---run the program--- #
the_menu = menu()
the_menu.main_menu()
