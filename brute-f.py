#!/bin/python3
#Python Version of BruteF by johnsmith
WARNING = '\033[93m'
OKGREEN = '\033[92m'
OKBLUE = '\033[94m'
HEADER = '\033[95m'
BOLD = '\033[1m'
RED = '\033[31m'
CRED2    = '\33[91m'
BLUE = '\033[34m'
CBLUE2   = '\33[94m'
UNDERL = '\033[4m'
RESET = '\033[0m'
import os
import time
#os.system("./banner.sh")
#=================================================
os.system("clear")
print (CRED2)
print ("                                                  ")
print ("                                                  ")
print (" █████░                 █                  ██████ ")
print (" █   ▒█                 █                  █      ")
print (" █    █  █▒██▒ █   █  █████   ███          █      ")
print (" █   ▒█  ██  █ █   █    █    ▓▓ ▒█         █      ")
print (" █████░  █     █   █    █    █   █         ██████ ")
print (" █   ▒█  █     █   █    █    █████   ███   █      ")
print (" █    █  █     █   █    █    █             █      ")
print (" █   ▒█  █     █▒ ▓█    █░   ▓▓  █         █      ")
print (" █████░  █     ▒██▒█    ▒██   ███▒         █      ")
print ("                                                  ")
print ("                                        " + CBLUE2 + UNDERL + "By: john" + BLUE + "smith")
print (RESET)
ans=True
while ans:
    print (WARNING + BOLD + """
    1.http-get
    2.ftp
    3.ssh
    4.Exit/Quit
    """)
    ans=str(input(OKGREEN + "Protocol type: "))
#==============================================
    if ans=="1": 
      print(OKBLUE + "\n HTTP-GET" + RESET)
      ip = str(input("Target IP: "))
      port = str(input("Target PORT: "))
      user=True
      while user:
            print (OKBLUE + """
                HTTP-GET
    1) single username
    2) list of username
    3) Exit
    """)
            user=str(input(OKGREEN + "option: "))
            if user=="1":
              # USE -l
              print ("signle username")
              user = str(input(OKGREEN + "Username: "))
              passwd=True
              while passwd:
                    print (WARNING + BOLD + """
    Drag or Type the location of your password list
    make sure the spelling are correct. if not this
    may take some""" + RED + """ Error""" + RESET)
                    passwd = str(input("option: "))
                    # start hydra
                    show=True
                    while show:
                          print (OKGREEN + """
    1) Show Proccess
    2) Hide Proccess
    3) Exit
    """)
                          process = str(input(OKGREEN + "option: "))
                          if process=="1":
                            print (OKGREEN + "Wait...")
                            os.system("hydra -l" + user + " -P " + passwd + " -s " + port + "-f " + ip + " http-get -V")
                            print (" Found")
                            input("Press ENTER to Continue")
                          elif process=="2":
                            print (OKGREEN + "Wait...")
                            os.system("hydra -l" + user + " -P " + passwd + " -s " + port + "-f " + ip + " http-get")
                            print (" Found")
                            input("Press ENTER to Continue")
                          elif process=="3":
                            print (OKGREEN + "CLEANING & EXIT")
                            print ("Thank You!!!")
                            time.sleep(3)
                            break
                          elif process!="":
                            print(RED + "\n Not Valid Choice Try again" + OKGREEN)
                          
            elif user=="2":
              # USE -L
              print ("location/filename")
              user = str(input(OKGREEN + "Username/file: "))
              passwd=True
              while passwd:
                    print (WARNING + BOLD + """
    Drag or Type the location of your password list
    make sure the spelling are correct. if not this
    may take some""" + RED + """ Error""" + RESET)
                    passwd = str(input("option: "))
                    # start hydra
                    show=True
                    while show:
                          print (OKGREEN + """
    1) Show Proccess
    2) Hide Proccess
    3) Exit
    """)
                          process = str(input(OKGREEN + "option: "))
                          if process=="1":
                            print (OKGREEN + "Wait...")
                            os.system("hydra -L" + user + " -P " + passwd + " -s " + port + "-f " + ip + " http-get -V")
                            print (" Found")
                            input("Press ENTER to Continue")
                          elif process=="2":
                            print (OKGREEN + "Wait...")
                            os.system("hydra -L" + user + " -P " + passwd + " -s " + port + "-f " + ip + " http-get")
                            print (" Found")
                            input("Press ENTER to Continue")
                          elif process=="3":
                            print (OKGREEN + "CLEANING & EXIT")
                            print ("Thank You!!!")
                            time.sleep(3)
                            break
                          elif process!="":
                            print(RED + "\n Not Valid Choice Try again" + OKGREEN)
              
            elif user=="3":
              print("CLEANING")
              time.sleep(2)
              print("EXIT")
              break
            elif user !="":
              print(RED + "\n Not Valid Choice Try again" + RESET)
