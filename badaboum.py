# -*- coding: UTF-8 -*-
'''
Copyright (c) 2013, Patrick Louis <patrick at unixhub.net>

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    1.  The author is informed of the use of his/her code. The author does not have to consent to the use; however he/she must be informed.
    2.  If the author wishes to know when his/her code is being used, it the duty of the author to provide a current email address at the top of his/her code, above or included in the copyright statement.
    3.  The author can opt out of being contacted, by not providing a form of contact in the copyright statement.
    4.  If any portion of the author's code is used, credit must be given.
            a. For example, if the author's code is being modified and/or redistributed in the form of a closed-source binary program, then the end user must still be made somehow aware that the author's work has contributed to that program.
            b. If the code is being modified and/or redistributed in the form of code to be compiled, then the author's name in the copyright statement is sufficient.
    5.  The following copyright statement must be included at the beginning of the code, regardless of binary form or source code form.

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
import completer,config_handler,db_handler,bomb_handler,readline

#---pretty colors---#
HEADER  = '\033[95m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[1;32m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'
CYAN    = '\033[1;36m'
COOL    = '\033[0;45m'
COOL1   = '\033[1;45m'

class menu(object):
    def __init__(self):
        self.endprogram = False
        self.config     = config_handler.config_getter()
        self.db         = db_handler.db_interaction(self.config)
        self.target     = ""
        #---start completion---#
        self.comp = completer.Completer()
        readline.set_completer_delims(' \t\n;')
        readline.parse_and_bind("tab:complete")
        readline.set_completer(self.comp.complete)

    def menu_mode(self):
        option = raw_input(OKGREEN+"  "+self.config.prompt()+ENDC+" ")
        #---menu related options---#
        if option == 'db':
            self.comp.mode = 'db'
        elif option == 'bomb':
            self.comp.mode = 'bomb'
        elif option == 'insert':
            self.comp.mode = 'insert'
        elif option == 'exit':
            self.endprogram = True
        #---main menu---#
        elif option == 'config' :
            self.change_config()
        elif option == '?' or option == 'help':
            print """
    bomb      : Enter bomb mode (Setup and start flooding an email)
    db        : Enter db mode (get infos and execute sql query over the db)
    insert    : Enter intert mode (insert new data in the db easily)
    config    : Apply changes to the configs
    exit      : Exit the program
    help/?    : Display this help menu
                    """

    def change_config(self):
        open("config.conf",'w').write("---CONFIGS---\ndb_name="+self.config.db_name()+"\nprompt="+self.config.prompt()+"\ntable_name="+self.config.table_name()+"\nid="+self.config.id()+"\nurl="+self.config.url()+"\npost="+self.config.post()+"\nrotation="+self.config.rotation()+"\nnbtimes="+self.config.nbtimes()+"\nsleeper="+self.config.sleeper()+"\nchrono="+self.config.chrono()+"\nthreads="+self.config.threads()+"\nnew_links="+self.config.new_links()+"\ndelimiter_email="+self.config.delimiter_email()+"\ndelimiter_random="+self.config.delimiter_random()+"\ndelimiter_separator="+self.config.delimiter_separator()+"\n")

    def db_mode(self):
        option = raw_input(OKGREEN+"db "+self.config.prompt()+ENDC+" ")
        #---menu related options---#
        if option == 'menu':
            self.comp.mode = 'menu'
        elif option == 'bomb':
            self.comp.mode = 'bomb'
        elif option == 'insert':
            self.comp.mode = 'insert'
        elif option == 'exit':
            self.endprogram = True
        #---db related options---#
        elif option == '?' or option == 'help':
            print """
    Keep the order of the column (id,url,post), change them in this way: id=newid
    tablename : Display the current table name set in the configs
    id        : Displaay the name of the column id
    url       : Display the name of the column url
    post      : Display the name of the column post
    sql query : Write an sql query and you'll receive the output (no need to write sql before)
    submit    : Submit changes to the DB (After the execution of a query)
    menu      : Go back to the main menu
    exit      : Exit the program
    help/?    : Display this help menu
                    """
        elif 'tablename=' in option:
            self.config._table_name = option.replace('tablename=','')
        elif 'id=' in option:
            self.config._id         = option.replace('id=','')
        elif 'url=' in option:
            self.config._url        = option.replace('url=','')
        elif 'post=' in option:
            self.config._post       = option.replace('post=','')
        elif option == 'tablename':
            print self.config.table_name()
        elif option == 'id':
            print self.config.id()
        elif option == 'url':
            print self.config.url()
        elif option == 'post':
            print self.config.post()
        elif option == 'submit':
            self.db.commit()
        elif option != "":
            try:
                print self.db.execute(option)
            except Exception, e:
                print e

    def bomb_mode(self):
        option = raw_input(OKGREEN+"bomb "+self.config.prompt()+ENDC+" ")
        #---menu related options---#
        if option == 'menu':
            self.comp.mode = 'menu'
        elif option == 'db':
            self.comp.mode = 'db'
        elif option == 'insert':
            self.comp.mode = 'insert'
        elif option == 'exit':
            self.endprogram = True
        #---bomb related options---#
        elif 'target=' in option :
            self.target = option.replace('target=','')
        elif option == 'target':
            print self.target
        elif 'threads=' in option:
            self.config._threads = option.replace('threads=','')
        elif option == 'threads':
            print self.config.threads()
        elif 'rotation=' in option:
            self.config._rotation = option.replace('rotation=','')
        elif option == 'rotation':
            print self.config.rotation()
        elif 'nbtimes=' in option:
            self.config._nbtimes = option.replace('nbtimes=','')
        elif option == 'nbtimes':
            print self.config.nbtimes()
        elif 'chrono=' in option:
            self.config._chrono = option.replace('chrono=','')
        elif option == 'chrono':
            print self.config.chrono()
        elif option == 'bomb':
            if '@' not in self.target :
                print "wrong email"
            else :
                bomb = bomb_handler.baboum(self.target,self.config,self.db)
                bomb.start_thread()
        elif option == 'help' or option == '?':
            print """
    target=   : The email to attack
    threads   : Number of threads running at the same time
    rotation  : Number of time each of threads loop through the list
    nbtimes   : Number of times to send messages
    chrono    : The timeout
    menu      : Go back to the main menu
    exit      : Exit the program
    help/?    : Display this help menu
    """

    def insert_mode(self):
        option = raw_input(OKGREEN+"insert "+self.config.prompt()+ENDC+" ")
        #---menu related options---#
        if option == 'menu':
            self.comp.mode = 'menu'
        elif option == 'bomb':
            self.comp.mode = 'bomb'
        elif option == 'db':
            self.comp.mode = 'db'
        elif option == 'exit':
            self.endprogram = True
        #---insert related options---#
        elif 'file=' in option:
            self.config._new_links = option.replace('file=','')
        elif 'separator=' in option:
            self.config._delimiter_separator = option.replace('separator=','')
        elif 'email=' in option:
            self.config._delimiter_email = option.replace('email=','')
        elif 'random=' in option:
            self.config._delimiter_random = option.replace('random=','')
        elif option =='file':
            print self.config.new_links()
        elif option =='separator':
            print self.config.delimiter_separator()
        elif option =='email':
            print self.config.delimiter_email()
        elif option =='random':
            print self.config.delimiter_random()
        elif option =='insert':
            self.db.insert()
        elif option == 'submit':
            self.db.commit()
        elif option == 'help' or option == '?':
            print """
    file      : Display the name of the file with the new data to add (= to change it)
    separator : Display the separator between url and post (= to change it)
    email     : Display the current email separator (= to change it)
    random    : Display the current random separator (= to change it)
    insert    : Insert the new data with the current configs (from the file)
    submit    : Commit the insertion in the db
    menu      : Go back to the main menu
    exit      : Exit the program
    help/?    : Display this help menu
    """

    def main_menu(self):
        while not self.endprogram:
            if self.comp.mode == 'menu':
                self.menu_mode()
            elif self.comp.mode == 'db':
                self.db_mode()
            elif self.comp.mode == 'bomb':
                self.bomb_mode()
            elif self.comp.mode == 'insert':
                self.insert_mode()

#---run the program---#
the_menu = menu()
the_menu.main_menu()
