#!/usr/bin/env python2.7
#
#
#

import os
import sys
d3=os.system("curl http://ipinfo.io/ip")
os.system("clear && clear && clear")
logo = '''\033[0m 
   _|_|_|            _|                      
 _|        _|  _|_|      _|_|_|      _|_|_|  
 _|        _|_|      _|  _|    _|  _|_|      
 _|        _|        _|  _|    _|      _|_|  
   _|_|_|  _|        _|  _|_|_|    _|_|_|    
                         _|                  
                         _| \033[0m  \033[91m    \033[1m 
       }--{+} Coded By Manisso {+}--{
     }----{+}  fb.me/dzmanisso {+}----{
       }--{+} Greetz To IcoDz  {+}--{                               
     '''
menu = '''\033[0m
    {1}--Whois lookup
    {2}--Traceroute
    {3}--DNS Lookup
    {4}--Reverse DNS Lookup
    {5}--GeoIP Lookup
    {6}--Port Scan
    {7}--Reverse IP Lookup
    {0}--INSTALL & UPDATE
    {99}-Exit                                                                                                                   
 '''
print logo
print menu
def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                print logo
                print menu
                select()
           
def  select():
  try:
    choice = input("Crips~# ")
    if choice == 1:
      d3 = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
 _       ____  ______  _________
| |     / / / / / __ \/  _/ ___/
| | /| / / /_/ / / / // / \__ \ 
| |/ |/ / __  / /_/ _/ / ___/ / 
|__/|__/_/ /_/\____/___//____/                                  
      """)
      os.system("curl http://api.hackertarget.com/whois/?q=" + d3)
      print("")
      quit()
    elif choice == 0:
	  os.system("clear")
	  print("This tool is only available for Linux and similar systems  ")
	  os.system("git clone https://github.com/Manisso/Crips.git")
	  os.system("cd Crips && sudo bash ./update.sh")
	  os.system("crips")
    elif choice == 2:
      d3 = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
 ____ ____   __   ___ ____ ____ _____ __  __ ____ ____ 
(_  _(  _ \ /__\ / __( ___(  _ (  _  (  )(  (_  _( ___)
  )(  )   //(__)( (__ )__) )   /)(_)( )(__)(  )(  )__) 
 (__)(_)\_(__)(__\___(____(_)\_(_____(______)(__)(____)
""")
      os.system("curl https://api.hackertarget.com/mtr/?q=" + d3 )
      print("")
      quit()
    elif choice == 3:
      d3 = raw_input('Enter Domain : ')
      os.system("clear")
      print("""
______ _   _ _____   _                 _                
|  _  | \ | /  ___| | |               | |               
| | | |  \| \ `--.  | |     ___   ___ | | ___   _ _ __  
| | | | . ` |`--. \ | |    / _ \ / _ \| |/ | | | | '_ \ 
| |/ /| |\  /\__/ / | |___| (_) | (_) |   <| |_| | |_) |
|___/ \_| \_\____/  \_____/\___/ \___/|_|\_\\__,_| .__ / 
                                                 | |    
                                                 |_|     
""")
      os.system("curl http://api.hackertarget.com/dnslookup/?q=" + d3 )
      print("")
      quit()    
    elif choice == 0:
      print "Bye Bye"
      os.system("clear")
      exit()
    elif choice == 4:
	  d3 = raw_input('Enter IP Address - IP Range Or Domain  : ')
	  os.system("clear")
	  print("""
 _____                            ____  _____ _____ 
| __  |___ _ _ ___ ___ ___ ___   |    \|   | |   __|
|    -| -_| | | -_|  _|_ -| -_|  |  |  | | | |__   |
|__|__|___|\_/|___|_| |___|___|  |____/|_|___|_____|
                                                    
	  """)
	  os.system("curl https://api.hackertarget.com/reversedns/?q=" + d3 )
	  print("")
	  quit()
    elif choice == 5:
	  d3 = raw_input('Enter IP Or Domain : ')
	  os.system("clear")
	  print("""
   _____           _____ _____  
  / ____|         |_   _|  __ \ 
 | |  __  ___  ___  | | | |__) |
 | | |_ |/ _ \/ _ \ | | |  ___/ 
 | |__| |  __| (_) _| |_| |     
  \_____|\___|\___|_____|_|     
                                	
	""")
	  os.system("curl http://api.hackertarget.com/geoip/?q=" + d3 )
	  print("")
	  print("")
	  quit()
    elif choice == 6:
      d3 = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
     __                         __                 
  /\ \ \_ __ ___   __ _ _ __   / _\ ___ __ _ _ __  
 /  \/ | '_ ` _ \ / _` | '_ \  \ \ / __/ _` | '_ \ 
/ /\  /| | | | | | (_| | |_) | _\ | (_| (_| | | | |
\_\ \/ |_| |_| |_|\__,_| .__/  \__/\___\__,_|_| |_|
                       |_|                         
      """)
      os.system("curl http://api.hackertarget.com/nmap/?q=" + d3 )
      print("")
      quit()
    elif choice == 7:
	  d3 = raw_input('Enter IP Or Domain : ')
	  os.system("clear")
	  print("""
 (   (      (                             
 )\ ))\ )   )\ )            )             
(()/(()/(  (()/(         ( /(   (         
 /(_)/(_))  /(_)) (   (  )\()) ))\ `  )   
(_))(_))   (_))   )\  )\((_)\ /((_)/(/(   
|_ _| _ \  | |   ((_)((_| |(_(_))(((_)_\  
 | ||  _/  | |__/ _ / _ | / /| || | '_ \) 
|___|_|    |____\___\___|_\_\ \_,_| .__/  
                                  |_|     
	  """)
	  os.system("wget http://api.hackertarget.com/reverseiplookup/?q=" + d3 )
	  os.system("clear")
	  os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + d3 )
	  print("")
	  print("\033[91m\033[1mFile Saved On : ")
	  os.system("pwd")
	  print("File : index.html?q=" +d3)
	  print("\033[0m")
	  quit()
  except(KeyboardInterrupt):
    print ""
select()