#==================================================================
    elif ans=="2":
      print(OKBLUE + "\n FTP" + RESET)
      ip = str(input("Target IP: "))
      port = str(input("Target PORT: "))
      user=True
      while user:
            print (OKBLUE + """
                HTTP-GET
    1) single username
    2) list of username
    3) Exit
    """)
            user=str(input(OKGREEN + "option: "))
            if user=="1":
              # USE -l
              print ("signle username")
              user = str(input(OKGREEN + "Username: "))
              passwd=True
              while passwd:
                    print (WARNING + BOLD + """
    Drag or Type the location of your password list
    make sure the spelling are correct. if not this
    may take some""" + RED + """ Error""" + RESET)
                    passwd = str(input("option: "))
                    # start hydra
                    show=True
                    while show:
                          print (OKGREEN + """
    1) Show Proccess
    2) Hide Proccess
    3) Exit
    """)
                          process = str(input(OKGREEN + "option: "))
                          if process=="1":
                            print (OKGREEN + "Wait...")
                            os.system("hydra -l" + user + " -P " + passwd + " -s " + port + "-f " + ip + " ftp -V")
                            print (" Found")
                            input("Press ENTER to Continue")
                          elif process=="2":
                            print (OKGREEN + "Wait...")
                            os.system("hydra -l" + user + " -P " + passwd + " -s " + port + "-f " + ip + " ftp")
                            print (" Found")
                            input("Press ENTER to Continue")
                          elif process=="3":
                            print (OKGREEN + "CLEANING & EXIT")
                            print ("Thank You!!!")
                            time.sleep(3)
                            break
                          elif process!="":
                            print(RED + "\n Not Valid Choice Try again" + OKGREEN)
                          
            elif user=="2":
              # USE -L
              print ("location/filename")
              user = str(input(OKGREEN + "Username/file: "))
              passwd=True
              while passwd:
                    print (WARNING + BOLD + """
    Drag or Type the location of your password list
    make sure the spelling are correct. if not this
    may take some""" + RED + """ Error""" + RESET)
                    passwd = str(input("option: "))
                    # start hydra
                    show=True
                    while show:
                          print (OKGREEN + """
    1) Show Proccess
    2) Hide Proccess
    3) Exit
    """)
                          process = str(input(OKGREEN + "option: "))
                          if process=="1":
                            print (OKGREEN + "Wait...")
                            os.system("hydra -L" + user + " -P " + passwd + " -s " + port + "-f " + ip + " ftp -V")
                            print (" Found")
                            input("Press ENTER to Continue")
                          elif process=="2":
                            print (OKGREEN + "Wait...")
                            os.system("hydra -L" + user + " -P " + passwd + " -s " + port + "-f " + ip + " ftp")
                            print (" Found")
                            input("Press ENTER to Continue")
                          elif process=="3":
                            print (OKGREEN + "CLEANING & EXIT")
                            print ("Thank You!!!")
                            time.sleep(3)
                            break
                          elif process!="":
                            print(RED + "\n Not Valid Choice Try again" + OKGREEN)
              
            elif user=="3":
              print("CLEANING")
              time.sleep(2)
              print("EXIT")
              break
            elif user !="":
              print(RED + "\n Not Valid Choice Try again" + RESET)
#=================================================================
    elif ans=="3":
      print(OKBLUE + "\n SSH" + RESET)
      ip = str(input("Target IP: "))
      port = str(input("Target PORT: "))
      user=True
      while user:
            print (OKBLUE + """
                HTTP-GET
    1) single username
    2) list of username
    3) Exit
    """)
            user=str(input(OKGREEN + "option: "))
            if user=="1":
              # USE -l
              print ("signle username")
              user = str(input(OKGREEN + "Username: "))
              passwd=True
              while passwd:
                    print (WARNING + BOLD + """
    Drag or Type the location of your password list
    make sure the spelling are correct. if not this
    may take some""" + RED + """ Error""" + RESET)
                    passwd = str(input("option: "))
                    # start hydra
                    show=True
                    while show:
                          print (OKGREEN + """
    1) Show Proccess
    2) Hide Proccess
    3) Exit
    """)
                          process = str(input(OKGREEN + "option: "))
                          if process=="1":
                            print (OKGREEN + "Wait...")
                            os.system("hydra -l" + user + " -P " + passwd + " -s " + port + "-f " + ip + " ssh -V")
                            print (" Found")
                            input("Press ENTER to Continue")
                          elif process=="2":
                            print (OKGREEN + "Wait...")
                            os.system("hydra -l" + user + " -P " + passwd + " -s " + port + "-f " + ip + " ssh")
                            print (" Found")
                            input("Press ENTER to Continue")
                          elif process=="3":
                            print (OKGREEN + "CLEANING & EXIT")
                            print ("Thank You!!!")
                            time.sleep(3)
                            break
                          elif process!="":
                            print(RED + "\n Not Valid Choice Try again" + OKGREEN)
                          
            elif user=="2":
              # USE -L
              print ("location/filename")
              user = str(input(OKGREEN + "Username/file: "))
              passwd=True
              while passwd:
                    print (WARNING + BOLD + """
    Drag or Type the location of your password list
    make sure the spelling are correct. if not this
    may take some""" + RED + """ Error""" + RESET)
                    passwd = str(input("option: "))
                    # start hydra
                    show=True
                    while show:
                          print (OKGREEN + """
    1) Show Proccess
    2) Hide Proccess
    3) Exit
    """)
                          process = str(input(OKGREEN + "option: "))
                          if process=="1":
                            print (OKGREEN + "Wait...")
                            os.system("hydra -L" + user + " -P " + passwd + " -s " + port + "-f " + ip + " ssh -V")
                            print (" Found")
                            input("Press ENTER to Continue")
                          elif process=="2":
                            print (OKGREEN + "Wait...")
                            os.system("hydra -L" + user + " -P " + passwd + " -s " + port + "-f " + ip + " ssh")
                            print (" Found")
                            input("Press ENTER to Continue")
                          elif process=="3":
                            print (OKGREEN + "CLEANING & EXIT")
                            print ("Thank You!!!")
                            time.sleep(3)
                            break
                          elif process!="":
                            print(RED + "\n Not Valid Choice Try again" + OKGREEN)
              
            elif user=="3":
              print("CLEANING")
              time.sleep(2)
              print("EXIT")
              break
            elif user !="":
              print(RED + "\n Not Valid Choice Try again" + RESET)
#=================================================================
    elif ans=="4":
      print(OKBLUE + "\n EXIT" + RESET)
      break
#=================================================================
    elif ans !="":
      print(RED + "\n Not Valid Choice Try again" + RESET)
