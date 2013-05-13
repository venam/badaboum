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
import sqlite3
#---handle the db---#
class db_interaction(object):
    def __init__(self,configs):
        #---get db cursor---#
        self.conn   = sqlite3.connect('links.db')
        self.c      = self.conn.cursor()
        self.config = configs

    #---commit changes to the db---#
    def commit(self):
        self.conn.commit()

    #---get the data array--#
    def get_db_data(self):
        self.c.execute("select * from "+self.config.table_name()+" order by "+self.config.url());
        return list(self.c)

    #---do a query and return the result as array---#
    def execute(self,query):
        return list(self.c.execute(str(query)))

    #---insert data from the new_links file--#
    def insert(self):
        max_number = self.db.execute("select max("+self.config.id()+") from "+self.config.table_name())[0]
        links,ite = open(self.config.new_links(),'r').readlines() , max_number+1
        for link in links:
            link = link.split(self.config.delimiter_separator())
            self.c.execute("insert into "+self.config.table_name()+" values ("+str(ite)+",'"+link[0]+"','"+link[1]+"');")
            ite += 1

