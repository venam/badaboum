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
import random,re
#---handle the config file--#
class config_getter(object):
    def __init__(self):
        self._config_file = open("config.conf",'r').read()
        self._db_name             = "-"
        self._table_name          = "-"
        self._id                  = "-"
        self._url                 = "-"
        self._post                = "-"
        self._rotation            = "-"
        self._nbtimes             = "-"
        self._sleeper             = "-"
        self._chrono              = "-"
        self._new_links           = "-"
        self._delimiter_email     = "-"
        self._delimiter_random    = "-"
        self._delimiter_separator = "-"
        self._threads             = "-"
        self._prompt              = "-"

    def reload(self):
        self._config_file = open("config.conf",'r').read()

    def db_name(self):
        if self._db_name!="-":
            return self._db_name
        if "db_name=" in self._config_file:
            return re.findall("db_name=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def table_name(self):
        if self._table_name!="-":
            return self._table_name
        if "table_name=" in self._config_file:
            return re.findall("table_name=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def id(self):
        if self._id!="-":
            return self._id
        if "id=" in self._config_file:
            return re.findall("id=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def url(self):
        if self._url!="-":
            return self._url
        if "url=" in self._config_file:
            return re.findall("url=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def post(self):
        if self._post!="-":
            return self._post
        if "post=" in self._config_file:
            return re.findall("post=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def rotation(self):
        if self._rotation!="-":
            return self._rotation
        if "rotation=" in self._config_file:
            return re.findall("rotation=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def nbtimes(self):
        if self._nbtimes!="-":
            return self._nbtimes
        if "nbtimes=" in self._config_file:
            return re.findall("nbtimes=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def sleeper(self):
        if self._sleeper!="-":
            return self._sleeper
        if "sleeper=" in self._config_file:
            return re.findall("db_name=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def chrono(self):
        if self._chrono!="-":
            return self._chrono
        if "chrono=" in self._config_file:
            return re.findall("chrono=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def delimiter_email(self):
        if self._delimiter_email!="-":
            return self._delimiter_email
        if "delimiter_email=" in self._config_file:
            return re.findall("delimiter_email=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def delimiter_random(self):
        if self._delimiter_random!="-":
            return self._delimiter_random
        if "delimiter_random=" in self._config_file:
            return re.findall("delimiter_random=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def delimiter_separator(self):
        if self._delimiter_separator!="-":
            return self._delimiter_separator
        if "delimiter_separator=" in self._config_file:
            return re.findall("delimiter_separator=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def new_links(self):
        if self._new_links!="-":
            return self._new_links
        if "new_links=" in self._config_file:
            return re.findall("new_links=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def threads(self):
        if self._threads!="-":
            return self._threads
        if "threads=" in self._config_file:
            return re.findall("threads=(.*)\n",self._config_file)[0]
        else:
            return "-"

    def prompt(self):
        if self._prompt!="-":
            return self._prompt
        if "prompt=" in self._config_file:
            return re.findall("prompt=(.*)\n",self._config_file)[0]
        else:
            return ">"

    #---return a random string---#
    def randomname(self):
        naming=""
        mynoomber = random.randint(5,11)
        for i in xrange(mynoomber):
            if i%2==0 :
                if random.randint(0,4)==0:
                    naming+=random.choice(['ch','sh','ph','th','pr','ck',
                        'sr','zw','tr','kr','pl','kl','sc','dr'])
                else:
                    naming+=random.choice('bcdfghjklmnpqrstvwxyz')
            else:
                naming+=random.choice('aeiou')
        return naming
