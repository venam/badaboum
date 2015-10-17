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

import random
import re
import json


# ---handle the config file-- #
class config_getter(object):
    def __init__(self):
        self._config = json.load(open("config.json", 'r'))
        for i in self._config.keys():
            def t(self, v=i):
                return self._config[v]
            self.add_method(t, i)

    def reload(self):
        self._config = json.load(open("config.conf", 'r'))

    def add_method(self, method, name=None):
        if name is None:
            name = method.func_name

        class new(self.__class__):
            pass
        setattr(new, name, method)
        self.__class__ = new

    # ---return a random string--- #
    def randomname(self):
        naming = ""
        mynoomber = random.randint(5, 11)
        for i in xrange(mynoomber):
            if i % 2 == 0:
                if random.randint(0, 4) == 0:
                    naming += random.choice(
                        [
                            'ch', 'sh', 'ph', 'th', 'pr', 'ck', 'sr', 'zw',
                            'tr', 'kr', 'pl', 'kl', 'sc', 'dr'])
                else:
                    naming += random.choice('bcdfghjklmnpqrstvwxyz')
            else:
                naming += random.choice('aeiou')
        return naming
